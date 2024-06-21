"""
This module provides functions to update an HDF5 file. This is useful for interacting 
with .h5ad files without loading the entire file as an AnnData object in memory. 
"""
import h5py
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
from scipy.sparse import issparse
import anndata as ad
from . import helper

def update_h5ad(
    file_path: str, key: str, data, compression: str | None = None, repack: bool = True
):
    """
    Update the data at the specified key in the HDF5 file. If the key does not exist, 
    it will be created. Otherwise, the data will be overwritten.

    :param file_path: Path to the HDF5 file.
    :param key: The key specifying the location of the data to update.
    :param data: The data to be updated.
    :param compression: The compression algorithm to use. Default is None.
    :param repack: Whether to repack the file after updating. This can retrieve unused space in 
                    the file. Default is True.
    :raise KeyError: The key is invalid. See error message for more details.
    :raise ValueError: The shape or structure of the data is invalid. 
        See error message for more details
    """

    def validate_compatibility(
        file: h5py.File, key: str, data, is_in_df: bool, df_group: str
    ):
        """
        Validate that the data is compatible with the key.

        Parameters:
        - file (h5py.File): The HDF5 file object.
        - keys (list[str]): The components of the key.
        - data: The data to be updated.
        - is_in_df (bool): Whether the data is being appended to a DataFrame.
        - df_group (str): The group in which the DataFrame is stored.
        """
        # Check if the key is a column in a DataFrame
        keys = key.split("/")
        # Overwrite the root-level group
        if len(keys) == 1:
            if key not in file and key != "raw":
                raise KeyError(f"Key {key} not found in the .h5ad file.")
            if key == "X":
                validate_shape(data, (num_obs, num_var))
            # If the key is a DataFrame, validate the shape of the DataFrame
            elif key in ["obs", "var"] and isinstance(data, pd.DataFrame):
                validate_shape(data, (num_obs if key == "obs" else num_var,))
            # If the key is a dictionary, validate the shape of the dictionary
            elif key in [
                "obsm",
                "varm",
                "obsp",
                "varp",
                "layers",
                "uns",
            ] and isinstance(data, dict):
                # Different keys have different shapes
                if key in ["obsp", "varp", "layers"]:
                    row_shape = num_var if key == "varp" else num_obs
                    col_shape = num_obs if key == "obsp" else num_var
                    validate_dict_shape(data, (row_shape, col_shape))
                elif key in ["obsm", "varm"]:
                    row_shape = num_obs if key == "obsm" else num_var
                    validate_dict_shape(data, (row_shape,))
                # No shape validation needed for uns
                else:
                    pass
            # Update the raw data, no shape validation needed, but requires AnnData object or
            # .h5ad file
            elif key == "raw" and (
                isinstance(data, ad.AnnData)
                or (isinstance(data, str) and data.endswith(".h5ad"))
            ):
                pass
            else:
                raise KeyError(
                    "Cannot append to this location with the given data type."
                )
        # Overwrite a nested group or dataset
        else:
            # Only one level of nesting is allowed for these keys, otherwise it cannot be read
            # as an AnnData object
            if keys[0] in ["obsm", "varm", "obsp", "varp", "layers"] and len(keys) > 2:
                raise KeyError(
                    "Cannot append to this location. Only one level of nesting is allowed "
                    "for this key."
                )

            if keys[0] in ["obs", "var"]:
                validate_shape(data, (num_obs, 1) if keys[0] == "obs" else (num_var,))
            elif keys[0] == "obsm":
                validate_shape(data, (num_obs,))
                # If the data is being appended to a DataFrame, need to validate the row names
                if isinstance(data, pd.DataFrame):
                    obs_names = file["obs"][file["obs"].attrs["_index"]][:]
                    # Decode the byte strings to utf-8
                    expected_row_names = (
                        [str(name, "utf-8") for name in obs_names]
                        if np.issubdtype(obs_names.dtype, np.object_)
                        else obs_names
                    )
                    # Validate the row names of the DataFrame, should match the index names of
                    # the obs group
                    validate_dataframe_row_names(data, expected_row_names)
            elif keys[0] == "varm":
                validate_shape(data, (num_var,))
                # If the data is being appended to a DataFrame, need to validate the row names
                if isinstance(data, pd.DataFrame):
                    var_names = file["var"][file["var"].attrs["_index"]][:]
                    # Decode the byte strings to utf-8
                    expected_row_names = (
                        [str(name, "utf-8") for name in var_names]
                        if np.issubdtype(var_names.dtype, np.object_)
                        else var_names
                    )
                    # Validate the row names of the DataFrame, should match the index names of
                    # the var group
                    validate_dataframe_row_names(data, expected_row_names)
            elif keys[0] == "obsp":
                validate_shape(data, (num_obs, num_obs))
            elif keys[0] == "varp":
                validate_shape(data, (num_var, num_var))
            elif keys[0] == "layers":
                validate_shape(data, (num_obs, num_var))
            elif keys[0] == "uns":
                # If the data is being appended to a DataFrame, check if the shape matches
                # the dataframe shape
                if is_in_df:
                    validate_shape(
                        data, (file[df_group][file[df_group].attrs["_index"]].shape[0],)
                    )
            elif keys[0] == "raw" and len(keys) != 2:
                if "raw/X" not in file:
                    raise KeyError("Key 'raw' not found in the .h5ad file.")
                # Infer the shape of the data from the X matrix
                _, num_raw_var = file["raw/X"].attrs["shape"]
                if keys[1] == "var":
                    if isinstance(data, pd.DataFrame):
                        raise ValueError("Cannot append a DataFrame to this location.")
                    validate_shape(data, (num_raw_var, 1))
                elif keys[1] == "varm":
                    validate_shape(data, (num_raw_var,))
                    # If the data is being appended to a DataFrame, need to validate the row names
                    if isinstance(data, pd.DataFrame):
                        raw_var_names = file["raw/var"][
                            file["raw/var"].attrs["_index"]
                        ][:]
                        # Decode the byte strings to utf-8
                        expected_row_names = (
                            [str(name, "utf-8") for name in raw_var_names]
                            if np.issubdtype(raw_var_names.dtype, np.object_)
                            else raw_var_names
                        )
                        # Validate the row names of the DataFrame, should match the index names of
                        # the raw/var group
                        validate_dataframe_row_names(data, expected_row_names)
                else:
                    raise KeyError("Cannot append to this location.")
            else:
                raise KeyError("Cannot append to this location.")

    def validate_shape(data, expected_shape: tuple):
        """
        Validate the shape of the data against the expected shape.

        Parameters:
        - data: The data to validate.
        - expected_shape (tuple): The expected shape of the data.
        """
        if isinstance(data, list):
            # expected_shape should be (len(data), 1) or (len(data),)
            if len(data) != expected_shape[0] or (
                len(expected_shape) > 1 and expected_shape[1] != 1
            ):
                raise ValueError(
                    f"List length {len(data)} does not match expected shape {expected_shape}."
                )
        else:
            if data.shape[0] != expected_shape[0]:
                raise ValueError(
                    f"Data shape {data.shape} does not match expected shape {expected_shape}."
                )
            if len(expected_shape) > 1:
                if (len(data.shape) == 1 and expected_shape[1] != 1) or (
                    len(data.shape) > 1 and data.shape[1] != expected_shape[1]
                ):
                    raise ValueError(
                        f"Data shape {data.shape} does not match expected shape {expected_shape}."
                    )

    def validate_dict_shape(data_dict: dict, expected_shape: tuple):
        """
        Validate the shape of the dictionary against the expected shape.

        Parameters:
        - data_dict (dict): The dictionary to validate.
        - expected_shape (tuple): The expected shape of the dictionary.
        """
        for _, value in data_dict.items():
            validate_shape(value, expected_shape)

    def validate_dataframe_row_names(df: pd.DataFrame, expected_names: list):
        """
        Validate the row names of the DataFrame against the expected names.

        Parameters:
        - df (pd.DataFrame): The DataFrame to validate.
        - expected_names (list): The expected row names.
        """
        if not df.index.equals(pd.Index(expected_names)):
            raise ValueError(
                f"DataFrame row names {df.index.to_list()} do not match expected names "
                f"{expected_names}."
            )

    # Split the key into its components
    keys = key.split("/")
    with h5py.File(file_path, "a") as f:
        # Infer the shape of the data from the X matrix
        if isinstance(f["X"], h5py.Dataset):
            num_obs, num_var = f["X"].shape
        else:
            num_obs, num_var = f["X"].attrs["shape"]
        # If data is a pandas Series, convert it to a numpy array
        if isinstance(data, pd.Series):
            data = data.values
        # If data is a pandas DataFrame and we are updating to a key in 'obsp', 'varp', or
        # 'layers', convert it to a numpy array
        if isinstance(data, pd.DataFrame):
            if key == "X":
                data = data.to_numpy()
            elif len(keys) > 1:
                if keys[0] in ["obsp", "varp", "layers"]:
                    data = data.to_numpy()
                elif keys[0] in ["obs", "var"] and data.shape[1] == 1:
                    data = data.to_numpy().flatten()

        if isinstance(data, dict) and key in ["obsp", "varp", "layers"]:
            for key_dict, value in data.items():
                if isinstance(value, pd.DataFrame):
                    data[key_dict] = value.to_numpy()
        # Check if the key is a column in a DataFrame
        is_in_df, df_group, df_col = helper.in_dataframe(f, key)

        # If the data is a scalar and we append it to a DataFrame, repeat it to match the shape of
        # the DataFrame
        if isinstance(data, (bool, str, int, float, complex)):
            if is_in_df:
                data = np.repeat(
                    data, f[df_group][f[df_group].attrs["_index"]].shape[0]
                )

        # Validate the compatibility of the data with the key
        validate_compatibility(f, key, data, is_in_df, df_group)

        is_deleted = False
        if key in f:
            del f[key]
            is_deleted = True

    # Cannot repack during append mode
    if is_deleted and repack:
        helper.repack_file(file_path)

    with h5py.File(file_path, "a") as f:
        # Perform the update
        deep_update(f, keys, data, compression=compression)

        # Update column-order after a successful deep_update
        if is_in_df:
            if is_deleted:
                # Delete all the columns starting with the same prefix
                column_order = [col if isinstance(col, str) else str(col, "utf-8")
                                for col in f[df_group].attrs["column-order"]]
                f[df_group].attrs["column-order"] = np.array(
                    [col for col in column_order if not col.startswith(df_col)], dtype="S")
            f[df_group].attrs["column-order"] = np.array(
                np.append(f[df_group].attrs["column-order"], df_col),
                dtype=h5py.special_dtype(vlen=str)
            )

