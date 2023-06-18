import dash_mantine_components as dmc
import dash
from dash_iconify import DashIconify
from utils.utility import get_icon

def get_header():

    return dmc.Container([
                        dmc.Header(
                            height=80,
                            children=[
                                dmc.Group([
                                    dmc.MediaQuery([
                                        dmc.Button(
                                            DashIconify(icon="ci:hamburger-lg", width=30, height=30,color="#c2c7d0"),
                                            variant="subtle", 
                                            p=1,
                                            id='sidebar-button'
                                        ),
                                        ], smallerThan="md", styles={'display': 'none'}),
                                    dmc.MediaQuery([
                                        dmc.Button(
                                            DashIconify(icon="ci:hamburger-lg", width=30, height=30,color="#c2c7d0"),
                                            variant="subtle", 
                                            p=1,
                                            id='drawer-demo-button'
                                        ),
                                        ], largerThan="md", styles={'display': 'none'}),
                                    dmc.SimpleGrid(
                                        cols=2,
                                        spacing=600,
                                        breakpoints=[
                                            {"maxWidth": 1400, "cols": 2, "spacing": 350},
                                             {"maxWidth": 1250, "cols": 2, "spacing": 200},
                                            {"maxWidth": 1000, "cols": 2, "spacing": 150},
                                            {"maxWidth": 820, "cols": 2, "spacing": 100},
                                            {"maxWidth": 768, "cols": 2, "spacing": 50},
                                            {"maxWidth": 480, "cols": 2, "spacing": 30},
                                            ],
                                        children=[
                                                dmc.Text("Carbon Emission of the Web", weight=400, size="xl", color = "#FFFFFF", style={'margin':'0 0 0 10px'}),
                                                # html.Div(style={"width": "40vw", "display": "flex", "justifyContent": "flex-end"}),
                                                # dmc.Space(w="60%", style={"width": "auto", "display": "flex", "justifyContent": "flex-end"}),
                                                dmc.Group([
                                                    dmc.ActionIcon(get_icon(icon="clarity:settings-line", height=60, color="#FFFFFF", variant="outline")),
                                                    dmc.ActionIcon(get_icon(icon="solar:help-outline", height=60, color="#FFFFFF", variant="outline")),
                                                    dmc.ActionIcon(get_icon(icon="mdi:about-circle-outline", height=60, color="#FFFFFF", variant="outline")),
                                                ],
                                                # style={'padding':'0px'}
                                                )
                                                ,
                                        ],
                                        ),

                                ])
                            ],p='0px', style={"backgroundColor": "#607D8B",
                                               "alignItems": "center",
                                               "padding": "20px 20px",
                                            
                                               }),
                        dash.page_container, 
                        ],
                        id="page-container",
                        p=0,
                        fluid=True,
                        style={'background-color':'#f4f6f9',  'width':'100%', 'height':'100%', 'margin':'0'}
                        )
