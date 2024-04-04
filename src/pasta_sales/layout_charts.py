""" Contains variables for all the rows and elements in the 'charts' page """
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input
from pasta_sales.figures import line_chart


number_inputs = dbc.Col(
    [
        html.P("Type the brand number:"),
        dbc.Input(id="brand-input", type="number", value=1, min=1, max=4, step=1),
        html.P("Type the item number:"),
        dbc.Input(id="item-input", type="number", value=1, min=1, step=1)
    ],
    width=4
)

chart_output = dbc.Col(dcc.Graph(id="line-chart"), width=8)

chart_layout = dbc.Row([
    number_inputs,
    chart_output
])

@callback(
    Output("line-chart", "figure"),
    Input("brand-input", "value"),
    Input("item-input", "value")
)
def update_line_chart(brand_number, item_number):
    if brand_number is not None and item_number is not None:
        return line_chart(brand_number, item_number)