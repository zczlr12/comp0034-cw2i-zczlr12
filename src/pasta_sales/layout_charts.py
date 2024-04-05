""" Contains variables for all the rows and elements in the 'charts' page """
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input, exceptions
from pasta_sales.figures import current_trend_chart


number_inputs = dbc.Col(
    [
        html.Br(),
        html.Br(),
        html.P("Type the brand number:"),
        dbc.Input(id="brand-input", type="number", min=1, step=1),
        html.P("Type the item number:"),
        dbc.Input(id="item-input", type="number", min=1, step=1),
        html.Br(),
        html.Div(id="error-message")
    ],
    width=4,
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
    try:
        return current_trend_chart(brand_number, item_number)
    except ValueError:
        return {}


@callback(
    Output("error-message", "children"),
    Input("brand-input", "value"),
    Input("item-input", "value")
)
def update_error_message(brand_number, item_number):
    if brand_number is None or item_number is None:
        return dbc.Alert("Please enter a brand number and an item number.",
                         color="info")
    try:
        current_trend_chart(brand_number, item_number)
    except ValueError:
        return dbc.Alert("Invalid value for brand number or item number.",
                         color="danger")