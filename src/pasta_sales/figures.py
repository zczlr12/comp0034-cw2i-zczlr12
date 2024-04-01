from pathlib import Path

import pandas as pd
import plotly.express as px

data_path = Path(__file__).parent.parent.parent.joinpath("data", "dataset_prepared.csv")


def line_chart(brand, item):
    """ Creates a line chart with data from dataset_prepared.csv

    Data is displayed over time from 01/01/2014 to 31/12/2018.
    The figure shows separate trends for the winter and summer events.

     Parameters
     feature: events, sports or participants

     Returns
     fig: Plotly Express line figure
     """
    
    quantity = f"QTY_B{brand}_{item}"
    promotion = f"PROMO_B{brand}_{item}"

    # Load the data from the CSV file
    line_chart_data = pd.read_csv(data_path)
    
    # take the feature parameter from the function and check it is valid
    if quantity not in line_chart_data.columns:
        raise ValueError("Invalid value for brand number or item number.")

    # Create a Plotly Express line chart with the following parameters
    #  line_chart_data is the DataFrane
    #  x="year" is the column to use as a x-axis
    #  y=feature is the column to use as the y-axis
    # color="type" indicates if winter or summer
    fig = px.line(line_chart_data, x="DATE", y=quantity, color=promotion)
    return fig
