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
cidades = df_data["City"].value_counts().index



#Layout
app.layout = html.Div(children=[
    html.H5("Cidades:"),
    #checklist primeiro a lista, e depois a lista com os marcados, id para acessar pelo Callback
    dcc.Checklist(cidades, cidades, id='check_city'),

    html.H5("Variável de análise:"),
    #radio buttons, primeiro a lista, e depois o item padrão selecionado
    dcc.RadioItems(["gross income", "Rating"],  "gross income", id="main_variable"),

    #gráficos criados pelos callbacks
    dcc.Graph(id='city_fig'),
    dcc.Graph(id='pay_fig'),
    dcc.Graph(id='income_per_product_fig'),

])


#Callbacks



if __name__ == '__main__':
    app.run_server(port=8050, debug=True)