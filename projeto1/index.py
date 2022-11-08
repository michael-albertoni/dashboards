import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server

#conteúdo da aplicação
df_data = pd.read_csv('supermarket_sales.csv')
#ajusta coluna de datas para não ficar como string e sim como data
df_data['Date'] = pd.to_datetime(df_data['Date'])




#Layout
app.layout = html.Div(children=[

])


#Callbacks



if __name__ == '__main__':
    app.run_server(port=8050, debug=True)