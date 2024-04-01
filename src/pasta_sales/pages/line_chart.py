from dash import html, register_page
import dash_bootstrap_components as dbc
from pasta_sales import layout_charts

register_page(__name__, path="/line_chart")

layout = dbc.Container([
    html.H1("Line Chart"),
    layout_charts.number_inputs,
    layout_charts.chart_output
])