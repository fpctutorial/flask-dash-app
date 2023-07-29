# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:18:17 2022

@author: User
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_daq as daq
import speedtest
from pythonping import ping

def run_speedtest():
    # Create a Speedtest object
    st = speedtest.Speedtest()
    
    # Get the best server
    print("Finding the best server...")
    st.get_best_server()
    
    # Perform the speed test
    print("Running the speed test...")
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    ping_ = st.results.ping 
    # Get server information
    server_info = st.results.server
    result = s.results
    ispinfo = result.client['isp']
    ipinfo = result.client['ip']
    ipcord_lat = result.client['lat']
    ipcord_long = result.client['lon']
    # Get the server's distance
    distance = server_info['d']
   
    
    # Get jitter
    # Run latency tests and calculate jitter
    latency_tests = []
    for _ in range(2):
        st.get_best_server()
        latency_tests.append(st.results.ping)
    
    latency = sum(latency_tests) / len(latency_tests)  # Calculate average latency
    jitter = sum(abs(latency_tests[i] - latency_tests[i-1]) for i in range(1, len(latency_tests))) / (len(latency_tests) - 1)
    
    # Get network type
    #network_type = detect_network_type()
    
    result = [download_speed,upload_speed, ping_,server_info['name'],server_info['sponsor'], server_info['latency'], jitter, ipcord_lat, ipcord_long, ispinfo,ipinfo,distance ]
    return result 
    # Print the results
    # print("Speed Test Results:")
    # print(f"Download Speed: {download_speed:.2f} Mbps")
    # print(f"Upload Speed: {upload_speed:.2f} Mbps")
    # print("Server Information:")
    # print(f"Server Name: {server_info['name']}")
    # print(f"Server Location: {server_info['sponsor']}")
    # print(f"Server Country: {server_info['country']}")
    # print(f"Server Latency: {server_info['latency']:.2f} ms")
    # print(f"Jitter: {jitter:.2f} ms")
    # print(f"Network Type: {network_type}")

# def detect_network_type():
#     # Perform a ping test to analyze the round-trip time (RTT)
#     ping_result = ping('www.google.com', count=5)
#     average_rtt = ping_result.rtt_avg_ms
    
#     # Determine the network type based on RTT values
#     if average_rtt <= 60:
#         network_type = "5G"
#     elif average_rtt <= 200:
#         network_type = "4G"
#     else:
#         network_type = "3G"
    
#     return network_type

dash.register_page(__name__, path='/', name='Recent Test Results') # '/' is home page


# Speedtest codes 

s = speedtest.Speedtest()

serv  = s.get_closest_servers()
items = []
for z in range(len(serv)):
    items.append(serv[z]['name'])
# create GUI components

# Create the dropdown menu
dropdown = dcc.Dropdown(
        options=[{'label': item, 'value': item} for item in items],
        value=None
    )

row_content = [
    dbc.Col(html.Div(children='Servers',
    style={'fontSize':23, 'textAlign': 'center'}), width=2),
    dbc.Col(html.Div(dropdown), width=2),
]
row_content2 = [
    dbc.Col(html.Div(children='ISP Info: ',
    style={'fontSize':24, 'textAlign': 'center'}), width=2),
    dbc.Col(html.Div(children = '--', id="isp-info"), width=2)
]

row_content3 = [
    dbc.Col(html.Div(children='Coordinates: ',
    style={'fontSize':23, 'textAlign': 'center'}), width=2),
    dbc.Col(html.Div(children = '--', id="coordinates"), width=2),
]


# row_content4 = [
#     dbc.Col(html.Div(children='Network Type: ',
#     style={'fontSize':23, 'textAlign': 'center'}), width=2),
#     dbc.Col(html.Div(children = '--', id="network"), width=2),
# ]

row_content5 = [
    dbc.Col(html.Div(children='Distance: ',
    style={'fontSize':23, 'textAlign': 'center'}), width=2),
    dbc.Col(html.Div(children = '--', id="dist", style={'font-size': '24px'}), width=2),
]


# Create Layout for the home page

layout = html.Div(
    [
        
        # First row   
        dbc.Row([
            # First Row, col one 
            dbc.Col([
                daq.Gauge(
                size = 200,
                showCurrentValue=True,
                id='my-gauge-1',
                color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                label="Download (Mbps)",
                max=100,
                min=0,
                style={'fontSize': '35px'},
                value=0)
                
                
                ]),
            # First Row, col two 
            dbc.Col([
                daq.Gauge(
                    size = 200,
                    showCurrentValue=True,
                    id='my-gauge-2',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Upload (Mbps)",
                    max=100,
                    min=0,
                    value=0)
                
                ])
        ]),
        # second row 
         
        dbc.Row([
            # Second Row, col one 
            dbc.Col([
                daq.Gauge(
                size = 200,
                showCurrentValue=True,
                id='my-gauge-3',
                color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                label="Ping (ms)",
                max=200,
                min=0,
                value=0)
                
                ]),
            # Second Row, col two 
            dbc.Col([
                daq.Gauge(
                    size = 200,
                    showCurrentValue=True,
                    id='my-gauge-4',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Jitter (ms)", 
                    max=50,
                    min=0,
                    value=0)
                
                ])
            
        ]),
        # Thrid Row 
        # dbc.Row([
        #     dbc.Card(
        #         dbc.CardBody([
        #             html.H4(children='Speed Test',
        #             style={'fontSize':25, 'textAlign': 'center'}),
        #             ]),
                
        #         )
        # ]),

        dbc.Row([
            dbc.Button("Start", id="start-button", className="me-1", n_clicks=0)
            ]),
        # fourth row 
        dbc.Row(
            row_content,
            justify="center"
        ),
        # fifth row 
        dbc.Row(
            row_content2,
            justify="center"
            ),
        
        # sixth row 
        dbc.Row(row_content3,
                justify="center"),
        
        # seventh row 
        # dbc.Row(row_content4,
        #         justify="center"),
        # eight row 
        dbc.Row(row_content5,
                justify="center"),
        # night row 
        #dbc.Row([
        #    dbc.Button("Start", id="start-button", className="me-1", n_clicks=0)
        #    ]),
        
        # night row 
        
        
    ]
)



@callback(
    Output("isp-info", "children"),
    Output("coordinates", "children"),
    Output('my-gauge-1', 'value'),
    Output('my-gauge-2', 'value'),
    Output("my-gauge-3", 'value'),
    Output("my-gauge-4", 'value'),
    Output("dist", "children"),
    
    [Input("start-button", "n_clicks")]
)
def on_button_click(n):
    
    if n is None:
        raise dash.exceptions.PreventUpdate
    else:
        
        re = run_speedtest()
        
        value_3 = re[2]
        #ispinfo = result.client['isp']
        ispinfo = re[9] 
        #ipinfo = result.client['ip']
        ipinfo = re[10]
        #ipcord_lat = result.client['lat']
        ipcord_lat = re[7]
        #ipcord_long = result.client['lon']
        ipcord_long = re[8]
        #result = [download_speed,upload_speed,server_info['name'],server_info['sponsor'], server_info['latency'], jitter,network_type, ipcord_lat, ipcord_long, ispinfo ]
        
        value2 = re[1]
        value = re [0]
        jitter = re[6]
        #network = re[7]
        dist = re[11]
        #value2 = uploadspeed
        #value = downloadspeed
        return f"{ipinfo} {ispinfo}", f"{ipcord_lat},  {ipcord_long}", value, value2, value_3, jitter, dist


