from dash import register_page, callback, Output, Input, State, html, dcc

register_page(__name__, path="/login")

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

@callback(
    Output('output1', 'children'),
    Input('verify', 'n_clicks'),
    State('user', 'value'),
    State('passw', 'value')
)
def update_output(n_clicks, uname, passw):
    li = {'shraddha': 'admin123'}
    if uname == '' or uname is None or passw == '' or passw is None:
        return html.Div(children='', style={'padding-left': '550px', 'padding-top':'10px'})
    elif uname not in li:
        return html.Div(children='Incorrect Username', style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
    elif li[uname]==passw:
        return html.Div(dcc.Link('Access Granted!', href='/', style={'color':'#183d22','font-family': 'serif', 'font-weight': 'bold', "text-decoration": "none",'font-size':'20px'}),style={'padding-left':'605px','padding-top':'40px'})
    else:
        return html.Div(children='Incorrect Password', style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})