from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from pasta_sales import layout_charts

register_page(__name__, path="/future_trends")

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


layout = dbc.Container([
    html.H1("Future Trends"),
    dbc.Row([number_inputs])
])