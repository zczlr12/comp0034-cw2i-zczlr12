import re
import pandas as pd


def rearrange_data(data):
    """Rearrange the data to have a hierarchical structure.

    Parameters
    ----------
    data : pandas.DataFrame
        The original data with columns for each brand and item combination.

    Returns
    -------
    pandas.DataFrame
        The rearranged data with a hierarchical structure.
    """
    # Create a list to store the data
    rearranged_data = []
    # Loop over the columns in the original data
    for column in data.columns:
        # Check if the column name matches the pattern for quantity
        match_obj = re.match(r"QTY_B(\d+)_(\d+)", column)
        if match_obj is not None:
            # Extract the brand and item number from the column name
            brand, item = match_obj.groups()
            temp = data[["DATE", match_obj.group()]].rename(
                columns={"DATE": "Date", match_obj.group(): "Quantity"}
            )
            temp["Store"] = "1"
            temp["Brand"] = brand
            temp["Item"] = item
            # Append the new dataframe to the list
            rearranged_data.append(temp)
    # Concatenate the columns in the list to create the rearranged data
    return pd.concat(rearranged_data)