"""
This module provides functions and utilities for exploring, processing, slicing,
and writing HDF5 files in memory, specifically targeting the AnnData format and its components.
"""
from typing import Union, Optional
import h5py
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import anndata as ad
import slicers_read

def read_slice_h5ad(
    file_path: str,
    rows: slice,
    cols: slice,
    include_raw: bool = False
) -> ad.AnnData:
    """
    Slice a .h5ad file based on specified rows and columns and return an AnnData object.

    :param file_path: The path to the .h5ad file to be sliced.
    :param rows: A slice object specifying the range of rows to include.
    :param cols: A slice object specifying the range of columns to include.
    :param include_raw: If True, include the 'raw' group in the sliced data.
            Default is False.

    :return: An AnnData object containing the sliced data.

    :raise MemoryError: If the slice size exceeds available memory when check_size is True.
    :raise ValueError: If no rows or columns are available to slice.
    """
    with h5py.File(file_path, 'r') as f:
        # Get the total number of rows and columns
        num_rows = f['obs'][f['obs'].attrs['_index']].shape[0]
        num_cols = f['var'][f['var'].attrs['_index']].shape[0]

        # Generate row and column indices based on the slice objects
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

        # Ensure indices are within bounds
        row_indices = row_indices[row_indices < num_rows]
        col_indices = col_indices[col_indices < num_cols]

        row_indices = row_indices.astype(np.int64)
        col_indices = col_indices.astype(np.int64)

        if len(row_indices) == 0 or len(col_indices) == 0:
            raise ValueError("No rows or columns to slice")

        sliced_data = {}
        for key, item in f.items():
            if item == 'raw' and not include_raw:
                continue
            if isinstance(item, h5py.Group):
                # Process h5py.Group items (X, layers, obs, ...)
                sliced_data[key] = read_process_group(item, row_indices, col_indices)
            elif isinstance(item, h5py.Dataset):
                # Process h5py.Dataset items (usually not the case, mostly for completeness)
                sliced_data[key] = read_process_dataset(item, row_indices, col_indices)

        # Extract data components from the sliced data
        x = sliced_data.pop('X')
        layers = sliced_data.pop('layers', {})
        obs = sliced_data.pop('obs')
        obsm = sliced_data.pop('obsm', {})
        obsp = sliced_data.pop('obsp', {})
        raw = sliced_data.pop('raw', {}) if include_raw else None
        uns = sliced_data.pop('uns', {})
        var = sliced_data.pop('var')
        varm = sliced_data.pop('varm', {})
        varp = sliced_data.pop('varp', {})

        # Create and return the AnnData object
        adata = ad.AnnData(
            X=x,
            layers=layers,
            obs=obs,
            obsm=obsm,
            obsp=obsp,
            raw=raw,
            uns=uns,
            var=var,
            varm=varm,
            varp=varp
        )

        return adata

def read_process_csr_matrix(
    source_group: h5py.Group,
    row_indices: np.ndarray,
    col_indices: np.ndarray
) -> csr_matrix:
    """
    Processes and slices a CSR (Compressed Sparse Row) matrix into memory.

    Args:
        source_group (h5py.Group): The source HDF5 group containing the CSR matrix.
        row_indices (array-like): The indices of the rows to slice.
        col_indices (array-like): The indices of the columns to slice.

    Returns:
        csr_matrix: A sliced CSR matrix.
    """
    data_list = []
    indices_list = []
    total_indptr = np.zeros(len(row_indices) + 1, dtype=source_group['indptr'].dtype)
    current_length = 0

    # Iterate through the specified row indices to slice the CSR matrix
    for i, row_idx in enumerate(row_indices):
        data_start_idx = source_group['indptr'][row_idx]
        data_end_idx = source_group['indptr'][row_idx + 1]

        if data_start_idx < data_end_idx:
            # Extract data and indices for the current row
            data = source_group['data'][data_start_idx:data_end_idx]
            indices = source_group['indices'][data_start_idx:data_end_idx]

            # Mask to select columns of interest
            mask = np.isin(indices, col_indices)
            if np.any(mask):
                data = data[mask]
                indices = indices[mask]

                # Map indices to new indices based on the selected columns
                index_map = {col: idx for idx, col in enumerate(col_indices)}
                indices = np.array([index_map[i] for i in indices])

                data_list.append(data)
                indices_list.append(indices)

                current_length += data.shape[0]
                total_indptr[i + 1] = current_length
            else:
                total_indptr[i + 1] = current_length
        else:
            total_indptr[i + 1] = current_length

    data_array = (
        np.concatenate(data_list)
        if data_list
        else np.array([], dtype=source_group['data'].dtype)
    )
    indices_array = (
        np.concatenate(indices_list)
        if indices_list
        else np.array([], dtype=source_group['indices'].dtype)
    )
    indptr_array = total_indptr

    return csr_matrix((
        data_array,
        indices_array,
        indptr_array),
        shape=(len(row_indices), len(col_indices))
    )


