"""
This module provides functionalities to perform Incremental Principal Component Analysis (IPCA)
on datasets stored in HDF5 files. It includes capabilities to handle both dense arrays 
and CSR and CSC sparse matrix formats efficiently, within the constraints of 
the HDF5 file structure.

Features:
- Perform IPCA incrementally to manage memory usage effectively,
    which is suitable for large datasets.
- Store results in a structured manner within HDF5 files,
    organizing results into the groups 'obsm', 'varm', and 'uns'.
- Check and manage existing datasets with options to overwrite,
    ensuring data integrity and flexibility in data handling.
- Support numeric datasets stored as h5py.Datasets or within h5py.Groups,
    accounting for diverse data storage practices.
- Provide detailed warnings and handle exceptions related to data types
    and structure to ensure robust data processing.

The module is designed to be flexible and efficient, allowing users to specify the 
number of components, batch size, and other parameters, making it suitable for 
a variety of IPCA-related tasks.

Dependencies:
    - h5py: For handling HDF5 files.
    - numpy: For numerical operations.
    - scipy.sparse: For handling CSR/CSC matrices.
    - sklearn.decomposition.IncrementalPCA: For performing the Incremental PCA.
    - eighta_lib.slicing: For efficient data slicing in sparse formats.
"""

import warnings
from typing import Union
import h5py
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.decomposition import IncrementalPCA
from eighta_lib.slicing.slicing_to_memory import read_process_csc_matrix


# pylint: disable=too-many-arguments
def incremental_pca_h5ad(
    file_path: str,
    path_to_item: str,
    n_components: int,
    batch_size: int,
    store_key: str | None = None,
    overwrite: bool = False
) -> None:
    """
    Performs Incremental Principal Component Analysis (IPCA) on a dataset, stored as either
    a h5py.Group or a h5py.Dataset in an HDF5 file. This function manages the 
    creation of necessary groups and datasets within the HDF5 file structure, organizes 
    the IPCA results under specified keys derived from ``store_key``, and handles existing 
    datasets under the same ``store_key`` based on the ``overwrite`` parameter.

    Note:
        This method's functionality:
        - Only supports h5py.Datasets encoded as arrays and 
            h5py.Groups encoded as CSR or CSC matrices.
        - Only allows matrices within the groups 'X', 'layers', 'obsm', and 'varm'. 
        - Ensures that the 'obsm', 'varm', and 'uns' groups are created if they do not exist.
        - Organizes the IPCA results into different groups within the HDF5 file:
            - Creates and populates a dataset in 'obsm' for the IPCA transformed data: 
                ``ipca_{store_key}``
            - Creates and populates a dataset in 'varm' for the IPCA components: 
                ``ipca_components_{store_key}``
            - Creates and populates datasets in 'uns' for explained variance and 
                variance ratios: ``ipca_explained_variance_{store_key}`` and 
                ``ipca_explained_variance_ratio_{store_key}``
        - Checks for existing (previously created) IPCA datasets corresponding to 
            the ``store_key``, before proceeding with dataset creation 
            or overwriting based on the ``overwrite`` parameter.
        - Operates only on datasets of numeric data types.

    :param file_path: Path to the HDF5 file containing the dataset.
    :type file_path: str
    :param path_to_item: Path within the HDF5 file to the dataset to have IPCA be performed on.
    :type path_to_item: str
    :param n_components: The number of principal components to retain in the IPCA.
    :type n_components: int
    :param batch_size: The size of each batch for fitting and transforming the IPCA.
    :type batch_size: int
    :param store_key: A key used to uniquely create and identify IPCA datasets within the file. 
        If not provided, a default key based on ``path_to_item`` will be used 
        (``store_key`` will be replaced with ``path_to_item``). 
    :type store_key: str, optional
    :param overwrite: Flag to control the behavior when IPCA dataset(s) with the same ``store_key`` 
        already exist. If False, raises an error to prevent data loss. If True, 
        existing datasets are overwritten.
    :type overwrite: bool

    :returns: None. The function modifies the file specified by ``file_path``, storing IPCA 
        components, the explained variances, the explained variance ratios, and transformed data. 
              
    :raises ValueError: 
        - If the specified ``path_to_item`` does not exist
        - If the item represented by ``path_to_item`` is not within 
            the groups 'X', 'layers', 'obsm', or 'varm'
        - If the item is not a h5py.Dataset encoded as an array 
            or a h5py.Group encoded in CSR or CSC format
        - Or if the item's data type is not numeric
    :raises ValueError: If `overwrite` is False and datasets with the specified ``store_key`` 
        already exist in the file, indicating a risk of unintentional data overwriting.
    """
    with h5py.File(file_path, 'r+') as f:
        # Use the helper function to validate and retrieve the item
        item, encoding_type, shape = verify_and_get_item(f, path_to_item)

        if batch_size <= 0:
            raise ValueError("Batch size must be larger than 0.")
        if n_components <= 0:
            raise ValueError("Number of components must be larger than 0.")

        if batch_size < n_components:
            raise ValueError(
                "Batch size must be greater than or equal to the "
                "number of components."
            )

        # Check if the number of samples in the last batch is less than the number of components
        if (shape[0] % batch_size) < n_components and (shape[0] % batch_size) != 0:
            raise ValueError(
                "The number of samples in the last batch must be greater than "
                "or equal to the number of components."
                "This condition is violated when the remainder of the "
                "total number of rows divided by the batch size "
                "(number of rows % batch size) is less than the number of components and not zero."
            )

        # Initialize the name_suffix identifier, that will be used to store the IPCA data
        if store_key is None:
            # Naming convention correction for consistency
            name_suffix = path_to_item.strip('/')
        else:
            name_suffix = store_key

        if encoding_type == "array":
            perform_incremental_pca_array(f, item, shape, batch_size,
                                          n_components, name_suffix, overwrite)
        elif encoding_type == "csr_matrix":
            perform_incremental_pca_csr_matrix(f, item, shape, batch_size,
                                               n_components, name_suffix, overwrite)
        elif encoding_type == "csc_matrix":
            perform_incremental_pca_csc_matrix(f, item, shape, batch_size,
                                               n_components, name_suffix, overwrite)

