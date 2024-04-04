from dash import html, register_page
import dash_bootstrap_components as dbc
from pasta_sales import layout_charts

register_page(__name__, path="/current_trends")

layout = dbc.Container([
    html.H1("Current Trends"),
    layout_charts.chart_layout
])