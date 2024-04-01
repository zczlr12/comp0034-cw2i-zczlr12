from dash import register_page, callback, Output, Input, State, html, dcc

register_page(__name__, path="/register")

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

layout = html.Div([
    html.Div([
        "Username",
        dcc.Input(id="user", type="text", placeholder="Enter Username",className="inputbox1",
                  style=INPUT_STYLE)
    ]),
    html.Div([
        "Password",
        dcc.Input(id="passw1", type="text", placeholder="Enter Password",className="inputbox2",
                  style=INPUT_STYLE)
    ]),
    html.Div(
        dcc.Input(id="passw2", type="text", placeholder="Repeat Password",className="inputbox3",
                  style=INPUT_STYLE)
    ),
    html.Div(
        dcc.Input(id="first_name", type="text", placeholder="Enter First Name",className="inputbox4",
                  style=INPUT_STYLE)
    ),
    html.Div(
        dcc.Input(id="last_name", type="text", placeholder="Enter Last Name",className="inputbox5",
                  style=INPUT_STYLE)
    ),
    html.Div(
        dcc.Input(id="email", type="text", placeholder="Enter Email",className="inputbox6",
                  style=INPUT_STYLE)
    ),
    html.Div(
        html.Button('Login', id='verify', n_clicks=0, style={'border-width':'3px','font-size':'14px'}),
        style={'margin-left':'45%','padding-top':'30px'}),
    html.Div(id='output2')
])