# pylint: disable=too-many-arguments
def perform_incremental_pca_csc_matrix(
    f: h5py.File,
    item_group: h5py.Group,
    shape: tuple,
    batch_size: int,
    n_components: int,
    name_suffix: str,
    overwrite: bool
) -> None:
    """
    Helper method that performs Incremental Principal Component Analysis (IPCA) on a dataset stored 
    as a CSC matrix in an HDF5 file. The IPCA is fitted in batches, and results including 
    transformed data, eigenvectors, explained variances, and explained variance ratios 
    are stored back into the file. Datasets are managed and created using the 
    `prepare_and_create_datasets()` function.
    
    Note:
        - **UserWarning**: This method warns about potential performance issues with the 
            CSC format due to its inefficient row access. Due to the columnar nature of 
            CSC matrices, this method may exhibit slower performance when accessing 
            data row-wise, which is necessary for IPCA.
        If performance is significantly impacted, consider reducing the number of
            components, adjusting the batch size, or converting the matrix to CSR 
            or dense array format.

    :param f: An open HDF5 file with write access.
    :type f: h5py.File
    :param item_group: The HDF5 group, containing the CSC matrix components, 
        to be processed, retrieved from the HDF5 file.
    :type item_group: h5py.Group
    :param shape: The shape of the dataset, used to determine batch processing.
    :type shape: tuple
    :param batch_size: The size of each batch for fitting and transforming the IPCA.
    :type batch_size: int
    :param n_components: The number of principal components to retain.
    :type n_components: int
    :param name_suffix: A suffix appended to the names of IPCA datasets to uniquely 
        identify them within the file.
    :type name_suffix: str
    :param overwrite: Flag to control the behavior when datasets with the same name_suffix 
        already exist. If False, an error is raised to prevent data loss. 
        If True, existing datasets are overwritten.
    :type overwrite: bool

    :returns: None. The function modifies the file specified by ``f``, storing IPCA 
        components, the explained variances, the explained variance ratios, and transformed data.      
    """
    # Warning about the potential performance issue
    warnings.warn("Due to the columnar nature of the CSC format, IPCA might "
          "take longer because it requires row access. If it takes too long, "
          "consider trying a different number of components, batch size, "
          "or convert the matrix to CSR or dense array format.", UserWarning)

    # Create an instance of IncrementalPCA
    ipca = IncrementalPCA(n_components=n_components, batch_size=batch_size)

    # Process the dataset in batches for fitting
    for i in range(0, shape[0], batch_size):
        start_row = i
        end_row = min(i + batch_size, shape[0])  # Avoid going out of bounds

        row_indices = np.arange(start_row, end_row)
        col_indices = np.arange(item_group.attrs["shape"][1])

        # Fetch the matrix slice for current batch of rows
        batch_data = read_process_csc_matrix(item_group, row_indices, col_indices)
        ipca.fit(batch_data)

    prepare_and_create_datasets(f, shape, ipca, n_components, name_suffix, overwrite)

    obsm_group = f.require_group('obsm')

    # Process the dataset in batches for transformation
    for i in range(0, shape[0], batch_size):
        start_row = i
        end_row = min(i + batch_size, shape[0])  # Avoid going out of bounds

        row_indices = np.arange(start_row, end_row)
        col_indices = np.arange(item_group.attrs["shape"][1])

        # Fetch the entire matrix slice for current batch of rows for transformation
        batch_data = read_process_csc_matrix(item_group, row_indices,col_indices)
        obsm_group[f'ipca_{name_suffix}'][i:i + end_row - start_row] = ipca.transform(batch_data)


