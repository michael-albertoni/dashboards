import dash

import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Frutas":["Maça", "Laranja", "Bananas", "Maça", "Laranja", "Bananas"],
    "Quantidade":[4, 1, 2, 2, 4, 5],
    "UF":["PR", "PR", "PR", "SP", "SP", "SP"]
})

#Cria o gráfico
fig = px.bar(df, x="Frutas", y="Quantidade", color="UF")

#-------------------------------------
#   CONFIGURA LAYOUT
#-------------------------------------
from dash import html, dcc
# dcc é dash_core_components


app.layout = html.Div(id="div1",
    children=[
        html.H1("Hello Dash", id="h1"),

        html.Div("Dash um framework web para Python"),

        dcc.Graph(figure=fig, id="graph")
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)