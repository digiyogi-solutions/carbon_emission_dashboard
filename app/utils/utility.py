from dash_iconify import DashIconify
import urllib.parse

def get_icon(icon, height=16, color = "#c2c7d0", variant="outline"):
    return DashIconify(icon=icon, height=height, color=color)

def string_to_url_paramater(string):
    return urllib.parse.quote_plus(string)