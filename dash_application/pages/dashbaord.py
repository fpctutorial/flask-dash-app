# -*- coding: utf-8 -*-
"""

Created on Thu Dec  10 11:48:45 2021
#   - Code for dashbaord for the oil and gas pipeline parameters
@author: User
"""

import dash
import sqlite3
from geopy.distance import distance
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash import html, dcc, Output, Input, callback
from dash.exceptions import PreventUpdate
import pandas as pd



# analyse data
def analyse_data(ser_provider_val, parameter):
    # Connect to the SQLite database
    conn = sqlite3.connect('data2.db')

    # Execute the SELECT query
    service_provider_value = ser_provider_val
    parameter = parameter
    query = "SELECT  latitude, longitude, upload, download, latency, jitter FROM data_collected WHERE service_provider = ?"
        
    cursor = conn.cursor()
    cursor.execute(query, (service_provider_value,))
    rows = cursor.fetchall()

    # Convert the rows to a DataFrame
    data = pd.DataFrame(rows, columns=['latitude','longitude','upload', 'download', 'latency', 'jitter'])

    # Remove commas from the values
    data['upload'] = data['upload'].str.replace(',', '').astype(float)
    data['download'] = data['download'].str.replace(',', '').astype(float)
    data['latency'] = data['latency'].str.replace(',', '').astype(float)
    data['jitter'] = data['jitter'].str.replace(',', '').astype(float)
    data['latitude'] = data['latitude'].str.replace(',', '').astype(float)
    data['longitude'] = data['longitude'].str.replace(',', '').astype(float)

    # Calculate the average values
    average_values = data.mean()

    # Get the last values
    last_values = data.tail(1).squeeze()
    
    # Extract latitude and longitude as a separate dataframe
    coordinates = data[['latitude', 'longitude']]


    # Get the last values
    target_latitude = data.tail(1).squeeze()['latitude']
    #target_latitude = 4.8805657
    #target_longitude = 6.9730933
    target_longitude = data.tail(1).squeeze()['latitude']
    

    upload_fig = go.Figure()
    if parameter == 'upload':
        title = 'Cummulative Upload Speed Comparison'
        yaxis = 'Mbps'
        upload_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['upload'], last_values['upload']]))
    elif parameter == 'download':
        yaxis = 'Mbps'
        upload_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['download'], last_values['download']]))
        title = 'Cummulative Download Speed Comparison'
    elif parameter == 'latency':
        upload_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['latency'], last_values['latency']]))
        title = 'Cummulative Latency Speed Comparison'
        yaxis = 'ms'
    elif parameter == 'jitter':
        upload_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['jitter'], last_values['jitter']]))
        title = 'Cummulative Jitter Speed Comparison'
        yaxis = 'ms'
        
    upload_fig.update_layout(
        title=title,
        xaxis=dict(title='Metric'),
        yaxis=dict(title=yaxis),
        height=400
    )
    
    local_fig = go.Figure()
    # Target location

    target_lat = data.tail(1).squeeze()['latitude']
    #target_latitude = 4.8805657
    #target_longitude = 6.9730933
    target_lon = data.tail(1).squeeze()['longitude']
    # Select locations within 1 kilometer
    selected_locations = []
    for index, row in coordinates.iterrows():
        loc_lat = row['latitude']
        loc_lon = row['longitude']
        loc = (loc_lat, loc_lon)
        target_loc = (target_lat, target_lon)
        dist = distance(target_loc, loc).km
        #print(dist)
        if dist <= .05:
            selected_locations.append((loc_lat, loc_lon))
            #print(selected_locations)



    # Create a new DataFrame with selected locations
    selected_df = pd.DataFrame(selected_locations, columns=['Latitude', 'Longitude'])
    print(selected_df)


    # Select rows where latitude and longitude match the given values
    selected_rows = data.loc[(data['latitude'].isin(selected_df['Latitude'])) & (data['longitude'].isin(selected_df['Longitude']))]
    # Calculate the average values
    average_values = selected_rows.mean()

    # Get the last values
    last_values = selected_rows.tail(1).squeeze()
    
    if parameter == 'upload':
        title = 'Upload Speed Comparison (Less than 50 meters)'
        yaxis = 'Mbps'
        local_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['upload'], last_values['upload']]))
    elif parameter == 'download':
        yaxis = 'Mbps'
        local_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['download'], last_values['download']]))
        title = 'Download Speed Comparison (Less than 50 meters)'
    elif parameter == 'latency':
        local_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['latency'], last_values['latency']]))
        title = 'Latency Speed Comparison (Less than 50 meters)'
        yaxis = 'ms'
    elif parameter == 'jitter':
        local_fig.add_trace(go.Bar(x=['Average', 'Last'], y=[average_values['jitter'], last_values['jitter']]))
        title = 'Jitter Speed Comparison (Less than 50 meters)'
        yaxis = 'ms'
    
    local_fig.update_layout(
        title=title,
        xaxis=dict(title='Metric'),
        yaxis=dict(title=yaxis),
        height=400
    )
    # Close the database connection
    cursor.close()
    conn.close()

    return upload_fig,local_fig 


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
),
button = dbc.Button("View Analysis", id="analyis-btn", className="me-1",n_clicks=0), 

