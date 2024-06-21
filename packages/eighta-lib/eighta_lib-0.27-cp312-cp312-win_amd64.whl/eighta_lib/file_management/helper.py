"""
This module includes helper functions for file management functionalities.
"""
import subprocess
import os
from collections import OrderedDict
import h5py
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import anndata as ad

def load_h5ad(target: h5py.Group | h5py.Dataset, exclude: list[str] | None = None):
    """
    Load the data from the HDF5 file at the specified target location.

    Parameters:
    - target (h5py.Group | h5py.Dataset): The target location in the HDF5 file.

    Returns:
    - The data loaded from the HDF5 file.
    """
    # If the target is in the exclude list, return None
    ret = None

    if exclude is None or target.name not in exclude:
        if isinstance(target, h5py.Dataset):
            # We need to explicitly convert to string if the encoding-type is string/string-array
            if target.shape == ():  # scalar
                ret = (
                    str(target[()], "utf-8")
                    if target.attrs["encoding-type"] == "string"
                    else target[()]
                )
            else:  # array
                ret = (
                    np.array([str(val, "utf-8") for val in target[:]], dtype=object)
                    if target.attrs["encoding-type"] == "string-array"
                    else target[:]
                )
        else:
            # Load encoded group
            if "encoding-type" in target.attrs:
                # CSR matrix
                if target.attrs["encoding-type"] == "csr_matrix":
                    ret = csr_matrix(
                        (target["data"][:], target["indices"][:], target["indptr"][:]),
                        shape=target.attrs["shape"],
                    )
                # CSC matrix
                elif target.attrs["encoding-type"] == "csc_matrix":
                    ret = csc_matrix(
                        (target["data"][:], target["indices"][:], target["indptr"][:]),
                        shape=target.attrs["shape"],
                    )
                # Categorical data
                elif target.attrs["encoding-type"] == "categorical":
                    if target["categories"].attrs["encoding-type"] == "string-array":
                        categories = [
                            str(cat, "utf-8") for cat in target["categories"][:]
                        ]
                    else:
                        categories = target["categories"][:]
                    ret = pd.Categorical.from_codes(target["codes"][:], pd.Index(categories))
                # DataFrame
                elif target.attrs["encoding-type"] == "dataframe":
                    ret = load_dataframe_group(target, exclude=exclude)
                # Dictionary
                elif target.attrs["encoding-type"] == "dict":
                    ret = load_dict_group(target, exclude=exclude)
                elif target.attrs["encoding-type"] in ["raw", "anndata"]:
                    loaded_X = load_h5ad(target["X"], exclude=exclude)
                    # If X is None, create a dummy csc_matrix
                    if loaded_X is None:
                        shape = (
                            target["X"].attrs["shape"]
                            if isinstance(target, h5py.Group)
                            else target.shape
                        )
                        loaded_X = csc_matrix(([], [], np.zeros(shape[1] + 1)), shape=shape)
                    if target.attrs["encoding-type"] == "raw":
                        adata = ad.AnnData(
                            X=loaded_X,
                            var=load_dataframe_group(target["var"], exclude=exclude),
                            varm=load_dict_group(target["varm"], exclude=exclude),
                        )
                        ret = ad.Raw(adata)
                    else:
                        ret = ad.AnnData(
                            X=loaded_X,
                            obs=load_dataframe_group(target["obs"], exclude=exclude),
                            var=load_dataframe_group(target["var"], exclude=exclude),
                            obsm=load_dict_group(target["obsm"], exclude=exclude),
                            varm=load_dict_group(target["varm"], exclude=exclude),
                            obsp=load_dict_group(target["obsp"], exclude=exclude),
                            varp=load_dict_group(target["varp"], exclude=exclude),
                            layers=load_dict_group(target["layers"], exclude=exclude),
                            uns=load_dict_group(target["uns"], exclude=exclude),
                        )
                else:
                    raise NotImplementedError(
                        f"Unknown group type in {target.name}, please contact the developers."
                    )
            # If the group does not have an encoding-type, it is a regular group
            # We do not allow loading regular groups directly
            else:
                raise ValueError("Cannot load a group.")
    return ret


