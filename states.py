from dash import Dash, html, dcc
from dash.dependencies import Input, Output


app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id="input-1", type='text', value='Montréal'),
    dcc.Input(id="input-2", type='text', value='Canada'),
    html.Div(id="number-output"),
])

@app.callback(
    Output("number-output", "children"),
    Input("input-1", "value"),
    Input("input-2", "value"),
)
def update_output(input1, input2):
    return f'Input 1 is {input1} and Input 2 is {input2}'

if __name__ == '__main__':
    app.run_server(debug=True)