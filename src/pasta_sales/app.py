import dash
from dash import Dash, html, Input, Output, ctx
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

mata_tages = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
]

app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets, meta_tags=mata_tages)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H5("Pasta sales predictor", className="text-center"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Current Trends", href="/current_trends",
                            active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE
)

content = html.Div(
    dash.page_container,
    id="page-content",
    style=CONTENT_STYLE
)

app.layout = html.Div([sidebar, content])

if __name__ == '__main__':
    app.run(debug=True)
