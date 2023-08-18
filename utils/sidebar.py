import dash_mantine_components as dmc
from dash import html
from utils.utility import get_icon 


def get_sidebar():
    return dmc.Navbar(
                    p="md",
                    fixed=False,
                    width={"base": 300},
                    hidden=True,
                    hiddenBreakpoint='md',
                    position='right',
                    height='100vh',
                    id='sidebar',
                    children=[
                        html.Div(
                            [
                                dmc.NavLink(
                                        label="Home",
                                        icon=get_icon(icon="bi:house-door-fill"),
                                        href="/",
                                    ),
                                    dmc.NavLink(
                                        opened=False,
                                        label="Popular sites",
                                        description="Carbon Emission Profile",
                                        href="/popular_sites",
                                        icon=get_icon(icon="tabler:gauge"),
                                        rightSection=get_icon(icon="tabler-chevron-right"),
                                        children=[
                                            dmc.NavLink(label="Site summary", href="/popular_sites/site_summary/", icon=get_icon(icon="mdi:facebook")),
                                            dmc.NavLink(label="Geography analysis", icon=get_icon(icon="mdi:twitter")),
                                            dmc.NavLink(label="Tabular view", icon=get_icon(icon="mdi:instagram")),
                                            # dmc.NavLink(label="LinkedIn", icon=get_icon(icon="mdi:linkedin")),
                                            # dmc.NavLink(label="YouTube", icon=get_icon(icon="mdi:youtube")),

                                        ]
                                ),
                                dmc.NavLink(
                                    label="About",
                                    icon=get_icon(icon="tabler:circle-off"),
                                    # disabled=True,
                                ),
                                dmc.NavLink(
                                    label="Contact us",
                                    icon=get_icon(icon="tabler:gauge"),
                                    # description="Additional information",
                                    # icon=dmc.Badge(
                                    #     "3", size="xs", variant="filled", color="red", w=16, h=16, p=0
                                    # ),
                                ),
                                # dmc.NavLink(
                                #     label="Active subtle",
                                #     icon=get_icon(icon="tabler:activity"),
                                #     rightSection=get_icon(icon="tabler-chevron-right"),
                                #     variant="subtle",
                                #     active=True,
                                # ),
                            ],
                            style={'white-space': 'nowrap'},
                        )],style={'overflow':'hidden', 'transition': 'width 0.3s ease-in-out', 'background-color':'#343a40'}
                    )
 
