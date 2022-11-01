import dash
from dash import html, dcc
from pip import main
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd

#Dash app com multiplos inputs
css_externo = ['https://codepen.io/chriddyp/pen/bWLwP.css']

app = dash.Dash(__name__, external_stylesheets=css_externo)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

indicators = df['Indicator Name'].unique()

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in indicators],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'widht': '40%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in indicators],
                value='Life expectancy at birth, total (years)'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'widht': '40%', 'float':'right', 'display': 'inline-block'})
        ]),

        dcc. Graph(id='indicator-graphic'),

        dcc.Slider(
            id='year--slider',
            min=df['Year'].min(),
            max=df['Year'].max(),
            value=df['Year'].max(),
            marks={str(year): str(year) for year in df['Year'].unique()},
            step=None
        )
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),
     Input('year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value):
    nova_df=df[df['Year']==year_value]

    fig = px.scatter(x=nova_df[nova_df['Indicator Name'] == xaxis_column_name]['Value'],
                     y=nova_df[nova_df['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=nova_df[nova_df['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(margin={'l':40, 'b': 40, 't':10, 'r':0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)