# pylint: disable=too-many-arguments, too-many-locals
def perform_incremental_pca_csr_matrix(
    f: h5py.File,
    item_group: h5py.Group,
    shape: tuple,
    batch_size: int,
    n_components: int,
    name_suffix: str,
    overwrite: bool
) -> None:
    """
    Helper method that performs Incremental Principal Component Analysis (IPCA) on a dataset stored 
    as a CSR matrix in an HDF5 file. The IPCA is fitted in batches, and results including 
    transformed data, eigenvectors, explained variances, and explained variance ratios 
    are stored back into the file. Datasets are managed and created using the 
    `prepare_and_create_datasets()` function.
    
    :param f: An open HDF5 file with write access.
    :type f: h5py.File
    :param item_group: The HDF5 group, containing the CSR matrix components, to be processed, 
        retrieved from the HDF5 file.
    :type item_group: h5py.Group
    :param shape: The shape of the dataset, used to determine batch processing.
    :type shape: tuple
    :param batch_size: The size of each batch for fitting and transforming the IPCA.
    :type batch_size: int
    :param n_components: The number of principal components to retain.
    :type n_components: int
    :param name_suffix: A suffix appended to the names of IPCA datasets to uniquely 
        identify them within the file.
    :type name_suffix: str
    :param overwrite: Flag to control the behavior when datasets with the same name_suffix 
        already exist. If False, an error is raised to prevent data loss. 
        If True, existing datasets are overwritten.
    :type overwrite: bool

    :returns: None. The function modifies the file specified by ``f``, storing IPCA 
        components, the explained variances, the explained variance ratios, and transformed data.
    """
    # item_group corresponds to the HDF5 group containing the csr_matrix components
    data = item_group['data']
    indices = item_group['indices']
    indptr = item_group['indptr']

    # Create an instance of IncrementalPCA
    ipca = IncrementalPCA(n_components=n_components, batch_size=batch_size)

    # Process the dataset in batches for fitting
    for i in range(0, shape[0], batch_size):
        start_row = i
        end_row = min(i + batch_size, shape[0])  # Avoid going out of bounds

        # Extract the relevant slice of the csr_matrix
        batch_data = csr_matrix((data[indptr[start_row]:indptr[end_row]],
                                 indices[indptr[start_row]:indptr[end_row]],
                                 indptr[start_row:end_row + 1] - indptr[start_row]),
                                shape=(end_row - start_row, shape[1]))
        ipca.fit(batch_data)

    prepare_and_create_datasets(f, shape, ipca, n_components, name_suffix, overwrite)

    obsm_group = f.require_group('obsm')

    #  Process the dataset in batches for transformation
    for i in range(0, shape[0], batch_size):
        start_row = i
        end_row = min(i + batch_size, shape[0])  # Avoid going out of bounds

        # Extract the relevant slice of the csr_matrix
        batch_data = csr_matrix((data[indptr[start_row]:indptr[end_row]],
                                 indices[indptr[start_row]:indptr[end_row]],
                                 indptr[start_row:end_row + 1] - indptr[start_row]),
                                shape=(end_row - start_row, shape[1]))

        obsm_group[f'ipca_{name_suffix}'][i:i + end_row - start_row] = ipca.transform(batch_data)


