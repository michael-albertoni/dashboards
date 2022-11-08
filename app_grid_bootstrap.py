import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

#o bootstrap considera uma grid de 12 colunas
#md é a medida média - ver documentação
#sm é a medida small para telas menores
app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div("Column"), style={"background": "#ff0000"}, md=6, sm=4),
        dbc.Col(html.Div("Column"), md=3, sm=4),
        dbc.Col(html.Div("Column"), md=3, sm=4)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)