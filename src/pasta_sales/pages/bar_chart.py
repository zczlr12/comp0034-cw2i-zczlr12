from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/bar_chart")

layout = dbc.Container([
    html.H1("Bar Chart"),
    dcc.Graph(
        id='bar_chart',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1], 'type': 'bar', 'name': 'Series 1'},
                {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'type': 'bar', 'name': 'Series 2'},
            ],
            'layout': {
                'title': 'Bar Chart'
            }
        }
    )
])