def perform_incremental_pca_array(
    f: h5py.File,
    item_dataset: h5py.Dataset,
    shape: tuple,
    batch_size: int,
    n_components: int,
    name_suffix: str,
    overwrite: bool
) -> None:
    """
    Helper method that performs Incremental Principal Component Analysis (IPCA) on a dataset stored 
    as an array in an HDF5 file. The IPCA is fitted in batches, and results including 
    transformed data, eigenvectors, explained variances, and explained variance ratios 
    are stored back into the file. Datasets are managed and created using the 
    `prepare_and_create_datasets()` function.

    :param f: An open HDF5 file with write access.
    :type f: h5py.File
    :param item_dataset: The array dataset to be processed, retrieved from the HDF5 file.
    :type item_dataset: h5py.Dataset
    :param shape: The shape of the array dataset, used to determine batch processing.
    :type shape: tuple
    :param batch_size: The size of each batch for fitting and transforming the IPCA.
    :type batch_size: int
    :param n_components: The number of principal components to retain.
    :type n_components: int
    :param name_suffix: A suffix appended to the names of IPCA datasets to uniquely 
        identify them within the file.
    :type name_suffix: str
    :param overwrite: Flag to control the behavior when datasets with the same name_suffix 
        already exist. If False, an error is raised to prevent data loss. 
        If True, existing datasets are overwritten.
    :type overwrite: bool

    :returns: None. The function modifies the file specified by ``f``, storing IPCA 
        components, the explained variances, the explained variance ratios, and transformed data.
    """

    # Create an instance of IncrementalPCA
    ipca = IncrementalPCA(n_components=n_components, batch_size=batch_size)

    # Process the dataset in batches
    for i in range(0, shape[0], batch_size):
        batch_data = item_dataset[i:i + batch_size]
        ipca.fit(batch_data) # Update IPCA with this batch

    prepare_and_create_datasets(f, shape, ipca, n_components, name_suffix, overwrite)

    obsm_group = f.require_group('obsm')

    # Process the dataset in batches for transformation
    for i in range(0, shape[0], batch_size):
        batch_data = item_dataset[i:i + batch_size]
        transformed_data = ipca.transform(batch_data)  # Transform the current batch
        # Store the transformed data
        obsm_group[f'ipca_{name_suffix}'][i:i + batch_size] = transformed_data