def read_process_csc_matrix(
    source_group: h5py.Group,
    row_indices: np.ndarray,
    col_indices: np.ndarray
) -> csc_matrix:
    """
    Processes and slices a CSC (Compressed Sparse Column) matrix into memory.

    Args:
        source_group (h5py.Group): The source HDF5 group containing the CSC matrix.
        row_indices (array-like): The indices of the rows to slice.
        col_indices (array-like): The indices of the columns to slice.

    Returns:
        csc_matrix: A sliced CSC matrix.
    """
    data_list = []
    indices_list = []
    total_indptr = np.zeros(len(col_indices) + 1, dtype=source_group['indptr'].dtype)
    current_length = 0

    # Iterate through the specified column indices to slice the CSC matrix
    for i, col_idx in enumerate(col_indices):
        data_start_idx = source_group['indptr'][col_idx]
        data_end_idx = source_group['indptr'][col_idx + 1]

        if data_start_idx < data_end_idx:
            # Extract data and indices for the current column
            data = source_group['data'][data_start_idx:data_end_idx]
            indices = source_group['indices'][data_start_idx:data_end_idx]

            # Mask to select rows of interest
            mask = np.isin(indices, row_indices)
            if np.any(mask):
                data = data[mask]
                indices = indices[mask]

                # Map indices to new indices based on the selected rows
                index_map = {row: idx for idx, row in enumerate(row_indices)}
                indices = np.array([index_map[i] for i in indices])

                data_list.append(data)
                indices_list.append(indices)

                current_length += data.shape[0]
                total_indptr[i + 1] = current_length
            else:
                total_indptr[i + 1] = current_length
        else:
            total_indptr[i + 1] = current_length

    data_array = (
        np.concatenate(data_list)
        if data_list
        else np.array([], dtype=source_group['data'].dtype)
    )
    indices_array = (
        np.concatenate(indices_list)
        if indices_list
        else np.array([], dtype=source_group['indices'].dtype)
    )
    indptr_array = total_indptr

    return csc_matrix((
        data_array,
        indices_array,
        indptr_array),
        shape=(len(row_indices), len(col_indices))
    )


def read_process_matrix(
    source_group: h5py.Group,
    row_indices: np.ndarray,
    col_indices: np.ndarray,
    is_csr: bool
) -> Union[csr_matrix, csc_matrix]:
    """
    Process and slice a matrix (CSR or CSC) into memory.

    Args:
        source_group (h5py.Group): The source HDF5 group containing the matrix.
        row_indices (array-like): The indices of the rows to slice.
        col_indices (array-like): The indices of the columns to slice.
        is_csr (bool): True if the matrix is CSR, False if CSC.

    Returns:
        csr_matrix or csc_matrix: The sliced matrix.
    """
    if is_csr:
        result = slicers_read.read_process_csr_matrix(
          source_group.file.filename,
          source_group.name,
          row_indices,
          col_indices
        )
        return csr_matrix(
          (result[0], result[1], result[2]),
          shape=(len(row_indices),
          len(col_indices)
          )
        )
        # return read_process_csr_matrix(source_group, row_indices, col_indices)
    result = slicers_read.read_process_csc_matrix(
      source_group.file.filename,
      source_group.name,
      row_indices,
      col_indices
    )
    return csc_matrix(
      (result[0], result[1], result[2]),
      shape=(len(row_indices),
      len(col_indices)
      )
    )
    # return read_process_csc_matrix(source_group, row_indices, col_indices)


