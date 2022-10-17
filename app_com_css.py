import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

#1 opção de link
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#2 opção de arquivo com css
#app = dash.Dash(__name__)
#Cria pasta assets
#Cria um arquivo com extensão .css como styles.css
# O Dash vai reconhecer sozinho

#3 opção direto inline


app = dash.Dash(__name__)


app.layout = html.Div(id="div1",
    children=[
        html.H1("Hello Dash", id="h1"),
        #exemplo inline    html.H1("Hello Dash", id="h1", style={"color":"#000"}),

        html.Div("Dash um framework web para Python"),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)