def prepare_and_create_datasets(
    f: h5py.File,
    shape: tuple,
    ipca: IncrementalPCA,
    n_components: int,
    name_suffix: str,
    overwrite: bool
) -> None:
    """
    Prepares and manages datasets within an HDF5 file for storing the results of 
    Incremental PCA (IPCA).

    This function handles the creation of necessary groups and datasets within 
    the HDF5 file structure, manages overwrite behaviors, and organizes the IPCA results 
    under specified keys derived from `name_suffix`. It ensures necessary groups 
    (`obsm`, `varm`, `uns`) are created if they do not exist, and it handles
    existing datasets based on the `overwrite` parameter.

    Note:
        - The method organizes the PCA results into different groups within the HDF5 file:
            - Creates a dataset in 'obsm' for the IPCA transformed data: ``ipca_{name_suffix}``
            - Creates and populates a dataset in 'varm' for the IPCA components: 
                ``ipca_components_{name_suffix}``
            - Creates and populates datasets in 'uns' for explained variance and variance ratios:
                ``ipca_explained_variance_{name_suffix}`` and 
                ``ipca_explained_variance_ratio_{name_suffix}``
        - The method checks for existing datasets corresponding to the 
            ``name_suffix`` before proceeding with dataset creation or overwriting,
            based on the ``overwrite`` parameter.

    :param f: An open HDF5 file with write access.
    :type f: h5py.File
    :param shape: The shape of the item from the HDF5 file on which IPCA was performed,
                        used for determining the shape of the output datasets.
    :type shape: tuple
    :param ipca: The fitted IncrementalPCA object from which IPCA results such 
        as explained variance, components, and ratio are retrieved.
    :type ipca: IncrementalPCA
    :param n_components: The number of principal components retained in the IPCA.
    :type n_components: int
    :param name_suffix: A suffix appended to the names of IPCA datasets to 
        uniquely identify them within the file.
    :type name_suffix: str
    :param overwrite: Flag to control the behavior when datasets with the same 
        `name_suffix` already exist. If False, an error is raised to prevent data loss. 
        If True, existing datasets are overwritten.
    :type overwrite: bool
    
    :returns: None. The function modifies the file specified by ``f``, creating datasets for IPCA 
        components, the explained variances, the explained variance ratios, and transformed data.
              
    :raises ValueError: If `overwrite` is False and datasets with the specified `name_suffix` 
        already exist in the file, indicating a risk of unintentional data overwriting.
    """

    # Prepare groups within the HDF5 file
    # 'require_group' checks if the specified group exists; if not, it creates it.
    obsm_group = f.require_group('obsm')
    varm_group = f.require_group('varm')
    uns_group = f.require_group('uns')

    # If `overwrite` is set to False, check if datasets exist and raise an error if they do.
    if not overwrite:
        if f'ipca_{name_suffix}' in obsm_group or \
        f'ipca_explained_variance_{name_suffix}' in uns_group or \
        f'ipca_explained_variance_ratio_{name_suffix}' in uns_group or \
        f'ipca_components_{name_suffix}' in varm_group:
            raise ValueError(
                f"Data under the key '{name_suffix}' already exists and "
                "cannot be overwritten."
            )

    # If `overwrite` is set to True, delete existing datasets under the `name_suffix` identifier.
    else:
        if f'ipca_{name_suffix}' in obsm_group:
            del obsm_group[f'ipca_{name_suffix}']
        if f'ipca_explained_variance_{name_suffix}' in uns_group:
            del uns_group[f'ipca_explained_variance_{name_suffix}']
        if f'ipca_explained_variance_ratio_{name_suffix}' in uns_group:
            del uns_group[f'ipca_explained_variance_ratio_{name_suffix}']
        if f'ipca_components_{name_suffix}' in varm_group:
            del varm_group[f'ipca_components_{name_suffix}']

    # Create datasets to store incremental transformations
    dataset = obsm_group.create_dataset(
        f'ipca_{name_suffix}',
        shape=(shape[0], n_components),
        dtype='float32'
    )
    dataset.attrs['encoding-type'] = 'array'
    dataset.attrs['encoding-version'] = '0.2.0'

    dataset = uns_group.create_dataset(
        f'ipca_explained_variance_{name_suffix}',
        data=ipca.explained_variance_
    )
    dataset.attrs['encoding-type'] = 'array'
    dataset.attrs['encoding-version'] = '0.2.0'

    dataset = uns_group.create_dataset(
        f'ipca_explained_variance_ratio_{name_suffix}',
        data=ipca.explained_variance_ratio_
    )
    dataset.attrs['encoding-type'] = 'array'
    dataset.attrs['encoding-version'] = '0.2.0'

    dataset = varm_group.create_dataset(
        f'ipca_components_{name_suffix}',
        data=ipca.components_.T  # Transpose the components matrix
    )
    dataset.attrs['encoding-type'] = 'array'
    dataset.attrs['encoding-version'] = '0.2.0'