def read_process_categorical_group(
    source_group: h5py.Group,
    row_indices: np.ndarray,
    col_indices: np.ndarray
) -> pd.Categorical:
    """
    Process an HDF5 group representing a categorical variable, slicing based on
    the specified row or column indices.

    Args:
        source_group (h5py.Group): The source HDF5 group to process.
        row_indices (array-like): The indices of the rows to slice.
        col_indices (array-like): The indices of the columns to slice.

    Returns:
        pandas.Categorical: A categorical representation of the sliced data.
    """
    # Retrieve the 'categories' dataset from the source group
    categories = source_group['categories'][:]

    # Decode byte strings to UTF-8 if necessary
    if isinstance(categories[0], bytes):
        categories = [cat.decode('utf-8') for cat in categories]

    # Determine whether to slice based on row or column indices
    if 'var' in source_group.name:
        codes = source_group['codes'][col_indices]
    elif 'obs' in source_group.name:
        codes = source_group['codes'][row_indices]
    else:
        raise ValueError("Source group name must contain 'var' or 'obs'")

    # Ensure unique codes are integers
    unique_codes = np.unique(codes).astype(int)

    # Generate new categories based on the unique codes
    new_categories = [categories[i] if i < len(categories) else "NaN" for i in unique_codes]

    # Ensure the new categories are unique
    unique_new_categories, unique_indices = np.unique(new_categories, return_index=True)

    # Create a mapping from old codes to new codes using unique indices
    code_map = {
        old_code: new_index
        for new_index, old_code in enumerate(unique_codes[unique_indices])
    }

    # Map the old codes to the new codes, falling back to "NaN" for unknown codes
    new_codes = np.array(
        [
            code_map.get(code, len(unique_new_categories) - 1)
            for code in codes
        ],
        dtype=codes.dtype
    )

    # Return a pandas Categorical from the new codes and unique new categories
    return pd.Categorical.from_codes(new_codes, unique_new_categories) # type: ignore


def read_process_dataframe_group(
    source_group: h5py.Group,
    indices: np.ndarray,
    is_obs: bool,
) -> pd.DataFrame:
    """
    Processes and slices a dataframe group from an HDF5 file, maintaining the column order.

    Args:
        source_group (h5py.Group): The source HDF5 group containing the dataframe.
        indices (array-like): The indices to slice.
        is_obs (bool): True if the dataframe belongs to 'obs', False if it belongs to 'var'.

    Returns:
        pd.DataFrame: The sliced dataframe with the specified indices.
    """
    sliced_data = {}

    # Retrieve the column-order attribute and convert it to a list
    column_order = source_group.attrs.get('column-order', [])
    if np.issubdtype(column_order.dtype, np.bytes_):
        column_order = [str(i, 'utf-8') for i in column_order]

    # Iterate over all keys in the source group
    for key in source_group.keys():
        if key == "_index":
            continue  # Skip the index key
        item = source_group[key]
        if isinstance(item, h5py.Dataset):
            # Process datasets by slicing based on indices
            sliced_data[key] = item[indices]
        elif isinstance(item, h5py.Group):
            # Recursively process sub-groups
            sliced_data[key] = read_process_group(item, indices, indices)

    # Get the original indices from the parent 'obs' or 'var' group
    if is_obs:
        original_indices = (
            source_group[source_group.attrs["_index"]][indices]
        )
    else:
        original_indices = (
            source_group[source_group.attrs["_index"]][indices]
        )

    # Create the sliced DataFrame
    sliced_df = pd.DataFrame(sliced_data, index=original_indices.astype(str))

    # Reorder the columns based on the original column order if it is not empty
    if len(column_order) != 0:
        sliced_df = sliced_df[column_order]

    # Preserve the column-order attribute in the DataFrame's metadata
    sliced_df.attrs['column-order'] = column_order

    return sliced_df


