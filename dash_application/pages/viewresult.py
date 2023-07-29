# -*- coding: utf-8 -*-
"""

Created on Thu Dec  10 11:48:45 2021
#   - Code for dashbaord for the oil and gas pipeline parameters
@author: User
"""

import dash
import sqlite3
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash import html, dcc, Output, Input, callback, State
from dash.exceptions import PreventUpdate
import pandas as pd

from dash import dash_table

# Connect to the SQLite database
conn = sqlite3.connect('data2.db')

# Execute the SELECT query
query = "SELECT * FROM data_collected"
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()

# Get column names
columns = [col[0] for col in cursor.description]

# Create DataFrame from fetched rows
data = pd.DataFrame(rows, columns=columns)


dash.register_page(__name__, name='View Result')

# Create Page Layout
layout = html.Div([
    # create row one
    dbc.Row([
       # Define app layout

   html.H4('Data from the Database:'),
   html.Button("Download CSV", id="btn_csv"),
        dcc.Download(id="download-dataframe-csv"),
    dash_table.DataTable(
        data=data.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in data.columns],
        style_table={'overflowX': 'scroll'},
        style_data={'whiteSpace': 'normal', 'height': 'auto'}
    )
    
    #
    ])
    
    ]) 
   
# Close the database connection
cursor.close()
conn.close()
@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(data.to_csv, "nccspeed.csv")