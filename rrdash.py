import sqlite3
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import socket
import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from appJar import gui
import webbrowser

def openbrowser(btn):
    print(f"Opening server in browser")
    host_name = socket.gethostbyname(socket.gethostname())
    port_number = 5151
    webbrowser.open(f"http://{host_name}:{port_number}/server/")

def server(btn): 
    host_name = socket.gethostbyname(socket.gethostname())
    port_number = 5151
    # Create an HTTP server
    httpd = HTTPServer((host_name, port_number), SimpleHTTPRequestHandler)
    # Start the server in a separate thread
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.start()
    app.setLabel("SL", f"Server: http://{host_name}:{port_number}")
    app.setLabel("SS", "Online")
    print("Server started at http://{}:{}/server/".format(*httpd.socket.getsockname()))

# Connect to the SQLite database
conn = sqlite3.connect('acrecords.db')
df = pd.read_sql_query('SELECT * FROM records', conn)
table_trace = go.Table(
    header=dict(values=list(df.columns)),
    cells=dict(values=[df[col] for col in df.columns])
)

def update():
    fig = make_subplots(rows=5, cols=1)
    fig.add_trace(table_trace)
    fig.update_layout(title=f'Records')
    # Save the Plotly figure to an HTML file
    fig.write_html("server/index.html")


app=gui("RRDASH","400x200")
app.setBg("White")

app.startLabelFrame("Server Commands",1,1)
app.addButton("Server",server)
app.addButton("Open Browser",openbrowser)
app.addButton("Update",update)
app.stopLabelFrame()

app.startLabelFrame("Server Status",1,2)
app.addLabel("SL")
app.addLabel("SS")
app.stopLabelFrame()
app.go()

