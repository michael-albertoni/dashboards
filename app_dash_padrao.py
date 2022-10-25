import dash
from dash import html, dcc
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([

])

if __name__ == '__main__':
    app.run_server(debug=True)