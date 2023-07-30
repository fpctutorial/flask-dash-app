# -*- coding: utf-8 -*-
"""

Created on Thu Dec  10 15:48:45 2021
#   code to create a submission form for setting the threshold for parameters

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
from geopy.distance import distance



# create a function to display map 
def plot_map(ser_provider):
    # Connect to the SQLite database
    conn = sqlite3.connect('data2.db')

    # Execute the SELECT query
    #service_provider_value = 'MTN NIGERIA Communication limited'
    service_provider_value = ser_provider
    query = "SELECT latitude, longitude, upload FROM data_collected WHERE service_provider = ?"
    cursor = conn.cursor()
    cursor.execute(query, (service_provider_value,))
    rows = cursor.fetchall()

    # Convert the rows to a DataFrame
    data = pd.DataFrame(rows, columns=['latitude', 'longitude', 'upload'])

    # Convert latitude and longitude to float
    data['latitude'] = data['latitude'].astype(float)
    data['longitude'] = data['longitude'].astype(float)

    # Create scatter mapbox trace
    trace = go.Scattermapbox(
        lat=data['latitude'],
        lon=data['longitude'],
        mode='markers',
        marker=dict(
            
            size=10,
            color='blue',
            opacity=0.7
        ),
        text='Latitude: ' + data['latitude'].astype(str) + '<br>Longitude: ' + data['longitude'].astype(str) +
             '<br>Upload Speed: ' + data['upload'].astype(str)
    )

    if service_provider_value == 'MTN NIGERIA Communication limited':
       title = 'MTN Nigeria'
    elif service_provider_value == 'Globacom Limited':
       title = 'Globacom Limited'
    elif service_provider_value == 'Airtel Networks Limited':
       title = 'Airtel Nigeria'
        
    # Create map layout
    layout = go.Layout(
    
        mapbox=dict(
            style='open-street-map',
            #style='mapbox://styles/mapbox/light-v10',
            #accesstoken='YOUR_MAPBOX_ACCESS_TOKEN',
            #center=dict(lat=data['latitude'].mean(), lon=data['longitude'].mean()),
            center=dict(lat=9.081999, lon=8.675277),
            zoom=5),
        
                   
        title = title,
        height=650
    )

    # Create map figure
    fig = go.Figure(data=[trace], layout=layout)
    
    return fig

# Specify the desired columns to select
network_columns = ['MTN Nigeria', 'Glo Nigeria', 'Airtel Nigeria']
# Create a dropdown menu for network
dropdown_network = dcc.Dropdown(
    id='dropdown-menu',
    options=[
        {'label':  column, 'value': column}
        for column in network_columns
    ],
    placeholder='Select Network',
    multi=False,
),

# Specify the desired columns to select
metrics_columns = ['Upload', 'Download', 'Latency', 'Jitter']

# Create a dropdown menu for parameters to select
dropdown_para = dcc.Dropdown(
    id='para-menu',
    options=[
        {'label':  column, 'value': column}
        for column in metrics_columns
    ],
    placeholder='Select',
    multi=False,
    style={'font-size': '18px'},  # Apply font size to options
    #option_style={'font-size': '18px'}  # Apply font size to labels
),
button = dbc.Button("View Map", id="display-map-btn", className="me-1",n_clicks=0), 

dash.register_page(__name__, name='View Map')

layout = html.Div(
    [
    # Row one
    dbc.Row([
        dbc.Col(html.Div(dropdown_network), width=6, lg=3),
        dbc.Col(html.Div(dropdown_para), width=6, lg=3),
        dbc.Col(html.Div(button), width=6, lg=3),
        
        #form
        ],justify="center", ),
    
    # row two 
       dbc.Row([
           dbc.Col(dcc.Graph(id='map-graph', figure={}))
                      
           ]) 
    ]
)

# Define the callback function to update the map when the button is clicked
@callback(
    Output('map-graph', 'figure'),
    [Input('display-map-btn', 'n_clicks')],
    [Input('dropdown-menu', 'value')],
    [Input('para-menu', 'value')]
)
def update_map(n_clicks,drop_menu, para_menu):
    
    if n_clicks > 0:
        if drop_menu and para_menu:
            if drop_menu == 'MTN Nigeria':
                fig = plot_map('MTN NIGERIA Communication limited')
                return fig
            if drop_menu == 'Glo Nigeria':
                fig = plot_map('Globacom Limited')
                return fig
            if drop_menu == 'Airtel Nigeria':
                fig = plot_map('Airtel Networks Limited')
                return fig
        
        # Don't update the map if the button hasn't been clicked yet
            #select_long_lat()
            
        
    else:
        raise PreventUpdate


# Close the database connection


# Close the database connection
