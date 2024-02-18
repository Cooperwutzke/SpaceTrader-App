# Cooper Wutzke
# JSON Viewer for basic API calls

import tkinter as tk
from tkinter import ttk
import requests
import json

# Function to send HTTP request and display the response
def send_request():
    url = url_entry.get()
    method = request_type.get()
    try:
        if method == "GET":
            response = requests.get(url)
        else:
            response = requests.post(url)
        response_json = response.json()
        display_response(response_json)
    except Exception as e:
        response_tree.insert('', 'end', text="Error", values=(str(e),))

# Function to display JSON response in the treeview
def display_response(response_json, parent=''):
    for key, value in response_json.items():
        if isinstance(value, dict):
            node = response_tree.insert(parent, 'end', text=key, open=True)
            display_response(value, node)
        elif isinstance(value, list):
            node = response_tree.insert(parent, 'end', text=key, open=True)
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    item_node = response_tree.insert(node, 'end', text=f"{key}[{i}]", open=True)
                    display_response(item, item_node)
                else:
                    response_tree.insert(node, 'end', text=f"{key}[{i}]", values=(item,))
        else:
            response_tree.insert(parent, 'end', text=key, values=(value,))

# Initialize main application window
app = tk.Tk()
app.title("HTTP Request GUI")

# URL entry
url_frame = ttk.Frame(app)
url_frame.pack(fill='x', padx=5, pady=5)
url_label = ttk.Label(url_frame, text="URL:")
url_label.pack(side='left')
url_entry = ttk.Entry(url_frame)
url_entry.pack(fill='x', expand=True)

# Request type selection
request_type = tk.StringVar(value="GET")
request_type_frame = ttk.Frame(app)
request_type_frame.pack(fill='x', padx=5, pady=5)
get_button = ttk.Radiobutton(request_type_frame, text="GET", variable=request_type, value="GET")
get_button.pack(side='left')
post_button = ttk.Radiobutton(request_type_frame, text="POST", variable=request_type, value="POST")
post_button.pack(side='left')

# Send button
send_button = ttk.Button(app, text="Send Request", command=send_request)
send_button.pack(fill='x', padx=5, pady=5)

# Response display (treeview)
response_frame = ttk.Frame(app)
response_frame.pack(fill='both', expand=True, padx=5, pady=5)
response_tree = ttk.Treeview(response_frame, columns=('Value',), show="tree")
response_tree.pack(fill='both', expand=True)

app.mainloop()