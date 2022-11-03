import dash
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
css_externo = ['https://codepen.io/chriddyp/pen/bWLwP.css']

app = dash.Dash(__name__, external_stylesheets=css_externo)

app.layout = html.Div([
    dcc.Graph(id='Grafico-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


#Callbacks
@app.callback(
    #primeiro quem quero alterar, e depois o que quero alterar
    Output('Grafico-slider', 'figure'), 
    
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filtered_df = df[df['year'] == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                    size='pop', color='continent', hover_name='country',
                    log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)