def verify_and_get_item(
    f: h5py.File,
    path_to_item: str
) -> tuple[Union[h5py.Dataset, h5py.Group], str, tuple]:
    """
    Helper method to verify the existence and type of an item within an HDF5 file, 
    and to return the item along with its encoding type and shape.

    This function checks if the specified path exists in the HDF5 file, validates that the
    item belongs to an allowed group, and ensures it is a recognized dataset or matrix format
    suitable for IPCA. It also confirms that the data type is numeric.

    Note:
        - The method only allows items within the groups 'X', 'layers', 'obsm', and 'varm'.
        - It supports datasets encoded as arrays and groups encoded as CSR or CSC matrices.

    :param f: An open HDF5 file with read access.
    :type f: h5py.File
    :param path_to_item: The path to the item within the HDF5 file.
    :type path_to_item: str

    :returns: A tuple containing the HDF5 item found at the specified path, 
        the encoding type of the item, and the shape of the item.
    :rtype: tuple[Union[h5py.Dataset, h5py.Group], str, tuple]

    :raises ValueError: If the specified path does not exist, 
        if the item is not within an allowed group,
        if the item is not an array dataset or recognized sparse matrix format,
        or if the item's data type is not numeric.
    """

    # Check if the item exists in the file
    if path_to_item not in f:
        raise ValueError(f"The specified path '{path_to_item}' does not exist in the HDF5 file.")

    valid_groups = ['X', 'layers', 'obsm', 'varm']
    # Extract the base group from path_to_item to validate it
    if path_to_item.split('/')[0] == "":
        base_group = path_to_item.split('/')[1]
    else:
        base_group = path_to_item.split('/')[0]

    # Check if the base group is one of the allowed groups
    if base_group not in valid_groups:
        raise ValueError(
            f"Path '{path_to_item}' must be within one of the following groups: "
            f"{', '.join(valid_groups)}."
        )

    item = f[path_to_item]

    # Check if the item is a dataset or a group that can represent a matrix
    # First, Checking for array matrix format
    if isinstance(item, h5py.Dataset) and item.attrs["encoding-type"] == "array":
        encoding_type = item.attrs["encoding-type"]
        data_type = item.dtype
        shape = item.shape

    # Checking for CSR or CSC matrix format
    elif (isinstance(item, h5py.Group) and
        item.attrs["encoding-type"] in ("csr_matrix", "csc_matrix") and
        "data" in item):
        encoding_type = item.attrs["encoding-type"]
        data_type = item['data'].dtype
        shape = item.attrs["shape"]

    else:
        raise ValueError(
            f"The item specified at '{path_to_item}' is neither a suitable dataset "
            f"nor a recognized sparse matrix format."
        )

    # Ensure the data type is numeric
    if not np.issubdtype(data_type, np.number):
        raise ValueError(
            f"The data at '{path_to_item}' is not numeric. "
            f"PCA requires numeric data types."
        )

    return item, encoding_type, shape
