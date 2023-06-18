import dash_mantine_components as dmc
import dash
from dash import Output, Input, State, html, register_page
from dash_iconify import DashIconify
from pages.home import card_generator


register_page(__name__, path="/", icon="fa-solid:home")

from dash.exceptions import PreventUpdate

def get_icon(icon):
    return DashIconify(icon=icon, height=16, color="#c2c7d0")

style = {
    # "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
    "padding": "20px",
    "margin": "20px"

}

layout = dmc.Grid(
    children=[
        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Carbon Emissions",
                main_kpi_value="$10.5 M",
                icon_name="icons8:up-round",
                icon_color="#00D084",
                icon_text="5.5% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),
        
        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Total Investment",
                main_kpi_value="8.5T Kg",
                icon_name="icons8:down-round",
                icon_color="#D32F2F",
                icon_text="15% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),
        
        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Total Investment",
                main_kpi_value="$ 1.5 M",
                icon_name="icons8:up-round",
                icon_color="#00D084",
                icon_text="5.5% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),
        
        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Total Investment",
                main_kpi_value="$ 1.5 M",
                icon_name="icons8:up-round",
                icon_color="#00D084",
                icon_text="5.5% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),


        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Carbon Emissions",
                main_kpi_value="$10.5 M",
                icon_name="icons8:up-round",
                icon_color="#00D084",
                icon_text="5.5% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),
        
        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Total Investment",
                main_kpi_value="8.5T Kg",
                icon_name="icons8:down-round",
                icon_color="#D32F2F",
                icon_text="15% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),
        
        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Total Investment",
                main_kpi_value="$ 1.5 M",
                icon_name="icons8:up-round",
                icon_color="#00D084",
                icon_text="5.5% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),
        
        dmc.Col(html.Div(
            card_generator.get_card(
                card_title="Total Investment",
                main_kpi_value="$ 1.5 M",
                icon_name="icons8:up-round",
                icon_color="#00D084",
                icon_text="5.5% vs Last Year",
                graph_name='kpi_card_graph'
        ), style=style), span=3),
        
    ],
    gutter="xs",
    grow=True,
    style={"backgroundColor": "#CFD8DC", 'height':'90vh'}
)


# dmc.MantineProvider(
#         theme={
#             'fontFamily': '"Inter", sans-serif',
#             "components": {
#                 "NavLink":{'styles':{'label':{'color':'#c2c7d0'}}}
#                 },
#             },
#         children=[
#             dmc.Container([
#                 sidebar.get_sidebar(),
#                 drawer.get_drawer(),
#                 header.get_header(),

#             ],
#              size='100%', p=0,m=0, style={'display':'flex'})
# ])