def read_process_raw_group(source_group: h5py.Group, row_indices: np.ndarray) -> dict:
    """
    Process an HDF5 group representing a 'raw' group, slicing based on the specified row indices.

    Args:
        source_group (h5py.Group): The source HDF5 group to process.
        row_indices (array-like): The indices of the rows to slice.

    Returns:
        dict: A dictionary containing the sliced data from the 'raw' group.
    """
    sliced_data = {}

    def copy_group(group):
        """
        Recursively copy an HDF5 group into a dictionary.

        Args:
            group (h5py.Group): The HDF5 group to copy.

        Returns:
            dict: A dictionary representation of the HDF5 group.
        """
        data = {}
        for key in group.keys():
            item = group[key]
            if isinstance(item, h5py.Group):
                # Recursively copy sub-groups
                data[key] = copy_group(item)
            elif isinstance(item, h5py.Dataset):
                # Copy datasets
                data[key] = item[()]
        return data

    # Process the 'X' dataset within the 'raw' group
    if 'X' in source_group:
        parent_encoding_type = source_group['X'].attrs.get('encoding-type', None)
        is_csr = parent_encoding_type != "csc_matrix"
        # Get all column indices for slicing
        col_indices = np.arange(source_group['X'].attrs['shape'][1])
        sliced_data['X'] = read_process_matrix(source_group['X'], row_indices, col_indices, is_csr)

    # Process the 'var' dataframe within the 'raw' group
    if 'var' in source_group:
        # Slice the 'var' dataframe (use all rows with slice(None) since we want to keep
        # the unsliced version)
        sliced_data['var'] = read_process_dataframe_group(
            source_group['var'],
            slice(None), # type: ignore
            is_obs=False,
        )

    # Process the 'varm' group within the 'raw' group
    if 'varm' in source_group:
        # Recursively copy the 'varm' group
        sliced_data['varm'] = copy_group(source_group['varm'])

    return sliced_data


def read_process_obsp_group(source_group: h5py.Group, row_indices: np.ndarray) -> dict:
    """
    Process an HDF5 group representing an 'obsp' group, slicing based on the specified row indices.

    Args:
        source_group (h5py.Group): The source HDF5 group to process.
        row_indices (array-like): The indices of the rows to slice.

    Returns:
        dict: A dictionary containing the sliced data from the 'obsp' group.
    """
    sliced_data = {}
    for key in source_group.keys():
        item = source_group[key]
        if isinstance(item, h5py.Group):
            # Determine if the matrix is CSR or CSC
            parent_encoding_type = item.attrs.get('encoding-type', None)
            is_csr = parent_encoding_type != "csc_matrix"
            sliced_data[key] = read_process_matrix(item, row_indices, row_indices, is_csr)
        elif isinstance(item, h5py.Dataset):
            # Slice the dataset across both dimensions using row indices
            data = item[row_indices, :][:, row_indices]
            sliced_data[key] = data

    return sliced_data


def read_process_varp_group(source_group: h5py.Group, col_indices: np.ndarray) -> dict:
    """
    Process an HDF5 group representing a 'varp' group, slicing based on the
    specified column indices.

    Args:
        source_group (h5py.Group): The source HDF5 group to process.
        col_indices (array-like): The indices of the columns to slice.

    Returns:
        dict: A dictionary containing the sliced data from the 'varp' group.
    """
    sliced_data = {}
    for key in source_group.keys():
        item = source_group[key]
        if isinstance(item, h5py.Group):
            # Determine if the matrix is CSR or CSC
            parent_encoding_type = item.attrs.get('encoding-type', None)
            is_csr = parent_encoding_type != "csc_matrix"
            sliced_data[key] = read_process_matrix(item, col_indices, col_indices, is_csr)
        elif isinstance(item, h5py.Dataset):
            # Slice the dataset across both dimensions using column indices
            data = item[col_indices, :][:, col_indices]
            sliced_data[key] = data

    return sliced_data


