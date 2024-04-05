from pathlib import Path

import pandas as pd
import plotly.express as px

data_path = Path(__file__).parent.parent.parent.joinpath("data", "dataset_prepared.csv")


def current_trend_chart(brand, item):
    """ Create a line chart for the current trend of the pasta sales

    Data is displayed over time from 01/01/2014 to 31/12/2018.
    The figure shows separate trends with and without promotion.

     Parameters
     brand: brand number
     item: item number

     Returns
     fig: Plotly Express line figure
     """

    # Load the data from the CSV file
    line_chart_data = pd.read_csv(data_path)

    # Generate the title, quantity and promotion columns
    title_text = f"Current trend for brand {brand} item {item}"
    quantity = f"QTY_B{brand}_{item}"
    promotion = f"PROMO_B{brand}_{item}"
    column_names = line_chart_data.columns

    # check whether the item is valid
    if quantity not in column_names or promotion not in column_names:
        raise ValueError("Invalid value for brand number or item number.")

    # Replace the 0 and 1 values in the promotion column with more descriptive text
    replace_values = {0: "Without Promotion", 1: "With Promotion"}
    line_chart_data[promotion].replace(replace_values, inplace=True) 

    # Create a Plotly Express line chart with the following parameters
    #  line_chart_data is the DataFrane
    #  x="DATE" is the column to use as a x-axis
    #  y=f"QTY_B{brand}_{item}" is the column to use as the y-axis
    # color=f"PROMO_B{brand}_{item}" indicates if promotion was present
    fig = px.line(line_chart_data,
                  x="DATE",
                  y=quantity,
                  color=promotion,
                  title=title_text,
                  labels={'DATE': 'Date', quantity: 'Quantity', promotion: ''}
                  )
    return fig
