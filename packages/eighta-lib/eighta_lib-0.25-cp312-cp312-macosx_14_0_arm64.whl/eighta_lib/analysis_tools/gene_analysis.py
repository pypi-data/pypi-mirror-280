"""
This module includes method related to gene analysis, including calculation of variance 
per gene and select top n genes.
"""
import h5py
import numpy as np
from tqdm import tqdm
from eighta_lib.file_management import update

def compute_var_csr(file_path: str) -> np.ndarray:
    """
    Helper method that calculates the variance of each column in the X component, 
    that is stored in CSR (Compressed Sparse Row) format, within an HDF5 file. 
    The function operates directly on the sparse matrix data from the HDF5 file, 
    using indices to calculate the variance without converting to a dense matrix form, 
    thus saving memory and processing time.

    :param file_path: The path to the HDF5 file containing the sparse matrix.
    :type file_path: str

    :returns: An array of variances for each column, calculated considering both the non-zero
              and the implicit zero entries of the sparse matrix.
    :rtype: numpy.ndarray
    """
    with h5py.File(file_path) as file:
        # pylint: disable=unpacking-non-sequence
        n_row, n_col = (
            file["X"].shape
            if isinstance(file["X"], h5py.Dataset)
            else file["X"].attrs["shape"]
        )
        variances = np.zeros(n_col)
        for i in tqdm(range(n_col)):
            col = file["X"]["data"][file["X"]["indices"][:] == i]
            mean = np.sum(col) / n_row
            col_sum = np.sum((col - mean) ** 2)
            col_sum += (n_row - len(col)) * mean**2
            variances[i] = col_sum / n_row
        return variances


def compute_var_csc(file_path: str) -> np.ndarray:
    """
    Helper method that calculates the variance of each column in the X component, 
    that is stored in CSC (Compressed Sparse Row) format, within an HDF5 file. The function 
    operates directly on the sparse matrix data from the HDF5 file, using indices to calculate 
    the variance without converting to a dense matrix form, thus saving memory and processing time.

    :param file_path: The path to the HDF5 file containing the sparse matrix.
    :type file_path: str

    :returns: An array of variances for each column, calculated considering both the non-zero
              and the implicit zero entries of the sparse matrix.
    :rtype: numpy.ndarray
    """
    with h5py.File(file_path) as file:
        # pylint: disable=unpacking-non-sequence
        n_row, n_col = (
            file["X"].shape
            if isinstance(file["X"], h5py.Dataset)
            else file["X"].attrs["shape"]
        )
        variances = np.zeros(n_col)
        for i in tqdm(range(1, n_col + 1)):
            col = file["X"]["data"][file["X"]["indptr"][i - 1] : file["X"]["indptr"][i]]
            mean = np.sum(col) / n_row
            col_sum = np.sum((col - mean) ** 2)
            col_sum += (n_row - len(col)) * mean**2
            variances[i - 1] = col_sum / n_row
        return variances


def compute_var_array(file_path: str) -> np.ndarray:
    """
        Helper method that calculates the variance of each column in the 'X' component, 
        which is stored as a (dense) array format within an HDF5 file. The function 
        processes the array data column by column from the HDF5 file.

        :param file_path: The path to the HDF5 file containing the dense array matrix.
        :type file_path: str

        :returns: An array of variances for each column, calculated by considering the actual values 
                in each column. This method computes the mean and the sum of the squared differences 
                from the mean for each column to derive the variance.
        :rtype: numpy.ndarray
    """
    with h5py.File(file_path) as file:
        # pylint: disable=unpacking-non-sequence
        n_row, n_col = (
            file["X"].shape
            if isinstance(file["X"], h5py.Dataset)
            else file["X"].attrs["shape"]
        )
        variances = np.zeros(n_col)
        for i in tqdm(range(n_col)):
            col = file["X"][:, i]
            mean = np.sum(col) / n_row
            col_sum = np.sum((col - mean) ** 2)
            variances[i] = col_sum / n_row
        return variances


def gene_variance(file_path: str, destination_key: str = "variance") -> np.ndarray:
    """
    Compute the variance of all genes in X and store in var.

    Note:
        The method supports X matrix in form of CSR matrix, CSC matrix 
        and array (dense matrix). The runtime will vary for different form of 
        X matrix. In specific, CSC < Dense <<<<< CSR.

    :param file_path: The path to the HDF5 file.
    :param destination_key: The key of the column where the variances
                        will be stored in var. Default is "variance".

    :return: An array of the computed variances
    :raise TypeError: If the encoding type of the X matrix is not one of
        CSR matrix, CSC matrix or array (dense matrix)
    """
    with h5py.File(file_path) as f:
        encoding_type = f["X"].attrs.get("encoding-type")
    if encoding_type == "csr_matrix":
        col_vars = compute_var_csr(file_path)
    elif encoding_type == "csc_matrix":
        col_vars = compute_var_csc(file_path)
    elif encoding_type == "array":
        col_vars = compute_var_array(file_path)
    else:
        raise TypeError(f"Encoding type of X {encoding_type} is not supported.")
    update.update_h5ad(file_path, f"var/{destination_key}", col_vars)
    return col_vars


def top_n_variance(
    file_path: str, n: int, variance_key_in_var: str | None = None
) -> np.ndarray:
    """
    Find the indexs of genes with the top n variance.

    :param file_path: The path to the HDF5 file.
    :param n: Number of genes to find.
    :param variance_key_in_var: The key of the column where the variances are stored in var.
        Default is None, meaning that the variances will be computed and stored in "var/variance".

    :return: An array of the indexs of genes with the top n variance.
    """
    if variance_key_in_var is None:
        variances = gene_variance(file_path)
    else:
        with h5py.File(file_path) as file:
            variances = file["var"][variance_key_in_var][:]
    return np.argpartition(variances, -n)[-n:]


def create_mask_top_n_variance(
    file_path: str,
    n: int,
    variance_key_in_var: str | None = None,
    destination_key: str = "var_mask",
):
    """
    Create a mask of X where only the columns repersenting the genes with top n variance
    is marked as true, and store it in layers.

    :param file_path: The path to the HDF5 file.
    :param n: Number of genes to find.
    :param variance_key_in_var: The key of the column where the variances are stored in var.
        Default is None, meaning that the variances will be computed and stored in "var/variance".
    :param destination_key: The key where the variances will be stored in layers.
        Default is "var_mask".
    """
    top_n_index = top_n_variance(file_path, n, variance_key_in_var)
    with h5py.File(file_path, mode='r+') as file:
        # pylint: disable=unpacking-non-sequence
        n_row, n_col = (
            file["X"].shape
            if isinstance(file["X"], h5py.Dataset)
            else file["X"].attrs["shape"]
        )
        mask = np.full(n_col, False)
        mask[top_n_index] = True

        layers_group = file.require_group('layers')
        if destination_key in layers_group:
            del layers_group[destination_key]
        dataset = layers_group.create_dataset(destination_key, shape=(n_row, n_col), dtype = 'bool')
        dataset.attrs['encoding-type'] = 'array'
        dataset.attrs['encoding-version'] = '0.2.0'
        for i in range(0, n_row):
            layers_group[destination_key][i] = mask