def read_process_group(
    source_group: h5py.Group,
    row_indices: np.ndarray,
    col_indices: np.ndarray
) -> dict | csc_matrix | csr_matrix | pd.Categorical | pd.DataFrame | ad.AnnData:
    """
    Process an HDF5 group based on the specified row and column indices.

    Args:
        source_group (h5py.Group): The source HDF5 group to process.
        row_indices (array-like): The indices of the rows to slice.
        col_indices (array-like): The indices of the columns to slice.

    Returns:
        dict: A dictionary containing the sliced data.
    """
    # Get the encoding type of the parent group
    parent_encoding_type = source_group.attrs.get('encoding-type', None)

    # Process based on the encoding type
    if parent_encoding_type == 'csr_matrix':
        # CSR group - X and Layers
        sliced_data = read_process_matrix(source_group, row_indices, col_indices, is_csr=True)
    elif parent_encoding_type == 'csc_matrix':
        # CSC group - X and Layers
        sliced_data = read_process_matrix(source_group, row_indices, col_indices, is_csr=False)
    elif parent_encoding_type == 'categorical':
        # Categorical group inside Obs, Var, and Raw/Var
        sliced_data = read_process_categorical_group(source_group, row_indices, col_indices)
    elif 'obsp' in source_group.name:
        sliced_data = read_process_obsp_group(source_group, row_indices)
    elif 'varp' in source_group.name:
        sliced_data = read_process_varp_group(source_group, col_indices)
    elif 'obs' in source_group.name and parent_encoding_type == 'dataframe':
        sliced_data = read_process_dataframe_group(source_group, row_indices, is_obs=True)
    elif 'var' in source_group.name and parent_encoding_type == 'dataframe':
        sliced_data = read_process_dataframe_group(source_group, col_indices, is_obs=False)
    elif parent_encoding_type == 'raw':
        sliced_data = read_process_raw_group(source_group, row_indices)
    else:
        # Process nested groups and datasets usually when dictionary is encountered
        sliced_data = {}
        for key in source_group.keys():
            item = source_group[key]

            if isinstance(item, h5py.Dataset):
                # Process dataset
                sliced_data[key] = read_process_dataset(
                    item,
                    row_indices,
                    col_indices,
                    parent_encoding_type,
                    source_group.name
                )
            elif isinstance(item, h5py.Group):
                # Recursively process sub-group
                sliced_data[key] = read_process_group(item, row_indices, col_indices)

    return sliced_data

def read_process_dataset(
    dataset: h5py.Dataset,
    row_indices: np.ndarray,
    col_indices: np.ndarray,
    parent_encoding_type: Optional[str] = None,
    parent_group_name: Optional[str] = None
) -> Optional[np.ndarray]:
    """
    Process an HDF5 dataset based on the specified row and column indices.

    Args:
        dataset (h5py.Dataset): The HDF5 dataset to process.
        row_indices (array-like): The indices of the rows to slice.
        col_indices (array-like): The indices of the columns to slice.
        parent_encoding_type (str, optional): The encoding type of the parent group.
            Default is None.
        parent_group_name (str, optional): The name of the parent group. Default is None.

    Returns:
        numpy.ndarray or None: The sliced data from the dataset or None if no processing is done.
    """
    data = None

    # Skip processing here as it will be handled by read_h5ad_process_matrix
    if parent_encoding_type in ['csr_matrix', 'csc_matrix']:
        return None

    # Scalar datasets
    if dataset.shape == ():
        data = (
            str(dataset[()], 'utf-8')
            if dataset.attrs['encoding-type'] == 'string'
            else dataset[()]
        )
    # 1-D datasets
    elif dataset.ndim == 1:
        data = (
            np.array([str(val, 'utf-8') for val in dataset[:]], dtype=object)
            if dataset.attrs['encoding-type'] == 'string-array'
            else dataset[:]
        )
    # 2-D datasets
    elif dataset.ndim == 2:
        if parent_group_name is None or parent_group_name == '/X':
            # Slice across both dimensions for X matrix
            data = dataset[row_indices, :][:, col_indices]
        elif 'layers' in parent_group_name:
            # Slice across both dimensions
            data = np.empty((len(row_indices), len(col_indices)), dtype=dataset.dtype)
            for i, row in enumerate(row_indices):
                data[i, :] = dataset[row, col_indices]
        elif 'obsm' in parent_group_name:
            # Slice across rows using row_indices
            data = np.empty((len(row_indices), dataset.shape[1]), dtype=dataset.dtype)
            for i, row in enumerate(row_indices):
                data[i, :] = dataset[row, :]
        elif 'varm' in parent_group_name:
            # Slice across rows using col_indices
            data = np.empty((len(col_indices), dataset.shape[1]), dtype=dataset.dtype)
            for i, col in enumerate(col_indices):
                data[i, :] = dataset[col, :]

    return data
