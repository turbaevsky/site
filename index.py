#!/usr/bin/python3

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#from dash.exceptions import PreventUpdate

from app import app
from apps import business, sentiment, cv
from apps import monitor
import layouts

from pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    feesMins,
    distributions,
    newsReviews,
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
],)
#style={'background-image': 'linear-gradient(to right, lightblue, lightgreen)'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/business':
        return layouts.navbar, business.body
    elif pathname == '/apps/sentiment':
        return layouts.navbar, sentiment.body
    elif pathname == '/apps/cv':
        return layouts.navbar, cv.body
    elif pathname == '/dash-financial-report/overview':
        return overview.create_layout(app)
    elif pathname == "/dash-financial-report/price-performance":
        return pricePerformance.create_layout(app)
    elif pathname == "/dash-financial-report/portfolio-management":
        return portfolioManagement.create_layout(app)
    elif pathname == "/dash-financial-report/fees":
        return feesMins.create_layout(app)
    elif pathname == "/dash-financial-report/distributions":
        return distributions.create_layout(app)
    elif pathname == "/dash-financial-report/news-and-reviews":
        return newsReviews.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            pricePerformance.create_layout(app),
            portfolioManagement.create_layout(app),
            feesMins.create_layout(app),
            distributions.create_layout(app),
            newsReviews.create_layout(app),
        )
    elif pathname == '/apps/monitor':
        return monitor.body
    else:
        return layouts.navbar, layouts.topic, layouts.cards


if __name__ == '__main__':
    app.run_server()
