import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

#importando bootstrap components
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

load_figure_template("bootstrap")

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

#conteúdo da aplicação
df_data = pd.read_csv('supermarket_sales.csv')
#ajusta coluna de datas para não ficar como string e sim como data
df_data['Date'] = pd.to_datetime(df_data['Date'])
cidades = df_data["City"].value_counts().index



#Layout
app.layout = html.Div(children=[

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2("Dashboard", style={"font-size": "30px"}),
                html.Hr(),
                html.H5("Cidades:"),
                #checklist primeiro a lista, e depois a lista com os marcados, id para acessar pelo Callback
                dcc.Checklist(cidades, cidades, id='check_city', inputStyle={"margin": "10px 5px 10px 20px"}),

                html.H5("Variável de análise:", style={"margin-top": "20px"}),
                #radio buttons, primeiro a lista, e depois o item padrão selecionado
                dcc.RadioItems(["gross income", "Rating"],  "gross income", id="main_variable", inputStyle={"margin": "10px 5px 10px 20px"})

            ], style={"height": "90vh", "padding": "10px", "margin": "10px"})
                
            ], sm=2),

        dbc.Col([

            dbc.Row([
                dbc.Col([dcc.Graph(id='city_fig')], sm=4),
                dbc.Col([dcc.Graph(id='gender_fig')], sm=4),
                dbc.Col([dcc.Graph(id='pay_fig')], sm=4),
                
            ]),
            dbc.Row([dcc.Graph(id='income_per_date_fig')]),
            dbc.Row([dcc.Graph(id='income_per_product_fig')])


            #gráficos criados pelos callbacks
            
            
        ], sm=10)
    ])    
])

#Callbacks
@app.callback(
    [
        Output('city_fig', 'figure'),
        Output('pay_fig', 'figure'),
        Output('gender_fig', 'figure'),
        Output('income_per_date_fig', 'figure'),
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
    df_gender = df_filtered.groupby(["Gender", "City"])[main_variable].apply(operation).to_frame().reset_index()
    df_payment = df_filtered.groupby("Payment")[main_variable].apply(operation).to_frame().reset_index()
    df_product_income = df_filtered.groupby(["Product line","City"])[main_variable].apply(operation).to_frame().reset_index()
    df_income_time = df_filtered.groupby("Date")[main_variable].apply(operation).to_frame().reset_index()

    #criar figuras dos gráficos
    fig_city = px.bar(df_city, x='City', y=main_variable)
    fig_payment = px.bar(df_payment, y='Payment', x=main_variable, orientation='h')
    fig_gender = px.bar(df_gender, x='Gender', y=main_variable, color='City', barmode='group')
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line', color="City", orientation='h', barmode='group')
    fig_income_date = px.bar(df_income_time, y=main_variable, x='Date')

    #alteração de layout
    for fig in [fig_city, fig_payment, fig_gender, fig_income_date]:
        fig.update_layout(margin=dict(l=0,r=30,t=20,b=20), height=200, template='bootstrap')

    fig_product_income.update_layout(margin=dict(l=0,r=30,t=20,b=20), height=500)

    return fig_city, fig_payment,fig_gender, fig_income_date, fig_product_income

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)