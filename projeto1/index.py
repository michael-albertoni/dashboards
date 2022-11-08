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
@app.callback(
    [
        Output('city_fig', 'figure'),
        Output('pay_fig', 'figure'),
        Output('income_per_product_fig', 'figure')
    ],
    [    
        Input('check_city', 'value'),
        Input('main_variable', 'value')
    ]   
)
def render_graphs(cities, main_variable):
    #define a operação a ser realizada com os dados se vai usar soma ou média de acordo com o radio selecionado
    operation = np.sum if main_variable == 'gross income' else np.mean
    
    #filtra cidades
    df_filtered = df_data[df_data['City'].isin(cities)]
    
    #selecionar colunas
    df_city = df_filtered.groupby("City")[main_variable].apply(operation).to_frame().reset_index()
    df_payment = df_filtered.groupby("Payment")[main_variable].apply(operation).to_frame().reset_index()
    df_product_income = df_filtered.groupby(["Product line","City"])[main_variable].apply(operation).to_frame().reset_index()

    #criar figuras dos gráficos
    fig_city = px.bar(df_city, x='City', y=main_variable)
    fig_payment = px.bar(df_payment, y='Payment', x=main_variable, orientation='h')
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line', color="City", orientation='h', barmode='group')

    #alteração de layout
    fig_city.update_layout(margin=dict(l=0,r=0,t=20,b=20), height=200)
    fig_payment.update_layout(margin=dict(l=0,r=0,t=20,b=20), height=200)
    fig_product_income.update_layout(margin=dict(l=0,r=0,t=20,b=20), height=500)

    return fig_city, fig_payment, fig_product_income

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)