def load_dataframe_group(group: h5py.Group, exclude: list[str] | None = None):
    """
    Load a DataFrame group from the HDF5 file.

    Parameters:
    - group (h5py.Group): The group containing the DataFrame data.

    Returns:
    - pd.DataFrame: The DataFrame loaded from the HDF5 file.
    """
    index_name = group.attrs["_index"]
    index_data = group[index_name][:]
    if group[index_name].attrs["encoding-type"] == "string-array":
        index_data = [str(val, "utf-8") for val in index_data]
    columns = group.attrs["column-order"]
    # OrderedDict to preserve column order
    data = OrderedDict()
    for col in columns:
        # Only include the specified columns if exclude is None or the column is not in
        # the exclude list
        if exclude is None or f"{group.name}/{col}" not in exclude:
            if isinstance(group[col], h5py.Dataset):
                col_data = group[col][:]
                if group[col].attrs["encoding-type"] == "string-array":
                    col_data = [str(val, "utf-8") for val in col_data]
            else:
                if group[col].attrs["encoding-type"] == "categorical":
                    categories = group[col]["categories"][:]
                    if (
                        group[col]["categories"].attrs["encoding-type"]
                        == "string-array"
                    ):
                        categories = [str(cat, "utf-8") for cat in categories]
                    col_data = pd.Categorical.from_codes(
                        group[col]["codes"][:], pd.Index(categories)
                    )
                elif group[col].attrs["encoding-type"] == "csr_matrix" and (
                    group[col].attrs["shape"][0] == 1
                    or group[col].attrs["shape"][1] == 1
                ):
                    col_data = (
                        csr_matrix(
                            (
                                group[col]["data"][:],
                                group[col]["indices"][:],
                                group[col]["indptr"][:],
                            ),
                            shape=group[col].attrs["shape"],
                        )
                        .toarray()
                        .flatten()
                    )
                elif group[col].attrs["encoding-type"] == "csc_matrix" and (
                    group[col].attrs["shape"][0] == 1
                    or group[col].attrs["shape"][1] == 1
                ):
                    col_data = (
                        csc_matrix(
                            (
                                group[col]["data"][:],
                                group[col]["indices"][:],
                                group[col]["indptr"][:],
                            ),
                            shape=group[col].attrs["shape"],
                        )
                        .toarray()
                        .flatten()
                    )
                else:
                    raise NotImplementedError(
                        f"Unsupported format {group[col].attrs['encoding-type']}."
                    )
            # Add the value to the data dictionary with the column name as the key
            data[col] = col_data

    # If we did not include any data, it is not a root-level and not empty originally group,
    # return None
    if not data and group.name not in ["/obs", "/var"] and len(columns) > 0:
        return None
    # Create the DataFrame from the data dictionary
    # Set the index name if it is not the default '_index'
    df = pd.DataFrame(
        data,
        index=pd.Index(index_data, name=index_name if index_name != "_index" else None),
    )
    return df


def load_dict_group(group: h5py.Group, exclude: list[str] | None = None):
    """
    Load a dictionary group from the HDF5 file.

    Parameters:
    - group (h5py.Group): The group containing the dictionary data.

    Returns:
    - dict: The dictionary loaded from the HDF5 file.
    """
    data = {}
    for key, value in group.items():
        # Load the data only if it is not in the exclude list
        if exclude is None or f"{group.name}/{key}" not in exclude:
            # Dataset
            if isinstance(value, h5py.Dataset):
                if value.attrs["encoding-type"] == "numeric-scalar":
                    data[key] = value[()]
                elif value.attrs["encoding-type"] == "string":
                    data[key] = str(value[()], "utf-8")
                elif value.attrs["encoding-type"] == "array":
                    data[key] = value[:]
                elif value.attrs["encoding-type"] == "string-array":
                    data[key] = np.array(
                        [str(val, "utf-8") for val in value[:]], dtype=object
                    )
                else:
                    raise NotImplementedError(
                        f"Unsupported format {value.attrs['encoding-type']}."
                    )
            # Group
            else:
                if value.attrs["encoding-type"] == "dataframe":
                    val = load_dataframe_group(value, exclude=exclude)
                    # If the DataFrame is empty, do not include it
                    if val is not None:
                        data[key] = val
                elif value.attrs["encoding-type"] == "dict":
                    # Recursively load the dictionary
                    val = load_dict_group(value, exclude=exclude)
                    # If the dictionary is empty, do not include it
                    if val is not None:
                        data[key] = val
                elif value.attrs["encoding-type"] == "categorical":
                    if value["categories"].attrs["encoding-type"] == "string-array":
                        categories = [
                            str(cat, "utf-8") for cat in value["categories"][:]
                        ]
                    else:
                        categories = value["categories"][:]
                    data[key] = pd.Categorical.from_codes(value["codes"][:], pd.Index(categories))
                elif value.attrs["encoding-type"] == "csr_matrix":
                    data[key] = csr_matrix(
                        (value["data"][:], value["indices"][:], value["indptr"][:]),
                        shape=value.attrs["shape"],
                    )
                elif value.attrs["encoding-type"] == "csc_matrix":
                    data[key] = csc_matrix(
                        (value["data"][:], value["indices"][:], value["indptr"][:]),
                        shape=value.attrs["shape"],
                    )
                elif value.attrs["encoding-type"] in ["raw", "anndata"]:
                    # Find all paths of this group that can be deserialized
                    all_paths = find_all_deserializable_paths(value)
                    # Include the paths that are in the exclude list
                    group_exclude = (
                        [item for item in all_paths if item in exclude]
                        if exclude is not None
                        else []
                    )
                    if len(group_exclude) < len(all_paths):
                        loaded_X = load_h5ad(value["X"], exclude=group_exclude)
                        # If X is not in the include list, we need to create an empty dummy matrix
                        # with the correct shape
                        if loaded_X is None:
                            shape = (
                                value["X"].attrs["shape"]
                                if isinstance(value, h5py.Group)
                                else value.shape
                            )
                            loaded_X = csc_matrix(
                                ([], [], np.zeros(shape[1] + 1)), shape=shape
                            )
                        if value.attrs["encoding-type"] == "raw":
                            adata = ad.AnnData(
                                X=loaded_X,
                                var=load_dataframe_group(
                                    value["var"], exclude=group_exclude
                                ),
                                varm=load_dict_group(
                                    value["varm"], exclude=group_exclude
                                ),
                            )
                            data[key] = ad.Raw(adata)
                        else:
                            adata = ad.AnnData(
                                X=loaded_X,
                                obs=load_dataframe_group(
                                    value["obs"], exclude=group_exclude
                                ),
                                var=load_dataframe_group(
                                    value["var"], exclude=group_exclude
                                ),
                                obsm=load_dict_group(
                                    value["obsm"], exclude=group_exclude
                                ),
                                varm=load_dict_group(
                                    value["varm"], exclude=group_exclude
                                ),
                                obsp=load_dict_group(
                                    value["obsp"], exclude=group_exclude
                                ),
                                varp=load_dict_group(
                                    value["varp"], exclude=group_exclude
                                ),
                                layers=load_dict_group(
                                    value["layers"], exclude=group_exclude
                                ),
                                uns=load_dict_group(
                                    value["uns"], exclude=group_exclude
                                ),
                            )
                            data[key] = adata
                else:
                    raise NotImplementedError(
                        f"Unsupported format {value.attrs['encoding-type']}."
                    )

    # If we did not include any data, it is not a root-level group and not empty originally,
    # return None
    if (
        not data
        and group.name not in ["/obsm", "/varm", "/obsp", "/varp", "/uns", "/layers"]
        and len(group.items()) > 0
    ):
        return None
    return data

