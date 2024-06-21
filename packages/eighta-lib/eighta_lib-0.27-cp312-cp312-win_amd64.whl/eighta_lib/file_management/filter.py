"""
This module provides functions to partially load data from from an HDF5 file. This 
is useful for interacting with .h5ad files without loading the entire file as an 
AnnData object in memory. 
"""
import h5py
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import anndata as ad
from . import helper

def filter_anndata_h5ad(
    file_path: str, include: list[str] | None = None, exclude: list[str] | None = None
):
    """
    Filter the data in an HDF5-stored AnnData object and partially load it based on 
    the specified keys. Only able to filter deserializable paths.
    
    :param file_path: Path to the HDF5 file.
    :param include: A list of keys to include in the filtered data.
    :param exclude: A list of keys to exclude from the filtered data.

    :return: An AnnData object containing the filtered data.

    :raise ValueError: Both 'include' and 'exclude' is specified while only one of 
        them can be used at a time.
    :raise TypeError: The 'include' or 'exclude' parameter must be a list of string.
        This error indicates user attempt to input a string.
    """

    if include is not None and exclude is not None:
        raise ValueError("Only one of 'include' or 'exclude' can be used at a time.")
    # Load the entire dataset if no include/exclude is specified
    if include is None and exclude is None:
        return ad.read_h5ad(file_path)
    # Ensure the include and exclude parameters are lists of strings
    if isinstance(include, str):
        raise TypeError("The 'include' parameter must be a list of strings.")
    if isinstance(exclude, str):
        raise TypeError("The 'exclude' parameter must be a list of strings.")

    with h5py.File(file_path, "r") as f:
        path_list = helper.find_all_deserializable_paths(f)
        # Exhaustively exclude all children of the specified keys
        if exclude is not None:
            exclude_list = set()
            for key in exclude:
                if key not in f:
                    raise KeyError(f"Key {key} not found in the .h5ad file.")
                exclude_list.update(get_group_and_children(key, path_list))
            exclude = [item for item in path_list if item in exclude_list]
        # Complement the include list with all children of the specified keys to get
        # the exclude list
        else:
            include_list = set()
            for key in include: # type: ignore[union-attr]
                if key not in f:
                    raise KeyError(f"Key {key} not found in the .h5ad file.")
                include_list.update(get_group_and_children(key, path_list))
            exclude = [item for item in path_list if item not in include_list]
        # Load the whole anndata object if the exclude list is empty
        if not exclude:
            return ad.read_h5ad(file_path)

        # Determine the X matrix
        filtered_X = helper.load_h5ad(f["X"], exclude=exclude)
        # If X is not in the include list, we need to create an empty dummy matrix with
        # the correct shape
        if filtered_X is None:
            shape = (
                f["X"].attrs["shape"]
                if isinstance(f["X"], h5py.Group)
                else f["X"].shape
            )
            if shape[0] > shape[1]:
                filtered_X = csc_matrix(([], [], np.zeros(shape[1] + 1)), shape=shape)
            else:
                filtered_X = csr_matrix(([], [], np.zeros(shape[0] + 1)), shape=shape)

        adata = ad.AnnData(
            X=filtered_X,
            layers=helper.load_dict_group(f["layers"], exclude=exclude),
            obs=helper.load_dataframe_group(f["obs"], exclude=exclude),
            var=helper.load_dataframe_group(f["var"], exclude=exclude),
            obsm=helper.load_dict_group(f["obsm"], exclude=exclude),
            varm=helper.load_dict_group(f["varm"], exclude=exclude),
            obsp=helper.load_dict_group(f["obsp"], exclude=exclude),
            varp=helper.load_dict_group(f["varp"], exclude=exclude),
            uns=helper.load_dict_group(f["uns"], exclude=exclude),
        )

        # Load the raw data if it is in the file and not excluded
        if "raw" in f:
            # Find all the deserializable paths in the raw group
            raw_path_list = helper.find_all_deserializable_paths(f["raw"])
            # The deserializable paths in the raw group that are in the exclude list
            raw_exclude = [item for item in raw_path_list if item in exclude]
            # Load the raw data with the exclude list if any of the raw data is not excluded
            if len(raw_exclude) < len(raw_path_list):
                raw = helper.load_h5ad(f["raw"], exclude=raw_exclude)
                adata.raw = ad.AnnData(X=raw.X, var=raw.var, varm=raw.varm)
        return adata

def get_group_and_children(group: str, group_list: list[str]):
    """
    Get the specified group and all its children from the group list.

    Parameters:
    - group (str): The group to get.
    - group_list (list[str]): A list of groups to search.

    Returns:
    - list[str]: A list of groups and their children, depending on the inclusion or 
    exclusion criteria.
    """
    # Ensure the group name starts with a '/' for uniform and consistent handling across
    # different representations.
    # Example transformation: 'uns/a/b' becomes '/uns/a/b'.
    if not group.startswith("/"):
        group = "/" + group
    return [
        item for item in group_list if item == group or item.startswith(group + "/")
    ]
