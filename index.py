#!/usr/bin/python3

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#from dash.exceptions import PreventUpdate

from app import app
from apps import business, sentiment, cv
import layouts


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
],
style={'background-image': 'linear-gradient(to right, lightblue, lightgreen)'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/business':
        return layouts.navbar, business.body
    elif pathname == '/apps/sentiment':
        return layouts.navbar, sentiment.body
    elif pathname == '/apps/cv':
        return layouts.navbar, cv.body
    else:
        return layouts.navbar, layouts.topic, layouts.cards


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')