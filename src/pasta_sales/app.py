import dash
from dash import Dash, html, dcc, Input, Output, State
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

INPUT_STYLE = {
    'margin-left':'35%',
    'width':'450px',
    'height':'45px',
    'padding':'10px',
    'margin-top':'60px',
    'font-size':'16px',
    'border-width':'3px',
    'border-color':'#a0a3a2'
}

index_page = html.Div([
    html.Div(
        dcc.Input(id="user", type="text", placeholder="Enter Username",className="inputbox1",
                  style=INPUT_STYLE)
    ),
    html.Div(
        dcc.Input(id="passw", type="text", placeholder="Enter Password",className="inputbox2",
                  style=INPUT_STYLE)
    ),
    html.Div(
        html.Button('Login', id='verify', n_clicks=0, style={'border-width':'3px','font-size':'14px'}),
        style={'margin-left':'45%','padding-top':'30px'}),
    html.Div(id='output1')
])

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

app.layout = index_page

@app.callback(
    Output('output1', 'children'),
    Input('verify', 'n_clicks'),
    State('user', 'value'),
    State('passw', 'value')
)
def update_output(n_clicks, uname, passw):
    li = {'shraddha': 'admin123'}
    if uname == '' or uname == None or passw == '' or passw == None:
        return html.Div(children='', style={'padding-left': '550px', 'padding-top':'10px'})
    elif uname not in li:
        return html.Div(children='Incorrect Username',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
    elif li[uname]==passw:
        return html.Div(dcc.Link('Access Granted!', href= '/', style={'color':'#183d22','font-family': 'serif', 'font-weight': 'bold', "text-decoration": "none",'font-size':'20px'}),style={'padding-left':'605px','padding-top':'40px'})
    else:
        return html.Div(children='Incorrect Password',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})

if __name__ == '__main__':
    app.run(debug=True)