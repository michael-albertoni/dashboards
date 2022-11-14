import dash_bootstrap_components as dbc
import dash
from dash import html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]



app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(card_content, color="primary", inverse=True, style={"height": "90vh", "margin": "10px"})
        ], sm=4),
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color="info", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="secondary", inverse=True)),
            ], style={"margin": "10px"}),
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color="warning", inverse=True), md=4),
                dbc.Col(dbc.Card(card_content, color="error", inverse=False), md=4),
                dbc.Col(dbc.Card(card_content, color="danger", inverse=True), md=4),
            ], style={"margin": "10px"}),
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)