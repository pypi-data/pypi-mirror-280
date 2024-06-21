"""
This module includes util functions for developer.
"""
import h5py
import numpy as np

def explore_hdf5_file(file_path):
    """
    Recursively explores and prints the structure of an HDF5 file.

    Parameters:
        file_path (str): The path to the HDF5 file to explore.

    Outputs:
        This function prints the structure of the HDF5 file, including paths, dataset shapes, data
        types, compression (if applied) as well as the size of each dataset in gigabytes.
    """
    def explore_hdf5(item, path='/', indent=0):
        total_size_gb = 0
        indent_str = '    ' * indent

        if isinstance(item, h5py.Dataset):
            if '_index' in item.attrs:
                index_name = item.attrs['_index']
                print(f"{indent_str}{path} is a Dataset with index: {index_name}")
            else:
                dataset_size_gb = (np.prod(item.shape) * item.dtype.itemsize) / (1024 ** 3)
                total_size_gb += dataset_size_gb
                print(f"{indent_str}{path} is a Dataset with shape {item.shape}, "
                      f"dtype {item.dtype}, and size {dataset_size_gb:.4f} GB")

            # Add the compression information if available
            compression = item.compression if item.compression else "None"
            print(f"{indent_str}Compression: {compression}")

        elif isinstance(item, h5py.Group):
            index_info = ""
            if '_index' in item.attrs:
                index_name = item.attrs['_index']
                index_info = f" with index: {index_name}"
            print(f"{indent_str}{path} is a Group{index_info}")
            for key in item.keys():
                total_size_gb += explore_hdf5(item[key], path=f"{path}{key}/", indent=indent + 1)

        return total_size_gb

    with h5py.File(file_path, 'r') as f:
        total_size_gb = 0
        # Determine the dimensions of X depending on its format
        if isinstance(f['X'], h5py.Group):
            # Assume CSR or CSC format
            num_rows = f['obs'][f['obs'].attrs['_index']].shape[0]
            num_cols = f['var'][f['var'].attrs['_index']].shape[0]
            print(f"AnnData object with n_obs × n_vars = {num_rows} x {num_cols}")
        else:
            # Assume dense matrix
            n_obs, n_vars = f['X'].shape # pylint: disable=no-member
            print(f"AnnData object with n_obs × n_vars = {n_obs} x {n_vars}")
            dataset_size_gb = (np.prod(f['X'].shape) * f['X'].dtype.itemsize) / (1024 ** 3) # pylint: disable=no-member
            total_size_gb += dataset_size_gb  # Initialize total size with X dataset size

        total_size_gb += explore_hdf5(f)
        print(f"\nTotal size of the HDF5 file: {total_size_gb:.4f} GB")