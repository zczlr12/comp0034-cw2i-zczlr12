from dash import html, dcc, register_page, callback, Output, Input, State
import dash_bootstrap_components as dbc
from pasta_sales.figures import future_trend_line
from pasta_sales.prediction import predict_future_trend

register_page(__name__, path="/future_trends")

number_inputs = dbc.Col(
    [
        html.Br(),
        html.Br(),
        html.P("Type the brand number:"),
        dbc.Input(id="future-trend-brand-input", type="number", min=1, step=1),
        html.Br(),
        html.P("Type the item number:"),
        dbc.Input(id="future-trend-item-input", type="number", min=1, step=1),
        html.Br(),
        dbc.Button("Download the result", id="btn-prediction-results", className="col-12",
                   color="primary", outline=True),
        dcc.Download(id="download-prediction-results"),
        html.Br(),
        html.Br(),
        html.Div(id="future-trend-error-message")
    ],
    width=4
)

chart_output = dbc.Col(dcc.Graph(id="future-trend-line-chart"), width=8)


layout = dbc.Container([
    html.H1("Future Trends"),
    dbc.Row([number_inputs, chart_output])
])


@callback(
    Output("future-trend-line-chart", "figure"),
    Input("future-trend-brand-input", "value"),
    Input("future-trend-item-input", "value"),
    prevent_initial_call=True
)
def update_results(brand_number, item_number):
    try:
        return future_trend_line(brand_number, item_number)
    except ValueError:
        return {}


@callback(
    Output("future-trend-error-message", "children"),
    Input("future-trend-brand-input", "value"),
    Input("future-trend-item-input", "value")
)
def update_future_trend_error_message(brand_number, item_number):
    if brand_number is None or item_number is None:
        return dbc.Alert("Please enter a brand number and an item number.",
                         color="info")
    try:
        future_trend_line(brand_number, item_number)
    except ValueError:
        return dbc.Alert("Invalid value for brand number or item number.",
                         color="danger")
    

@callback(
    Output("download-prediction-results", "data"),
    Input("btn-prediction-results", "n_clicks"),
    State("future-trend-brand-input", "value"),
    State("future-trend-item-input", "value"),
    prevent_initial_call=True
)
def download_prediction_results(n_clicks, brand_number, item_number):
    try:
        result_df = predict_future_trend(brand_number, item_number)
        return dcc.send_data_frame(result_df.to_csv, "future_trend_line.csv")
    except ValueError:
        return
