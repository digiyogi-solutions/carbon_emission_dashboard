import dash_mantine_components as dmc
import dash
from dash import Output, Input, State, html, register_page
from pages.home import card_generator
from pages.popular_sites.carbon_emission_api import WebsiteCarbonEmissionAPI


register_page(__name__, path="/popular_sites/site_summary/", icon="fa-solid:home")

from dash.exceptions import PreventUpdate

layout = dmc.Text("Site Summary")