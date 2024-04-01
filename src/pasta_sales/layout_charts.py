""" Contains variables for all the rows and elements in the 'charts' page """
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input
from pasta_sales.figures import line_chart

brand_number_input = html.Div(
    [
        html.P("Type the brand number:"),
        dbc.Input(id="brand-number-input", type="number", value=1, min=1, max=4, step=1)
    ]
)

item_number_input = html.Div(
    [
        html.P("Type the item number:"),
        dbc.Input(id="item-number-input", type="number", value=1, min=1, step=1)
    ]
)

number_inputs = html.Div(
    dbc.Row([
        dbc.Col([brand_number_input]),
        dbc.Col([item_number_input])
    ])
)

chart_output = html.Div(dcc.Graph(id="line-chart"))

@callback(
    Output("line-chart", "figure"),
    Input("brand-number-input", "value"),
    Input("item-number-input", "value")
)
def update_line_chart(brand_number, item_number):
    if brand_number is not None and item_number is not None:
        return line_chart(brand_number, item_number)