dash.register_page(__name__, name='Dashboard')

# Create Page Layout
layout = html.Div([
    # create row one
    dbc.Row([
        dbc.Col(html.Div(dropdown_network), width=6, lg=3),
        dbc.Col(html.Div(dropdown_para), width=6, lg=3),
        dbc.Col(html.Div(button), width=6, lg=3),
        
        #form
        ],justify="center", ),
    # create row two
   
       dbc.Row([
           dbc.Col([dcc.Graph(id='up_load_fig', figure={}),
           dbc.Col([dcc.Graph(id='location_fig', figure={})])
                    
                    ])
           ])
    ])
   

# Define the callback function to view analysis when the button is clicked

@callback(
    Output('up_load_fig', 'figure'),
    Output('location_fig', 'figure'),
    [Input('analyis-btn', 'n_clicks')],
    [Input('dropdown-menu', 'value')],
    [Input('para-menu', 'value')]
)

def view_analysis(n_clicks,drop_menu, para_menu):
    if n_clicks > 0:
        if drop_menu and para_menu:
            
            
            if drop_menu == 'MTN Nigeria' and para_menu == 'Upload':
                upl_fig= analyse_data('MTN NIGERIA Communication limited', 'upload')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'MTN Nigeria' and para_menu == 'Download':
                upl_fig = analyse_data('MTN NIGERIA Communication limited', 'download')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'MTN Nigeria' and para_menu == 'Latency':
                upl_fig = analyse_data('MTN NIGERIA Communication limited', 'latency')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'MTN Nigeria' and para_menu == 'Jitter':
                upl_fig = analyse_data('MTN NIGERIA Communication limited', 'jitter')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'Glo Nigeria' and para_menu == 'Upload':
                upl_fig = analyse_data('Globacom Limited', 'upload')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'Glo Nigeria' and para_menu == 'Download':
                upl_fig = analyse_data('Globacom Limited', 'download')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'Glo Nigeria' and para_menu == 'Latency':
                upl_fig = analyse_data('Globacom Limited', 'latency')
                return upl_fig[0]
            elif drop_menu == 'Glo Nigeria' and para_menu == 'Jitter':
                upl_fig = analyse_data('Globacom Limited', 'jitter')
                return upl_fig[0], upl_fig[1]
            
            elif drop_menu == 'Airtel Nigeria' and para_menu == 'Upload':
                upl_fig = analyse_data('Airtel Networks Limited', 'upload')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'Airtel Nigeria' and para_menu == 'Download':
                upl_fig = analyse_data('Airtel Networks Limited', 'download')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'Airtel Nigeria' and para_menu == 'Latency':
                upl_fig = analyse_data('Airtel Networks Limited', 'latency')
                return upl_fig[0], upl_fig[1]
            elif drop_menu == 'Airtel Nigeria' and para_menu == 'Jitter':
                upl_fig = analyse_data('Airtel Networks Limited', 'jitter')
                return upl_fig[0], upl_fig[1]
            
        
    else:
        
        # Create upload speed figure
        raise PreventUpdate




    
    
   