"""
This module provides a wrapper class 'BackedAnnData' for other implemented methods.
"""

import os
import h5py
import numpy as np
import pandas as pd
import psutil
import eighta_lib
import eighta_lib.file_management
import eighta_lib.file_management.helper


# pylint: disable=too-many-instance-attributes
class BackedAnnData:
    """
    BackedAnnData class provides slice, delete, update on disk for .h5ad file.

    :param file_path: The path to the .h5ad file. 
    """

    def __init__(self, file_path: str) -> None:
        """
        Constructor of BackedAnnData.

        :param file_path: The path to the .h5ad file.
        """
        try:
            with h5py.File(file_path):
                self.file_path = file_path
                self.obs = Group("obs", file_path)
                self.var = Group("var", file_path)
                self.uns = Group("uns", file_path)
                self.obsm = Group("obsm", file_path)
                self.varm = Group("varm", file_path)
                self.layers = Group("layers", file_path)
                self.obsp = Group("obsp", file_path)
                self.varp = Group("varp", file_path)
                self.raw = Group("raw", file_path)
        except Exception as exc:
            raise FileNotFoundError(
                "The given path cannot be opened as hdf5 file."
            ) from exc

    def __repr__(self) -> str:
        with h5py.File(self.file_path) as file:
            # pylint: disable=unpacking-non-sequence
            n_obs, n_var = (
                file["X"].shape
                if isinstance(file["X"], h5py.Dataset)
                else file["X"].attrs["shape"]
            )
            res = f"BackedAnnData object with (n_obs x n_var) = ({n_obs} x {n_var})\n"
            for field in [
                "obs",
                "var",
                "uns",
                "obsm",
                "varm",
                "layers",
                "obsp",
                "varp",
            ]:
                res = res + f"    {field}: "
                for key in file[field].keys():
                    if key != "_index":
                        res = res + f"'{key}', "
                res = res[:-2] + "\n"
            res += f"\n  backing file: '{self.file_path}'\n"
            res += f"  size on dish: {os.path.getsize(self.file_path)/(1024**3):.4f} GB"
        return res

    def __str__(self) -> str:
        return f"<BackAnnData object with file path '{self.file_path}'>"

    def detailed_info(self) -> str:
        """
        Explores the structure of the HDF5 file.

        :return: A string with detailed information for the HDF5 file. 
                Formatted in a human understandable way.
        :rtype: str
        """

        def convert_size(size):
            if size / (1024**3) > 0.01:
                return f"{(size / (1024 ** 3)):.4f} GB"
            if size / (1024**2) > 0.01:
                return f"{(size / (1024 ** 2)):.4f} MB"
            if size / 1024 > 0.01:
                return f"{(size / 1024):.4f} KB"
            return f"{size:.4f} Bytes"

        def dataset_to_string(dataset, key, indent):
            indent_str = "  " * indent
            if isinstance(dataset, h5py.Dataset):
                dataset_size = np.prod(dataset.shape) * dataset.dtype.itemsize
                if dataset.attrs.get("encoding-type") in ["string", "string-array"]:
                    # pylint: disable=line-too-long
                    return f"{indent_str}{key}: string {dataset.shape}, {convert_size(dataset_size)}\n"
                # pylint: disable=line-too-long
                return f"{indent_str}{key}: {dataset.dtype} {dataset.shape}, {convert_size(dataset_size)}\n"

            if isinstance(dataset, h5py.Group):
                if dataset.attrs.get("encoding-type") == "csr_matrix":
                    dataset_size = 0
                    for i in ["data", "indptr", "indices"]:
                        dataset_size += dataset[i].size * dataset[i].dtype.itemsize
                    # pylint: disable=line-too-long
                    return f"{indent_str}{key}: sparse csr_matrix, {dataset['data'].size} elements, {convert_size(dataset_size)}\n"
                if dataset.attrs.get("encoding-type") == "csc_matrix":
                    dataset_size = 0
                    for i in ["data", "indptr", "indices"]:
                        dataset_size += dataset[i].size * dataset[i].dtype.itemsize
                    # pylint: disable=line-too-long
                    return f"{indent_str}{key}: sparse csc_matrix, {dataset['data'].size} elements, {convert_size(dataset_size)}\n"
                if dataset.attrs.get("encoding-type") == "categorical":
                    dataset_size = 0
                    for i in ["categories", "codes"]:
                        dataset_size += dataset[i].size * dataset[i].dtype.itemsize
                    # pylint: disable=line-too-long
                    return f"{indent_str}{key}: Categorical ({dataset['categories'].size} categories), {convert_size(dataset_size)}\n"
                res_str = f"{indent_str}{key}:\n"
                for child in dataset.keys():
                    if child != "_index":
                        res_str += dataset_to_string(
                            dataset[child],
                            child,
                            indent + 1,
                        )
                return res_str
            print(key, dataset, type(dataset))
            raise ValueError("The item needs to be either a database or a group.")

        with h5py.File(self.file_path) as file:
            # pylint: disable=unpacking-non-sequence
            n_obs, n_var = (
                file["X"].shape
                if isinstance(file["X"], h5py.Dataset)
                else file["X"].attrs["shape"]
            )
            res = f"BackedAnnData object with (n_obs x n_var) = ({n_obs} x {n_var})\n"
            for key, item in file.items():
                res += dataset_to_string(item, key, 1)
            res += f"\n  backing file: '{self.file_path}'\n"
            res += f"  size on dish: {convert_size(os.path.getsize(self.file_path))}"
            return res

    @property
    def shape(self) -> tuple:
        """
        Find the shape of the X matrix.

        :return: A tuple of the shape, in (number of obs, number of var).
        """
        with h5py.File(self.file_path) as file:
            # pylint: disable=unpacking-non-sequence
            n_obs, n_var = (
                file["X"].shape
                if isinstance(file["X"], h5py.Dataset)
                else file["X"].attrs["shape"]
            )
            return (n_obs, n_var)

    # pylint: disable=invalid-name
    @property
    def X(self):
        """
        Load the X matrix into memory. The matrix will be in type as its stored in the database. 
        The library currently support CSR matrix, CSC matrix and ndarray.

        :return: The X matrix
        :raises MemoryError: The size of X matrix is more than 70% of the available memory.
        """
        def convert_size(size):
            if size / (1024**3) > 0.01:
                return f"{(size / (1024 ** 3)):.4f} GB"
            if size / (1024**2) > 0.01:
                return f"{(size / (1024 ** 2)):.4f} MB"
            if size / 1024 > 0.01:
                return f"{(size / 1024):.4f} KB"
            return f"{size:.4f} Bytes"

        with h5py.File(self.file_path) as file:
            X_size = 0
            if file["X"].attrs.get("encoding-type") in ["csc_matrix", "csr_matrix"]:
                for key in file["X"].keys():
                    X_size += file["X"][key].dtype.itemsize * file["X"][key].size
            else:
                X_size = np.prod(file["X"].shape) * file["X"].dtype.itemsize # pylint: disable=no-member
            available_memory = psutil.virtual_memory().available
            print(f"The size of X is {convert_size(X_size)}.")
            print(f"Available memory is {convert_size(available_memory)}.")
            if X_size > available_memory * 0.7:
                raise MemoryError(
                    f"The size of X is more than 70% of available memory. "
                    f"Have {convert_size(available_memory)}, need {convert_size(X_size)}. "
                    f"If you want to continue anyway, call '.force_X().'"
                )
            return eighta_lib.file_management.helper.load_h5ad(file["X"])

    def force_X(self):
        """
        Load the X matrix into memory without memory check.

        :return: The X matrix
        """
        with h5py.File(self.file_path) as file:
            return eighta_lib.file_management.helper.load_h5ad(file["X"])

    def __getitem__(self, key):
        if isinstance(key, str):
            with h5py.File(self.file_path) as file:
                data = eighta_lib.file_management.helper.load_h5ad(file[key])
                keys = key.split("/")
                if keys[0] in ["obs", "var"] and len(keys) > 1:
                    return pd.Series(
                        data,
                        index=pd.Index(
                            file[keys[0]][file[keys[0]].attrs["_index"]][:].astype(
                                "str"
                            ),
                            name=file[keys[0]].attrs["_index"],
                        ),
                    )
                return data
        elif isinstance(key, slice):
            with h5py.File(self.file_path) as file:
                # pylint: disable=unsubscriptable-object
                n_var = (
                    file["X"].shape[1]
                    if isinstance(file["X"], h5py.Dataset)
                    else file["X"].attrs["shape"][1]
                )
            return eighta_lib.read_slice_h5ad(self.file_path, key, slice(n_var))
        elif isinstance(key, tuple):
            return eighta_lib.read_slice_h5ad(self.file_path, key[0], key[1])
        else:
            raise KeyError("Invalid key.")

    def __setitem__(self, name: str, new_value):
        eighta_lib.update_h5ad(self.file_path, name, new_value)

    def __delitem__(self, name: str):
        eighta_lib.pop_h5ad(self.file_path, name, do_return=False)

    def remove(self, key: str, repack: bool = True):
        """
        Remove the data at the specified key in the HDF5 file.

        :param key: The key specifying the location of the data to remove.
        :param repack: Whether to repack the file after removing the data. Defaults to True.
        """
        eighta_lib.pop_h5ad(self.file_path, key, repack=repack, do_return=False)

    def pop(self, key: str, repack: bool = True):
        """
        Remove the data at the specified key in the HDF5 file and return it.

        :param key: The key specifying the location of the data to remove.
        :param repack: Whether to repack the file after removing the data. Defaults to True.
        :return: The data that was removed.
        """
        return eighta_lib.pop_h5ad(self.file_path, key, repack=repack)

    def slice_to_file(self, new_file_path: str, row: slice, col: slice):
        """
        Writes a sliced version of an h5ad file to a new destination file 
        using 10% of available memory.

        :param new_file_path: The path to the destination h5ad file.
        :param row: The slice object defining the row indices to include.
        :param col: The slice object defining the column indices to include.
        :raises ValueError: If no rows or columns are selected for slicing.
        """
        eighta_lib.write_slice_h5ad(self.file_path, new_file_path, row, col)

    def filter(self, include: list[str] | None = None, exclude: list[str] | None = None):
        """
        Filter the data in an HDF5-stored AnnData object and partially load it based on 
        the specified keys. Only able to filter deserializable paths.
        
        :param include: One key or a list of keys to include in the filtered data.
        :param exclude: One key or a list of keys to exclude from the filtered data.

        :return: An AnnData object containing the filtered data.
        """
        return eighta_lib.filter_anndata_h5ad(self.file_path, include, exclude)


class Group:
    """
    Helper class for operations to a certain group in the dataset.
    """

    def __init__(self, key, file_path) -> None:
        self.key = key
        self.file_path = file_path

    def __getitem__(self, name: str):
        with h5py.File(self.file_path) as file:
            data = eighta_lib.file_management.helper.load_h5ad(file[f"{self.key}/{name}"])
            if self.key in ["obs", "var"] and name != "":
                return pd.Series(
                    data,
                    index=pd.Index(
                        file[self.key][file[self.key].attrs["_index"]][:].astype("str"),
                        name=file[self.key].attrs["_index"],
                    ),
                )
            return data

    def __setitem__(self, name: str, new_value):
        eighta_lib.update_h5ad(self.file_path, f"{self.key}/{name}", new_value)

    def __delitem__(self, name: str):
        eighta_lib.pop_h5ad(self.file_path, f"{self.key}/{name}")
