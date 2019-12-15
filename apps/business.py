import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import pandas as pd

from app import app

import dash
import base64
import dash_table
import datetime
import io

df = pd.DataFrame(data={'x':[1,2,3,4,5], 'y': [5,4,3,2,1]})

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return dict(table=html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            style_table={
                'maxHeight': '200px',
                'overflowY': 'scroll'
    },
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ]),
    data = df)


body = dbc.Container(
[ html.H1("Data Science to help your business", id="business"),
    dbc.Row(
        [ 
            dbc.Col(
                [
                    html.H2("Predictions"),
                    html.P(
                        """
                    There are few Machine Learning models presented there. You can make your choise to predict the 
                    next value based on your or pleloaded data.
                    You can put your data simply by dropping them into the dropping area or select the file. 
                    CSV and XLS supported. For demo purposes the only two columns supported. Real applicatin \
                    will suppost working with all the formats including databases.
                    """
                    ),
                    #dbc.Button("View details", color="secondary"),
                    dcc.Dropdown(
                        id = 'dDown1',
                        options=[
                            {'label': 'Linear Regression', 'value': 'lr'},
                            {'label': 'Supporting Vectors Regressor', 'value': 'svr'},
                            {'label': 'Decision Tree Regressor', 'value': 'dt'}
                        ],
                        value='lr'
                    ),  

                    dbc.Input(id="inp1", placeholder="Type something...", type="number", debounce=True),
                    html.Label('Predicred value'),
                    html.Div(id="text1"),
                ],
                md=4,
                ),
            dbc.Col(
                [
                    html.H2("Graph"),
                    html.Div(id='intermediate-value', style={'display': 'none'}, children=df.to_json(date_format='iso', orient='split')),

                    html.Div([
                       
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select Files')
                        ]),
                        style={
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                        },
                        # Allow multiple files to be uploaded
                        multiple=True
                    ),
                    
                    html.Div(id='output-data-upload', children = dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in df.columns],
                        data=df.to_dict('records'),
                        #editable=True
                    ))
                    ]),
                    

                    dcc.Graph(
                        id = 'graph',
                        figure={"data": [{'mode': 'markers', "x": df.x, "y": df.y}]}
                    ),
                ]
            ),
        ]
    )
],
className="mt-4",
)


    ############################ callbacks #############################
@app.callback([Output('output-data-upload', 'children'),
                Output('graph', 'figure'),
                Output('intermediate-value','children')],
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)['table'] for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        df = [
            parse_contents(c, n, d)['data'] for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        df = df[0]
        #print(df.iloc[:,1].values)
        fig = {'data':[{'mode': 'markers', 'x': df.iloc[:,0].values, 'y': df.iloc[:,1].values}]}
        return children, fig, df.to_json(date_format='iso', orient='split')
    else:
        raise dash.exceptions.PreventUpdate


@app.callback(Output('text1','children'),
            [Input('dDown1','value'),
            Input('inp1','value'),
            Input('intermediate-value','children')])
def prediction(mode, num, df):
    if num is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate
    try:
        df = pd.read_json(df, orient='split').to_numpy()
        X, y = df[:,0].reshape(-1,1), df[:,1]
        # linear regression
        if mode == 'lr':
            from sklearn import linear_model
            reg = linear_model.LinearRegression()
            reg.fit(X,y)
            
        elif mode == 'svr':
            from sklearn.svm import SVR
            reg = SVR()
            reg.fit(X,y)

        elif mode == 'dt':
            from sklearn.tree import DecisionTreeRegressor
            reg = DecisionTreeRegressor()
            reg.fit(X,y)

        predict = reg.predict([[num]])
        return predict

    except:
        return 'NA'

'''
@app.callback(
    Output('intermediate-value','children'),
    [Input('table', 'data'),
     Input('table', 'columns')])
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    return df.to_json(date_format='iso', orient='split')
'''