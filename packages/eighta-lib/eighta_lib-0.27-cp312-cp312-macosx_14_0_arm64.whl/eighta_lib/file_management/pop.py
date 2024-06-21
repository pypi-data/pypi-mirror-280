"""
This module provides functions to pop from an HDF5 file. This is useful for interacting 
with .h5ad files without loading the entire file as an AnnData object in memory. 
"""
import h5py
import pandas as pd
from . import helper

def pop_h5ad(file_path: str, key: str, repack: bool = True, do_return = True):
    """
    Remove the data at the specified key in the HDF5 file and return it.

    :param file_path: Path to the HDF5 file.
    :param key: The key specifying the location of the data to remove.
    :param repack: Whether to repack the file after removing the data. Defaults to True.
    :param do_return: Whether to return the removed data. Defaults to true.

    :return: The data that was removed is do_return is True. Otherwise None.
    :raise KeyError: The specified key is invalid. See error message for more details.
    """
    keys = key.split("/")
    # We do not allow removing the whole X/obs/var group
    if len(keys) < 2 and key not in [
        "obsm",
        "varm",
        "obsp",
        "varp",
        "uns",
        "layers",
        "raw",
    ]:
        raise KeyError(f"Invalid target key {key}. Cannot remove from this location.")

    with h5py.File(file_path, "a") as f:
        # Check if the target exists in the file
        if key not in f:
            raise KeyError(f"{key} not found in the .h5ad file.")

        # We do not allow removing the whole raw/var group
        if key in ["raw/var", "raw/X"]:
            raise KeyError(
                f"Cannot remove the whole {key} group. Please specify a column to remove."
            )

        if "encoding-type" in f[key].parent.attrs and f[key].parent.attrs[
            "encoding-type"
        ] in ["categorical", "csr_matrix", "csc_matrix"]:
            raise KeyError(
                f"Cannot remove {key}. Please remove the whole parent group instead."
            )

        # Check if the target is a column in a DataFrame
        is_in_df, df_group, df_col = helper.in_dataframe(f, key)
        # Load the data before deleting it
        if do_return:
            ret = helper.load_h5ad(f[key])

        # If the target is a column in a DataFrame
        if is_in_df:
            # Return a pd.Series with the corresponding indices
            # Indices needs to be converted to a list of strings
            if do_return:
                indices = [
                    x.decode("utf-8") for x in f[df_group][f[df_group].attrs["_index"]][:]
                ]
                # Return the data as a pd.Series with the corresponding indices
                ret = pd.Series(
                    ret,
                    index=pd.Index(
                        indices,
                        name=f[df_group].attrs["_index"]
                        if f[df_group].attrs["_index"] != "_index"
                        else None,
                    ),
                    name=df_col,
                )

            if df_col not in f[df_group].attrs["column-order"]:
                raise KeyError(f"{df_col} not found in the {df_group} group.")
            # Remove the column from the column-order
            f[df_group].attrs["column-order"] = [
                col for col in f[df_group].attrs["column-order"] if col != df_col
            ]

        # Delete the target dataset or group
        del f[key]

        # Check if we need to delete any upper-level empty groups
        group_components = keys[:-1]
        group_path = "/".join(group_components)
        while (
            group_components
            and isinstance(f[group_path], h5py.Group)
            and "encoding-type" not in f[group_path].attrs
            and len(f[group_path]) == 0
        ):
            # Delete the empty group
            del f[group_path]
            # Move up one level
            group_components.pop()
            group_path = "/".join(group_components)

        # If we deleted a root-level group, we need to make a new empty group
        if key in ["obsm", "varm", "obsp", "varp", "uns", "layers", "raw/varm"]:
            group = (
                f["raw"].create_group("varm")
                if key == "raw/varm"
                else f.create_group(key)
            )
            group.attrs.update({"encoding-type": "dict", "encoding-version": "0.1.0"})
    # Repack the file to reclaim space
    if repack:
        helper.repack_file(file_path)

    if do_return:
        return ret
