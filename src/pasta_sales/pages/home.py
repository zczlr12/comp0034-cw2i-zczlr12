from pathlib import Path
from dash import html, Output, Input, dcc, callback, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

AUTHORS = """Paolo Mancuso, Veronica Piccialli, Antonio M. Sudoso (University of
Rome Tor Vergata)"""
DESCRIPTION = """The dataset contains hierarchical sales data gathered from an
Italian grocery store. The dataset consists of 118 daily time series
representing the SKU-level sales from 01/01/2014 to 31/12/2018 of 4 national
pasta brands. Besides univariate time series data, the quantity sold is
integrated by information on the presence or the absence of a promotion. These
time series can be naturally arranged to follow a 3-level hierarchical
structure (seehttps://www.sciencedirect.com/science/article/pii/S0957417421005431)."""
ADDITIONAL_INFO = """- QTY_B'X'_'Y' - the quantity sold for brand 'X' item 'Y'
- PROMO_B'X'_'Y' - the promotion flag for brand 'X' and item 'Y'"""

data_path = Path(__file__).parents[3].joinpath("data", "dataset_prepared.csv")

layout = dbc.Container([
    html.H1("Home"),
    html.P("Please use the sidebar to navigate to different pages."),
    html.H2("About the Data"),
    dbc.Accordion(
        [
            dbc.AccordionItem(AUTHORS, title="Authors"),
            dbc.AccordionItem(
                dcc.Link(
                    "Creative Commons Attribution 4.0 International",
                    href="https://creativecommons.org/licenses/by/4.0/legalcode",
                    target="_blank"
                ),
                title="License"
            ),
            dbc.AccordionItem(
                [
                    html.P(DESCRIPTION),
                    html.Div(ADDITIONAL_INFO, style={"white-space": "pre"})
                ],
                title="Description"
            )
        ],
        always_open=True,
        start_collapsed=True
    ),
    dbc.Button("Download the Data", id="btn-raw-data", className="col-12",
               color="primary", outline=True),
    dcc.Download(id="download-raw-data")
])


@callback(
    Output("download-raw-data", "data"),
    Input("btn-raw-data", "n_clicks"),
    prevent_initial_call=True
)
def download_raw_data(n_clicks):
    return dcc.send_file(data_path, "pasta_sales.csv")