def repack_file(file_path: str):
    """
    Repack the HDF5 file to reclaim space.

    Parameters:
    - file_path (str): Path to the HDF5 file.
    """
    temp_file = file_path + ".temp"
    subprocess.run(["h5repack", file_path, temp_file], check=True)
    os.replace(temp_file, file_path)

def in_dataframe(file: h5py.Group, key: str):
    """
    Check if the key is a column in a DataFrame in the HDF5 file.

    Parameters:
    - file (h5py.Group): The HDF5 file to check.
    - key (str): The key to check.

    Returns:
    - bool: A boolean indicating whether the key is a column in a DataFrame.
    - str: The name of the DataFrame group if the key is a column in a DataFrame.
    - str: The name of the column if the key is a column in a DataFrame.
    """
    keys = key.split("/")
    # The last key is the column name
    column_name = keys.pop()
    # One level up is the group name
    current_group = "/".join(keys)
    # Check if the key is or is going to be a column in a DataFrame
    while current_group and (
        current_group not in file or "encoding-type" not in file[current_group].attrs
    ):
        # One level up is the new column name
        column_name = f"{keys.pop()}/{column_name}"
        current_group = "/".join(keys)
    if current_group and file[current_group].attrs["encoding-type"] == "dataframe":
        return True, current_group, column_name
    return False, None, None

def find_all_deserializable_paths(h5file: h5py.Group) -> list[str]:
    """
    Recursively find all paths in an HDF5 file that can be deserialized, filtering out
    paths based on certain encoding types and excluding specific datasets.

    Parameters:
    - hdf5_group (h5py.Group): The current HDF5 group to search within.

    Returns:
    - list[str]: A list of all unique paths to deserializable data within the HDF5 file,
           excluding datasets representing indices and children of any non-dictionary or 
           non-dataframe encoded groups, such as children of sparse matrix representation groups 
           and children of categorical groups.
    """
    dataset_paths = []
    for key in h5file.keys():
        full_key = f"{h5file.name}/{key}" if h5file.name != "/" else f"/{key}"
        if isinstance(h5file[key], h5py.Group):
            if "encoding-type" in h5file[key].attrs and h5file[key].attrs[
                "encoding-type"
            ] not in ["dict", "raw", "anndata"]:
                # dataframes we return the columns in the column-order
                if h5file[key].attrs["encoding-type"] == "dataframe":
                    dataset_paths.extend(
                        [
                            f"{full_key}/{col}"
                            for col in h5file[key].attrs["column-order"]
                        ]
                    )
                # for sparse matrices and categorical data, we skip the children
                else:
                    dataset_paths.append(full_key)
            # If the group is a dictionary/raw/anndata/regular group, we recursively search for
            # data paths
            else:
                dataset_paths.extend(find_all_deserializable_paths(h5file[key]))
        # If the key is a dataset, we add it to the list
        else:
            dataset_paths.append(full_key)
    return dataset_paths
