from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/line_chart")

layout = dbc.Container([
    html.H1("Line Chart"),
    dcc.Graph(
        id='line_chart',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1], 'type': 'line', 'name': 'Series 1'},
                {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'type': 'line', 'name': 'Series 2'},
            ],
            'layout': {
                'title': 'Line Chart'
            }
        }
    )
])