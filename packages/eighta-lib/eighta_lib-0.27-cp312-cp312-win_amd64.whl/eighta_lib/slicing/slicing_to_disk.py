"""
This module provides functions and utilities for exploring, processing, slicing,
and writing HDF5 files to disk, specifically targeting the AnnData format and its components.
"""
import threading
import h5py
import numpy as np
import psutil
import slicers_write

# Lock for locking mechanism of write_slice_h5ad.
write_lock = threading.Lock()

def get_memory_info() -> tuple[int, float]:
    """
    Retrieves the available system memory in bytes and gigabytes.

    Returns:
        tuple: A tuple containing:
            - available_memory_b (int): The available memory in bytes.
            - available_memory_gb (float): The available memory in gigabytes.
    """
    available_memory_b = psutil.virtual_memory().available
    available_memory_gb = available_memory_b / (1024 ** 3)
    return available_memory_b, available_memory_gb


def calculate_batch_size(memory_fraction: float, num_cols: int, dtype_size: int) -> int:
    """
    Calculates the batch size for data processing based on the available memory,
    fraction of memory to use, number of columns, and data type size.

    Args:
        memory_fraction (float): The fraction of available memory to use.
        num_cols (int): The number of columns in the dataset.
        dtype_size (int): The size of the data type in bytes.

    Returns:
        int: The calculated batch size. Ensures a minimum batch size of 1.
    """
    available_memory_b, _ = get_memory_info()
    memory_to_use = available_memory_b * memory_fraction
    row_size = num_cols * dtype_size
    return max(1, int(memory_to_use // row_size))


def copy_attrs(
    source: h5py.AttributeManager,
    dest: h5py.AttributeManager,
    shape: tuple | None = None
) -> None:
    """
    Copies attributes from the source to the destination HDF5 object.

    Args:
        source (h5py.AttributeManager): The source HDF5 object containing attributes.
        dest (h5py.AttributeManager): The destination HDF5 object to copy the attributes to.
        shape (tuple, optional): The shape to set as an attribute in the destination.
            Default is None.

    Raises:
        ValueError: If the destination object is invalid.
    """
    # Ensure the destination object is valid before copying attributes
    if not dest or not hasattr(dest, 'attrs'):
        raise ValueError("Invalid destination object. Cannot copy attributes.")

    # Copy each attribute from the source to the destination
    for key, value in source.attrs.items():
        dest.attrs[key] = value

    # If a shape is provided, set it as an attribute in the destination
    if shape is not None:
        dest.attrs['shape'] = shape


def write_process_csr_matrix(
    source_group: h5py.Group,
    dest_file_path: str,
    row_indices: np.ndarray,
    col_indices: np.ndarray,
    batch_size: int
) -> None:
    """
    Processes and writes a CSR matrix to the destination HDF5 file with specified slicing.

    Args:
        source_group (h5py.Group): The source group containing the CSR matrix.
        dest_file_path (str): The path to the destination HDF5 file.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        col_indices (np.ndarray): The indices of the columns to include in the slice.
        batch_size (int): The size of the batch for processing large datasets.
    """
    with write_lock:
        with h5py.File(dest_file_path, 'a') as f_dest:
            # Create destination datasets with initial empty shapes and appropriate compression
            dest_group = f_dest.require_group(source_group.name)
            data_group = dest_group.create_dataset(
                'data', shape=(0,), maxshape=(None,), dtype=source_group['data'].dtype,
                compression=source_group['data'].compression
            )
            indices_group = dest_group.create_dataset(
                'indices', shape=(0,), maxshape=(None,), dtype=source_group['indices'].dtype,
                compression=source_group['indices'].compression
            )
            indptr_group = dest_group.create_dataset(
                'indptr', shape=(len(row_indices) + 1,), dtype=source_group['indptr'].dtype,
                compression=source_group['indptr'].compression
            )
            indptr_group[0] = 0

    # Initialize the total indptr array and current length counter
    total_indptr = np.zeros(len(row_indices) + 1, dtype=source_group['indptr'].dtype)
    current_length = 0

    # Process the data in batches
    for start in range(0, len(row_indices), batch_size):
        end = min(start + batch_size, len(row_indices))
        batch_row_indices = row_indices[start:end]

        for i, row_idx in enumerate(batch_row_indices, start=start):
            data_start_idx = source_group['indptr'][row_idx]
            data_end_idx = source_group['indptr'][row_idx + 1]

            if data_start_idx < data_end_idx:
                # Extract data and indices for the current row
                data = source_group['data'][data_start_idx:data_end_idx]
                indices = source_group['indices'][data_start_idx:data_end_idx]

                # Mask and map indices to the new column indices
                mask = np.isin(indices, col_indices)
                data = data[mask]
                indices = indices[mask]

                index_map = {col: i for i, col in enumerate(col_indices)}
                indices = np.array([index_map[i] for i in indices])

                # Write data to the destination datasets
                with write_lock:
                    with h5py.File(dest_file_path, 'a') as f_dest:
                        dest_group = f_dest.require_group(source_group.name)
                        data_group = dest_group['data']
                        indices_group = dest_group['indices']

                        data_group.resize((current_length + data.shape[0],))
                        indices_group.resize((current_length + indices.shape[0],))

                        data_group[current_length:current_length + data.shape[0]] = data
                        indices_group[current_length:current_length + indices.shape[0]] = indices

                current_length += data.shape[0]
                total_indptr[i + 1] = current_length

    # Write the indptr to the destination dataset
    with write_lock:
        with h5py.File(dest_file_path, 'a') as f_dest:
            dest_group = f_dest.require_group(source_group.name)
            indptr_group = dest_group['indptr']
            indptr_group[:] = total_indptr
            copy_attrs(source_group, dest_group, shape=(len(row_indices), len(col_indices)))


def write_process_csc_matrix(
    source_group: h5py.Group,
    dest_file_path: str,
    row_indices: np.ndarray,
    col_indices: np.ndarray,
    batch_size: int
) -> None:
    """
    Processes and writes a CSC matrix to the destination HDF5 file with specified slicing.

    Args:
        source_group (h5py.Group): The source group containing the CSC matrix.
        dest_file_path (str): The path to the destination HDF5 file.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        col_indices (np.ndarray): The indices of the columns to include in the slice.
        batch_size (int): The size of the batch for processing large datasets.
    """
    with write_lock:
        with h5py.File(dest_file_path, 'a') as f_dest:
            # Create destination datasets with initial empty shapes and appropriate compression
            dest_group = f_dest.require_group(source_group.name)
            data_group = dest_group.create_dataset(
                'data', shape=(0,), maxshape=(None,), dtype=source_group['data'].dtype,
                compression=source_group['data'].compression
            )
            indices_group = dest_group.create_dataset(
                'indices', shape=(0,), maxshape=(None,), dtype=source_group['indices'].dtype,
                compression=source_group['indices'].compression
            )
            indptr_group = dest_group.create_dataset(
                'indptr', shape=(len(col_indices) + 1,), dtype=source_group['indptr'].dtype,
                compression=source_group['indptr'].compression
            )
            indptr_group[0] = 0

    # Initialize the total indptr array and current length counter
    total_indptr = np.zeros(len(col_indices) + 1, dtype=source_group['indptr'].dtype)
    current_length = 0

    # Process the data in batches
    for start in range(0, len(col_indices), batch_size):
        end = min(start + batch_size, len(col_indices))
        batch_col_indices = col_indices[start:end]

        for i, col_idx in enumerate(batch_col_indices, start=start):
            data_start_idx = source_group['indptr'][col_idx]
            data_end_idx = source_group['indptr'][col_idx + 1]

            if data_start_idx < data_end_idx:
                # Extract data and indices for the current column
                data = source_group['data'][data_start_idx:data_end_idx]
                indices = source_group['indices'][data_start_idx:data_end_idx]

                # Mask and map indices to the new row indices
                mask = np.isin(indices, row_indices)
                data = data[mask]
                indices = indices[mask]

                index_map = {row: i for i, row in enumerate(row_indices)}
                indices = np.array([index_map[i] for i in indices])

                # Write data to the destination datasets
                with write_lock:
                    with h5py.File(dest_file_path, 'a') as f_dest:
                        dest_group = f_dest.require_group(source_group.name)
                        data_group = dest_group['data']
                        indices_group = dest_group['indices']

                        data_group.resize((current_length + data.shape[0],))
                        indices_group.resize((current_length + indices.shape[0],))

                        data_group[current_length:current_length + data.shape[0]] = data
                        indices_group[current_length:current_length + indices.shape[0]] = indices

                current_length += data.shape[0]
                total_indptr[i + 1] = current_length

    # Write the indptr to the destination dataset
    with write_lock:
        with h5py.File(dest_file_path, 'a') as f_dest:
            dest_group = f_dest.require_group(source_group.name)
            indptr_group = dest_group['indptr']
            indptr_group[:] = total_indptr
            copy_attrs(source_group, dest_group, shape=(len(row_indices), len(col_indices)))


def write_process_matrix(
    source_group: h5py.Group,
    dest_file_path: str,
    row_indices: np.ndarray,
    col_indices: np.ndarray,
    batch_size: int,
    is_csr: bool
) -> None:
    """
    Processes and writes a matrix (CSR or CSC) to the destination HDF5 file with specified slicing.

    Args:
        source_group (h5py.Group): The source group containing the matrix.
        dest_file_path (str): The path to the destination HDF5 file.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        col_indices (np.ndarray): The indices of the columns to include in the slice.
        batch_size (int): The size of the batch for processing large datasets.
        is_csr (bool): Flag indicating if the matrix is CSR (True) or CSC (False).
    """
    # Kept here for C integration.
    if is_csr:
        with write_lock:
            with h5py.File(dest_file_path, 'a') as f_dest:
                dest_group = f_dest.require_group(source_group.name)
                dest_group.create_dataset(
                    'data', shape=(0,), maxshape=(None,), dtype=source_group['data'].dtype,
                    compression=source_group['data'].compression
                )
                dest_group.create_dataset(
                    'indices', shape=(0,), maxshape=(None,), dtype=source_group['indices'].dtype,
                    compression=source_group['indices'].compression
                )
                dest_group.create_dataset(
                    'indptr', shape=(len(row_indices) + 1,), dtype=source_group['indptr'].dtype,
                    compression=source_group['indptr'].compression
                )
        slicers_write.write_process_csr_matrix(
          source_group.file.filename,
          dest_file_path,
          source_group.name,
          row_indices,
          col_indices,
          batch_size
        )
    else:
        with write_lock:
            with h5py.File(dest_file_path, 'a') as f_dest:
                dest_group = f_dest.require_group(source_group.name)
                dest_group.create_dataset(
                    'data', shape=(0,), maxshape=(None,), dtype=source_group['data'].dtype,
                    compression=source_group['data'].compression
                )
                dest_group.create_dataset(
                    'indices', shape=(0,), maxshape=(None,), dtype=source_group['indices'].dtype,
                    compression=source_group['indices'].compression
                )
                dest_group.create_dataset(
                    'indptr', shape=(len(col_indices) + 1,), dtype=source_group['indptr'].dtype,
                    compression=source_group['indptr'].compression
                )
        slicers_write.write_process_csc_matrix(
          source_group.file.filename,
          dest_file_path,
          source_group.name,
          row_indices,
          col_indices,
          batch_size
        )
    with write_lock:
        with h5py.File(dest_file_path, 'a') as f_dest:
            dest_group = f_dest.require_group(source_group.name)
            copy_attrs(source_group, dest_group, shape=(len(row_indices), len(col_indices)))
    # if is_csr:
    #     write_process_csr_matrix(source_group, dest_file_path, row_indices, col_indices, batch_size)
    # else:
    #     write_process_csc_matrix(source_group, dest_file_path, row_indices, col_indices, batch_size)


def write_process_categorical_group(
    source_group: h5py.Group,
    dest_file_path: str,
    row_indices: np.ndarray,
    col_indices: np.ndarray
) -> None:
    """
    Processes and writes a categorical group to the destination HDF5 file with specified slicing.

    Args:
        source_group (h5py.Group): The source group to process.
        dest_file_path (str): The path to the destination HDF5 file.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        col_indices (np.ndarray): The indices of the columns to include in the slice.
    """
    # Extract categories from the source group
    categories = source_group['categories'][:]

    # Determine whether to use row or column indices based on the group's name
    if 'var' in source_group.name:
        codes = source_group['codes'][col_indices]
    elif 'obs' in source_group.name:
        codes = source_group['codes'][row_indices]

    # Get unique codes and their corresponding categories
    unique_codes = np.unique(codes)
    new_categories = categories[unique_codes]

    # Ensure new_categories contains only unique values
    unique_new_categories, unique_indices = np.unique(new_categories, return_index=True)
    new_categories = unique_new_categories
    unique_codes = unique_codes[unique_indices]

    # Create a mapping from old codes to new codes
    code_map = {old_code: new_code for new_code, old_code in enumerate(unique_codes)}

    # Map old codes to new codes
    new_codes = np.array([code_map.get(code, -1) for code in codes], dtype=codes.dtype)

    with write_lock:
        with h5py.File(dest_file_path, 'a') as f_dest:
            dest_group = f_dest.require_group(source_group.name)

            # Create datasets for new categories and codes
            categories_dset = dest_group.create_dataset(
                'categories',
                data=new_categories,
                dtype=new_categories.dtype,
                compression=source_group['categories'].compression
            )
            codes_dset = dest_group.create_dataset(
                'codes',
                data=new_codes,
                dtype=new_codes.dtype,
                compression=source_group['codes'].compression
            )

            # Copy attributes from the source to the destination datasets
            copy_attrs(source_group['categories'], categories_dset)
            copy_attrs(source_group['codes'], codes_dset)
            copy_attrs(source_group, dest_group)


def write_process_raw_group(
        source_group: h5py.Group,
        dest_file_path: str,
        row_indices: np.ndarray,
        batch_size: int
) -> None:
    """
    Processes and writes the 'raw' group to the destination HDF5 file with specified slicing.

    Args:
        source_group (h5py.Group): The source group to process.
        dest_file_path (str): The path to the destination HDF5 file.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        batch_size (int): The size of the batch for processing large datasets.
    """
    if 'X' in source_group.name:
        # Determine if the encoding type is CSR or CSC matrix
        parent_encoding_type = source_group.attrs.get('encoding-type', None)
        is_csr = parent_encoding_type != "csc_matrix"

        # Process the matrix with appropriate CSR/CSC flag
        write_process_matrix(
            source_group,
            dest_file_path,
            row_indices,
            np.arange(source_group.attrs['shape'][1]),
            batch_size,
            is_csr
        )

    if 'var' in source_group.name:
        for var_key in source_group.keys():
            with write_lock:
                with h5py.File(dest_file_path, 'a') as f_dest:
                    dest_group = f_dest.require_group(source_group.name)
                    # Copy var_key to the destination group if not already present
                    if var_key not in dest_group:
                        source_group.copy(var_key, dest_group)

    if 'varm' in source_group.name:
        for varm_key in source_group.keys():
            with write_lock:
                with h5py.File(dest_file_path, 'a') as f_dest:
                    dest_group = f_dest.require_group(source_group.name)
                    # Copy varm_key to the destination group if not already present
                    if varm_key not in dest_group:
                        source_group.copy(varm_key, dest_group)


def write_process_obsp_group(
        source_group: h5py.Group,
        dest_file_path: str,
        row_indices: np.ndarray,
        batch_size: int
) -> None:
    """
    Processes and writes 'obsp' group to the destination HDF5 file with specified slicing.

    Args:
        source_group (h5py.Group): The source group to process.
        dest_file_path (str): The path to the destination HDF5 file.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        batch_size (int): The size of the batch for processing large datasets.
    """
    for key in source_group.keys():
        item = source_group[key]

        if isinstance(item, h5py.Group):
            # Determine if the encoding type is CSR or CSC matrix
            parent_encoding_type = item.attrs.get('encoding-type', None)
            is_csr = parent_encoding_type != "csc_matrix"
            # Process the matrix with appropriate CSR/CSC flag
            write_process_matrix(item, dest_file_path, row_indices, row_indices, batch_size, is_csr)
        elif isinstance(item, h5py.Dataset):
            # Slice the dataset according to the row indices
            data = item[row_indices, :][:, row_indices]
            with write_lock:
                with h5py.File(dest_file_path, 'a') as f_dest:
                    # Ensure the destination group exists and create the dataset
                    dest_group = f_dest.require_group(source_group.name)
                    dset = dest_group.create_dataset(key, data=data, compression=item.compression)
                    # Copy attributes from the source to the destination dataset
                    copy_attrs(item, dset, shape=data.shape)


def write_process_varp_group(
        source_group: h5py.Group,
        dest_file_path: str,
        col_indices: np.ndarray,
        batch_size: int
) -> None:
    """
    Processes and writes 'varp' group to the destination HDF5 file with specified slicing.

    Args:
        source_group (h5py.Group): The source group to process.
        dest_file_path (str): The path to the destination HDF5 file.
        col_indices (np.ndarray): The indices of the columns to include in the slice.
        batch_size (int): The size of the batch for processing large datasets.
    """
    for key in source_group.keys():
        item = source_group[key]

        if isinstance(item, h5py.Group):
            # Determine if the encoding type is CSR or CSC matrix
            parent_encoding_type = item.attrs.get('encoding-type', None)
            is_csr = parent_encoding_type != "csc_matrix"
            # Process the matrix with appropriate CSR/CSC flag
            write_process_matrix(item, dest_file_path, col_indices, col_indices, batch_size, is_csr)
        elif isinstance(item, h5py.Dataset):
            # Slice the dataset according to the column indices
            data = item[col_indices, :][:, col_indices]
            with write_lock:
                with h5py.File(dest_file_path, 'a') as f_dest:
                    # Ensure the destination group exists and create the dataset
                    dest_group = f_dest.require_group(source_group.name)
                    dset = dest_group.create_dataset(key, data=data, compression=item.compression)
                    # Copy attributes from the source to the destination dataset
                    copy_attrs(item, dset, shape=data.shape)


def write_process_dataset(
        dataset: h5py.Dataset,
        dest_file_path: str,
        group_path: str,
        row_indices: np.ndarray,
        col_indices: np.ndarray,
        parent_encoding_type: str | None = None,
        parent_group_name: str | None = None
) -> None:
    """
    Processes and writes a dataset to the destination HDF5 file with specified slicing.

    Args:
        dataset (h5py.Dataset): The dataset to process.
        dest_file_path (str): The path to the destination HDF5 file.
        group_path (str): The path within the destination file where the dataset will be written.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        col_indices (np.ndarray): The indices of the columns to include in the slice.
        parent_encoding_type (str, optional): The encoding type of the parent group.
            Default is None.
        parent_group_name (str, optional): The name of the parent group. Default is None.
    """
    compression = dataset.compression if dataset.compression else None
    data = None

    # Skip processing if parent encoding type is a sparse matrix
    if parent_encoding_type in ['csr_matrix', 'csc_matrix']:
        return

    # Process 1D datasets
    if dataset.ndim == 1:
        if parent_group_name is not None and 'obs' in parent_group_name:
            valid_row_indices = row_indices[row_indices < dataset.shape[0]]
            data = dataset[valid_row_indices]
        elif parent_group_name is not None and 'var' in parent_group_name:
            valid_col_indices = col_indices[col_indices < dataset.shape[0]]
            data = dataset[valid_col_indices]
        else:
            data = dataset[:]
    # Process 2D datasets
    elif dataset.ndim == 2:
        if parent_group_name is not None:
            if 'layers' in parent_group_name:
                data = np.empty((len(row_indices), len(col_indices)), dtype=dataset.dtype)
                for i, row in enumerate(row_indices):
                    data[i, :] = dataset[row, col_indices]
            elif 'obsm' in parent_group_name:
                data = np.empty((len(row_indices), dataset.shape[1]), dtype=dataset.dtype)
                for i, row in enumerate(row_indices):
                    data[i, :] = dataset[row, :]
            elif 'varm' in parent_group_name:
                data = np.empty((len(col_indices), dataset.shape[1]), dtype=dataset.dtype)
                for i, col in enumerate(col_indices):
                    data[i, :] = dataset[col, :]

    # Write the processed data to the destination file
    if data is not None:
        with write_lock:
            with h5py.File(dest_file_path, 'a') as f_dest:
                dest_group = f_dest.require_group(group_path)
                dset = dest_group.create_dataset(
                    dataset.name.split('/')[-1],
                    data=data,
                    compression=compression
                )
                copy_attrs(dataset, dset)


def write_process_group(
        source_group: h5py.Group,
        dest_file_path: str,
        row_indices: np.ndarray,
        col_indices: np.ndarray,
        batch_size: int = 1000
) -> None:
    """
    Processes and writes a group to the destination HDF5 file, handling different
    encoding types.

    Args:
        source_group (h5py.Group): The source group to process.
        dest_file_path (str): The path to the destination HDF5 file.
        row_indices (np.ndarray): The indices of the rows to include in the slice.
        col_indices (np.ndarray): The indices of the columns to include in the slice.
        batch_size (int, optional): The size of the batch for processing large datasets.
            Default is 1000.
    """
    parent_encoding_type = source_group.attrs.get('encoding-type', None)

    # Process according to the parent encoding type
    if parent_encoding_type == 'csr_matrix':
        write_process_matrix(
            source_group,
            dest_file_path,
            row_indices,
            col_indices,
            batch_size,
            is_csr=True
        )
    elif parent_encoding_type == 'csc_matrix':
        write_process_matrix(
            source_group,
            dest_file_path,
            row_indices,
            col_indices,
            batch_size,
            is_csr=False
        )
    elif parent_encoding_type == 'categorical':
        write_process_categorical_group(source_group, dest_file_path, row_indices, col_indices)
    elif 'obsp' in source_group.name:
        write_process_obsp_group(source_group, dest_file_path, row_indices, batch_size)
    elif 'varp' in source_group.name:
        write_process_varp_group(source_group, dest_file_path, col_indices, batch_size)
    else:
        # Iterate through items in the source group
        for key in source_group.keys():
            item = source_group[key]

            if isinstance(item, h5py.Dataset):
                write_process_dataset(
                    item,
                    dest_file_path,
                    source_group.name,
                    row_indices,
                    col_indices,
                    parent_encoding_type,
                    source_group.name
                )
            elif isinstance(item, h5py.Group):
                if source_group.name == '/raw':
                    write_process_raw_group(item, dest_file_path, row_indices, batch_size)
                else:
                    write_process_group(item, dest_file_path, row_indices, col_indices, batch_size)


def write_slice_h5ad(
        source_file_path: str,
        dest_file_path: str,
        rows: slice,
        cols: slice,
        memory_fraction: float = 0.1
) -> None:
    """
    Writes a sliced version of an h5ad file to a new destination file.

    :param source_file_path: The path to the source h5ad file.
    :param dest_file_path: The path to the destination h5ad file.
    :param rows: The slice object defining the row indices to include.
    :param cols: The slice object defining the column indices to include.
    :param memory_fraction: The fraction of available memory to use for processing.
            Default is 0.1 (10%).

    :raise ValueError: If no rows or columns are selected for slicing.
    """
    with h5py.File(source_file_path, 'r') as f_src:
        # Create destination file, truncating if it already exists
        h5py.File(dest_file_path, 'w')

        # Retrieve the number of rows and columns in the source file
        num_rows = f_src['obs'][f_src['obs'].attrs['_index']].shape[0]
        num_cols = f_src['var'][f_src['var'].attrs['_index']].shape[0]

        # Generate row and column indices based on the provided slices
        row_indices = np.arange(
            rows.start or 0,
            rows.stop if rows.stop is not None else num_rows,
            rows.step or 1
        )
        col_indices = np.arange(
            cols.start or 0,
            cols.stop if cols.stop is not None else num_cols,
            cols.step or 1
        )

        # Ensure indices do not exceed the available range
        row_indices = row_indices[row_indices < num_rows]
        col_indices = col_indices[col_indices < num_cols]

        # Convert indices to 64-bit integers
        row_indices = row_indices.astype(np.int64)
        col_indices = col_indices.astype(np.int64)

        # Raise an error if no valid rows or columns are selected
        if len(row_indices) == 0 or len(col_indices) == 0:
            raise ValueError("No rows or columns to slice")

        # Determine the data type size and calculate the appropriate batch size
        # pylint: disable=no-member
        dtype_size = f_src['X/data'].dtype.itemsize
        batch_size = calculate_batch_size(memory_fraction, len(col_indices), dtype_size)

        # Iterate over items in the source file
        for key, item in f_src.items():

            if isinstance(item, h5py.Group):
                if key == 'uns':
                    # Copy 'uns' group to the destination file
                    with write_lock:
                        with h5py.File(dest_file_path, 'a') as f_dest:
                            f_src.copy(key, f_dest)
                else:
                    # Create the group in the destination file and copy attributes
                    with write_lock:
                        with h5py.File(dest_file_path, 'a') as f_dest:
                            dest_group = f_dest.require_group(key)
                            copy_attrs(item, dest_group)
                    # Process the group for writing sliced data
                    write_process_group(item, dest_file_path, row_indices, col_indices, batch_size)
            elif isinstance(item, h5py.Dataset):
                # Process the dataset for writing sliced data
                write_process_dataset(item, dest_file_path, key, row_indices, col_indices)
