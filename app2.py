import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd


#possibilidade de css externo
link_externo = ['https://codepen.io/exemplo.css']


# Inicialização padrão
# app = dash.Dash(__name__)

#inicialização com link externo
#app = dash.Dash(__name__, external_stylesheets = link_externo)

#deixar o css dentro da pasta criada assets o dash reconhece arquivos de extensão .csv
app = dash.Dash(__name__)

#pode ser adicionado inline como o exemplo abaixo

#-------------------------------------
#   CONFIGURA LAYOUT
#-------------------------------------

# dcc é dash_core_components


app.layout = html.Div(id="div1",
    children=[
        #normal
        #html.H1("Hello Dash", id="h1"),
        
        #css inline
        html.H1("Hello Dash", id="h1", style={"color":"red"}),

        html.Div("Dash um framework web para Python"),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)