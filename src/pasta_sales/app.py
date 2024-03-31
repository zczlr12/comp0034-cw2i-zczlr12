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

row_one = dbc.Row([
    dbc.Col(html.Button("Change password", id="change_passw", n_clicks=0)),
    dbc.Col(html.Button("Logout", id="logout", n_clicks=0))
])

sidebar = html.Div(
    [
        html.H2("Pasta sales", className="display-6"),
        html.Hr(),
        html.P(
            "Menu", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Line Chart", href="/line_chart", active="exact"),
                dbc.NavLink("Bar Chart", href="/bar_chart", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE
)

content = html.Div(
    [
        row_one,
        dash.page_container
    ],
    id="page-content",
    style=CONTENT_STYLE
)

app.layout = html.Div(id="app-content")

@app.callback(
    Output("app-content", "children"),
    Input("change_passw", "n_clicks"),
    Input("logout", "n_clicks")
)
def display_page(change_passw, logout):
    if ctx.triggered_id == "logout":
        return dbc

if __name__ == '__main__':
    app.run(debug=True)
