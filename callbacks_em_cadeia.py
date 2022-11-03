from dash import Dash, html, dcc, Input, Output, State

app = Dash(__name__)

all_options = {
    'USA': ['New York', 'San Francisco', 'Cincinnati'],
    'Canada': ['Montreal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'USA',
        id='countries-radio',
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-radio'),
    
    html.Hr(),

    html.Div(id='display-selected-values')
])

@app.callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

@app.callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(available_options):
    #tras selecionado o primeiro valor
    return available_options[0]['value']

@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return f'{selected_city} is a city in {selected_country}'





if __name__ == '__main__':
    app.run_server(debug=True)