def deep_update(file: h5py.Group, keys: list[str], data, compression: str | None = None):
    """
    Recursively updates the data at the specified key in the HDF5 file.

    Parameters:
    - file (h5py.Group): The HDF5 group to update.
    - keys (list): A list of keys specifying the location of the data to update.
    - data: The data to be updated.
    - compression (str): The compression algorithm to use. Default is None.
    - repack (bool): Whether to repack the file after updating. This can retrieve unused space 
    in the file. Default is True.
    """

    def create_anndata_group(
        file: h5py.Group, name: str, data: ad.AnnData, compression: str | None = None
    ):
        """
        Create a new group in the HDF5 file to store an AnnData object.

        Parameters:
        - file (h5py.Group): The parent group in the HDF5 file.
        - name (str): The name of the new group.
        - data (ad.AnnData): The AnnData object to be stored in the new group.
        - compression (str): The compression algorithm to use.
        """
        anndata_group = file.create_group(name)
        anndata_group.attrs.update(
            {"encoding-type": "anndata", "encoding-version": "0.1.0"}
        )
        # Extract all the root-level components of the AnnData object
        if issparse(data.X):
            create_sparse_matrix_group(
                anndata_group, "X", data.X, compression=compression
            )
        else:
            create_dataset(anndata_group, "X", data.X, "array", compression=compression)
        create_dataframe_group(anndata_group, "obs", data.obs, compression=compression)
        create_dataframe_group(anndata_group, "var", data.var, compression=compression)
        create_dict_group(anndata_group, "obsm", data.obsm, compression=compression)
        create_dict_group(anndata_group, "varm", data.varm, compression=compression)
        create_dict_group(anndata_group, "obsp", data.obsp, compression=compression)
        create_dict_group(anndata_group, "varp", data.varp, compression=compression)
        create_dict_group(anndata_group, "layers", data.layers, compression=compression)
        create_dict_group(anndata_group, "uns", data.uns, compression=compression)
        if data.raw is not None:
            create_raw_group(anndata_group, "raw", data.raw, compression=compression)

    def create_raw_group(
        file: h5py.Group, name: str, data: ad.AnnData | ad.Raw, compression: str | None = None
    ):
        """
        Create a new raw group in the HDF5 file.

        Parameters:
        - file (h5py.Group): The parent group in the HDF5 file.
        - keys (list[str]): The components of the key.
        - data: The data to be stored in the raw group.
        - compression (str): The compression algorithm to use.
        """
        # raw group is a special case, it is a group with X, var, and varm datasets of
        # the AnnData object
        raw_group = file.create_group(name)
        raw_group.attrs.update({"encoding-type": "raw", "encoding-version": "0.1.0"})
        # Extract the X, var, and varm datasets from the AnnData object
        if issparse(data.X):
            create_sparse_matrix_group(raw_group, "X", data.X, compression=compression)
        else:
            create_dataset(raw_group, "X", data.X, "array", compression=compression)
        create_dataframe_group(raw_group, "var", data.var, compression=compression)
        create_dict_group(raw_group, "varm", data.varm, compression=compression)

    def create_dataset(
        group: h5py.Group,
        name: str,
        data,
        encoding_type: str,
        encoding_version: str = "0.2.0",
        dtype: type | None = None,
        compression: str | None = None,
    ):
        """
        Helper function to create a dataset in the HDF5 file.

        Parameters:
        - group (h5py.Group): The HDF5 group to create the dataset in.
        - name (str): The name of the dataset.
        - data: The data to be stored in the dataset.
        - encoding_type (str): The encoding type of the dataset.
        - encoding_version (str): The encoding version of the dataset.
        - dtype: The data type of the dataset.
        - compression (str): The compression algorithm to use.
        """
        # If the string array has duplicates, convert it to a categorical
        if (
            isinstance(data, np.ndarray)
            and len(data.shape) == 1
            and np.issubdtype(data.dtype, np.str_)
            and len(data) != len(np.unique(data))
        ):
            # ordered=False to match the behavior of the AnnData object
            data = pd.Categorical(data, ordered=False)
        # Create categorical group
        if isinstance(data, pd.Categorical):
            new_group = group.create_group(name)
            new_group.attrs.update(
                {
                    "encoding-type": "categorical",
                    "encoding-version": encoding_version,
                    "ordered": data.ordered,
                }
            )
            data_type = (
                np.object_
                if data.categories.dtype == h5py.special_dtype(vlen=str)
                else None
            )
            encoding_type = "string-array" if data_type == np.object_ else "array"
            create_dataset(
                new_group,
                "categories",
                data.categories,
                encoding_type,
                dtype=data_type,
                compression=compression,
            )
            create_dataset(
                new_group, "codes", data.codes, "array", compression=compression
            )
        # Create regular dataset
        else:
            if np.issubdtype(dtype, np.object_):
                dtype = h5py.special_dtype(vlen=str)
                data = np.array(data, dtype="S")
            group.create_dataset(name, data=data, dtype=dtype, compression=compression)
            group[name].attrs.update(
                {"encoding-type": encoding_type, "encoding-version": encoding_version}
            )

    def create_dataframe_group(
        group: h5py.Group, name: str, data: pd.DataFrame, compression: str | None = None
    ):
        """
        Create a new group in the HDF5 file to store a DataFrame.

        Parameters:
        - group (h5py.Group): The parent group in the HDF5 file.
        - name (str): The name of the new group.
        - data (pd.DataFrame): The DataFrame to be stored in the new group.
        - compression (str): The compression algorithm to use.
        """
        index_name = data.index.name if data.index.name is not None else "_index"
        new_group = group.create_group(name)
        # Convert all the column names to strings
        data.columns = data.columns.astype(str)
        # Add metadata
        new_group.attrs.update(
            {
                "_index": index_name,
                "column-order": np.array(
                    data.columns, dtype=h5py.special_dtype(vlen=str)
                ),
                "encoding-type": "dataframe",
                "encoding-version": "0.2.0",
            }
        )
        # If the index is a string, use a variable-length string type which can be accepted by
        # h5py create_dataset function, they are equivalent.
        index_dtype = (
            h5py.special_dtype(vlen=str)
            if np.issubdtype(np.dtype(data.index.dtype), np.object_) # type: ignore
            else None
        )
        new_group.create_dataset(
            index_name,
            data=data.index.values,
            dtype=index_dtype,
            compression=compression,
        )
        new_group[index_name].attrs.update(
            {
                "encoding-type": "string-array"
                if index_dtype == h5py.special_dtype(vlen=str)
                else "array",
                "encoding-version": "0.2.0",
            }
        )
        for col in data.columns:
            col_data = data[col].values
            col_dtype = (
                np.object_
                if isinstance(col_data, pd.Categorical)
                and col_data.categories.dtype == h5py.special_dtype(vlen=str)
                or col_data.dtype == np.object_
                else None
            )
            create_dataset(
                new_group,
                col,
                col_data,
                "string-array" if col_dtype == np.object_ else "array",
                dtype=col_dtype,
                compression=compression,
            )

    def create_dict_group(
        group: h5py.Group, name: str, data: dict, compression: str | None = None
    ):
        """
        Create a new group in the HDF5 file to store a dictionary.

        Parameters:
        - group (h5py.Group): The parent group in the HDF5 file.
        - name (str): The name of the new group.
        - data (dict): The dictionary to be stored in the new group.
        - compression (str): The compression algorithm to use.
        """
        new_group = group.create_group(name)
        new_group.attrs.update({"encoding-type": "dict", "encoding-version": "0.1.0"})
        for key, value in data.items():
            # Handle different data types
            if isinstance(value, (bool, int, float, complex)):
                create_dataset(
                    new_group,
                    key,
                    np.array(value),
                    "numeric-scalar",
                    compression=compression,
                )
            elif isinstance(value, str):
                create_dataset(new_group, key, value, "string", compression=compression)
            elif isinstance(value, pd.DataFrame):
                create_dataframe_group(new_group, key, value, compression=compression)
            elif isinstance(value, dict):
                create_dict_group(new_group, key, value, compression=compression)
            elif isinstance(value, list):
                # Handle list of strings
                if any(isinstance(i, str) for i in value):
                    # Convert all elements to strings
                    str_value = np.array(value, dtype="S")
                    create_dataset(
                        new_group,
                        key,
                        str_value,
                        "string-array",
                        dtype=np.object_,
                        compression=compression,
                    )
                # Handle list of numbers
                elif all(isinstance(i, (bool, int, float, complex)) for i in value):
                    create_dataset(
                        new_group,
                        key,
                        np.array(value),
                        "array",
                        compression=compression,
                    )
                else:
                    raise TypeError(f"Unsupported list type in key {key}.")
            elif isinstance(value, np.ndarray):
                # Handle array of strings
                if np.issubdtype(value.dtype, np.object_) or np.issubdtype(
                    value.dtype, np.str_
                ):
                    create_dataset(
                        new_group,
                        key,
                        value,
                        "string-array",
                        dtype=np.object_,
                        compression=compression,
                    )
                else:
                    create_dataset(
                        new_group, key, value, "array", compression=compression
                    )
            elif isinstance(value, pd.Categorical):
                if np.issubdtype(value.categories.dtype, np.object_) or np.issubdtype(
                    value.categories.dtype, np.str_
                ):
                    create_dataset(
                        new_group, key, value, "string-array", compression=compression
                    )
                else:
                    create_dataset(
                        new_group, key, value, "array", compression=compression
                    )
            elif isinstance(value, ad.AnnData):
                create_anndata_group(new_group, key, value, compression=compression)
            elif isinstance(value, ad.Raw):
                create_raw_group(new_group, key, value, compression=compression)
            else:
                raise TypeError(f"Unsupported data type {type(value)} for key {key}.")

    def create_sparse_matrix_group(
        group: h5py.Group, name: str, data, compression: str | None = None
    ):
        """
        Create a new group in the HDF5 file to store a sparse matrix.

        Parameters:
        - group (h5py.Group): The parent group in the HDF5 file.
        - name (str): The name of the new group.
        - data: The sparse matrix to be stored in the new group.
        """
        if isinstance(data, (csr_matrix, csc_matrix)):
            sparse_group = group.create_group(name)
            sparse_group.create_dataset("data", data=data.data, compression=compression)
            sparse_group.create_dataset(
                "indices", data=data.indices, compression=compression
            )
            sparse_group.create_dataset(
                "indptr", data=data.indptr, compression=compression
            )
            sparse_group.attrs.update(
                {
                    "shape": data.shape,
                    "encoding-type": "csr_matrix"
                    if isinstance(data, csr_matrix)
                    else "csc_matrix",
                    "encoding-version": "0.1.0",
                }
            )
        else:
            raise TypeError(f"Unsupported sparse matrix format {type(data)}.")

    # Base case
    if len(keys) == 1:
        if issparse(data):
            # Handle csr_matrix or csc_matrix
            create_sparse_matrix_group(file, keys[0], data, compression=compression)
        elif isinstance(data, ad.AnnData):
            # If we are updating to 'raw' with an AnnData object, we need to create a raw group
            if len(keys) == 1 and keys[0] == "raw":
                create_raw_group(file, keys[0], data, compression=compression)
            else:
                create_anndata_group(file, keys[0], data, compression=compression)
        elif isinstance(data, ad.Raw):
            create_raw_group(file, keys[0], data, compression=compression)
        # Copying raw data from another file
        # Since it already has the correct postfix '.h5ad'(We checked in update_h5ad),
        # we can just copy the X, var, and varm datasets directly
        elif keys[0] == "raw" and isinstance(data, str):
            raw_group = file.create_group("raw")
            raw_group.attrs.update(
                {"encoding-type": "raw", "encoding-version": "0.1.0"}
            )
            with h5py.File(data, "r") as f:
                f.copy("X", raw_group)
                f.copy("var", raw_group)
                f.copy("varm", raw_group)
        elif isinstance(data, list):
            # Handle list of strings
            if any(isinstance(i, str) for i in data):
                str_data = np.array(data, dtype="S")
                create_dataset(
                    file,
                    keys[0],
                    str_data,
                    "string-array",
                    dtype=np.object_,
                    compression=compression,
                )
            # Handle list of numbers
            elif all(isinstance(i, (bool, int, float, complex)) for i in data):
                create_dataset(
                    file, keys[0], np.array(data), "array", compression=compression
                )
            else:
                raise TypeError(f"Unsupported list type in key {keys[0]}.")
        elif isinstance(data, (bool, int, float, np.bool_)):
            create_dataset(
                file, keys[0], data, "numeric-scalar", compression=compression
            )
        elif isinstance(data, str):
            create_dataset(file, keys[0], data, "string", compression=compression)
        elif isinstance(data, pd.Categorical):
            # Handle categorical data
            # If the categories are strings, annotate the categories as string-array
            if np.issubdtype(data.categories.dtype, np.object_) or np.issubdtype(
                data.categories.dtype, np.str_
            ):
                create_dataset(
                    file, keys[0], data, "string-array", compression=compression
                )
            else:
                create_dataset(file, keys[0], data, "array", compression=compression)
        elif isinstance(data, np.ndarray):
            # if data is an array of strings
            if np.issubdtype(data.dtype, np.str_):
                create_dataset(
                    file,
                    keys[0],
                    data,
                    "string-array",
                    dtype=np.object_,
                    compression=compression,
                )
            else:
                create_dataset(file, keys[0], data, "array", compression=compression)
        elif isinstance(data, pd.DataFrame):
            create_dataframe_group(file, keys[0], data, compression=compression)
        elif isinstance(data, dict):
            # Handle dictionary
            create_dict_group(file, keys[0], data, compression=compression)
        else:
            raise TypeError(
                f"Unsupported data type {type(data)} for key {keys[0]}. We need to implement this "
                "if needed."
            )
    else:
        if keys[0] not in file:
            file.create_group(keys[0])
        # Recursively update the next level
        deep_update(file[keys[0]], keys[1:], data, compression=compression)
