from dash import html, dcc, register_page, callback, Output, Input
import dash_bootstrap_components as dbc
from pasta_sales.figures import current_trend_chart

register_page(__name__, path="/current_trends")

number_inputs = dbc.Col(
    [
        html.Br(),
        html.Br(),
        html.P("Type the brand number:"),
        dbc.Input(id="current-trend-brand-input", type="number", min=1, step=1),
        html.P("Type the item number:"),
        dbc.Input(id="current-trend-item-input", type="number", min=1, step=1),
        html.Br(),
        html.Div(id="current-trend-error-message")
    ],
    width=4,
)

chart_output = dbc.Col(dcc.Graph(id="current-trend-line-chart"), width=8)

chart_layout = dbc.Row([
    number_inputs,
    chart_output
])

layout = dbc.Container([
    html.H1("Current Trends"),
    chart_layout
])


@callback(
    Output("current-trend-line-chart", "figure"),
    Input("current-trend-brand-input", "value"),
    Input("current-trend-item-input", "value")
)
def update_current_trend(brand_number, item_number):
    try:
        return current_trend_chart(brand_number, item_number)
    except ValueError:
        return {}


@callback(
    Output("current-trend-error-message", "children"),
    Input("current-trend-brand-input", "value"),
    Input("current-trend-item-input", "value")
)
def update_currrent_trend_error_message(brand_number, item_number):
    if brand_number is None or item_number is None:
        return dbc.Alert("Please enter a brand number and an item number.",
                         color="info")
    try:
        current_trend_chart(brand_number, item_number)
    except ValueError:
        return dbc.Alert("Invalid value for brand number or item number.",
                         color="danger")