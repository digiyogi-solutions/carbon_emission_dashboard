import dash_mantine_components as dmc
from dash import html
from utils.utility import get_icon 


def get_drawer():
    return dmc.Drawer(
                        title="Company Name",
                        id="drawer-simple",
                        padding="md",
                        zIndex=10000,
                        size=300,
                        
                        overlayOpacity=0.1,
                        children=[
                            html.Div(
                                [
                                    dmc.NavLink(
                                        label="Home",
                                        icon=get_icon(icon="bi:house-door-fill"),
                                    ),
                                    dmc.NavLink(
                                        opened=False,
                                        label="Popular sites",
                                        icon=get_icon(icon="tabler:gauge"),
                                        rightSection=get_icon(icon="tabler-chevron-right"),
                                    ),
                                    dmc.NavLink(
                                        label="Disabled",
                                        icon=get_icon(icon="tabler:circle-off"),
                                        disabled=True,
                                    ),
                                    dmc.NavLink(
                                        label="With description",
                                        description="Additional information",
                                        icon=dmc.Badge(
                                            "3", size="xs", variant="filled", color="red", w=16, h=16, p=0
                                        ),
                                        style={
                                            'body':{'overflow':'hidden'}
                                        }
                                    ),
                                    dmc.NavLink(
                                        label="Active subtle",
                                        icon=get_icon(icon="tabler:activity"),
                                        rightSection=get_icon(icon="tabler-chevron-right"),
                                        variant="subtle",
                                        active=True,
                                    ),
                                ],
                                style={'white-space': 'nowrap'},
                            )
                        ], style={'background-color':''}, styles={'drawer':{'background-color':'#343a40'}})
