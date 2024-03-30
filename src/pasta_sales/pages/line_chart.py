from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/line_chart")

layout = dbc.Container([
    html.H1("Line Chart")
])