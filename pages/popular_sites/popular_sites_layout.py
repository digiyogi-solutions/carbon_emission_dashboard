import dash_mantine_components as dmc
import dash
from dash import Output, Input, State, html, register_page
from pages.home import card_generator
from pages.popular_sites.carbon_emission_api import WebsiteCarbonEmissionAPI


register_page(__name__, path="/popular_sites", icon="fa-solid:home")

from dash.exceptions import PreventUpdate

style = {
    # "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
    "padding": "20px",
    "margin": "20px"

}

facebook_carbon_emission_api = WebsiteCarbonEmissionAPI('www.facebook.com')
amazon_carbon_emission_api = WebsiteCarbonEmissionAPI('www.amazon.com')
netflix_carbon_emission_api = WebsiteCarbonEmissionAPI('www.netflix.com')
instagram_carbon_emission_api = WebsiteCarbonEmissionAPI('www.instagram.com')
twitter_carbon_emission_api = WebsiteCarbonEmissionAPI('www.twitter.com')
linkedin_carbon_emission_api = WebsiteCarbonEmissionAPI('www.linkedin.com')


def get_icon_color(green_flag):
    if green_flag == True:
        return "#00D084"
    elif green_flag == False:
        return "#D32F2F"
    else:
        return "grey"
    
def get_icon_text(green_flag):
    if green_flag == True:
        return "Uses green energy"
    elif green_flag == False:
        return "Does not use green energy"
    else:
        return "Unknown"

layout = dmc.Grid(
    children=[
        dmc.Col([
            facebook_carbon_emission_api.get_carbon_emission_data(),  
            html.Div(
                card_generator.get_card(
                    card_title="Facebook",
                    card_icon_name="logos:facebook",
                    main_kpi_value=facebook_carbon_emission_api.co2_transferred_grams,
                    main_kpi_unit="g CO2",
                    main_kpi_unit_desc="per page load",
                    icon_name="ri:leaf-fill",
                    icon_color=get_icon_color(facebook_carbon_emission_api.get_green_flag()),
                    icon_text = get_icon_text(facebook_carbon_emission_api.get_green_flag()),
                    graph_name='kpi_card_graph'
                ),style=style)
        ], span=3),
        
        dmc.Col([
            amazon_carbon_emission_api.get_carbon_emission_data(),
            html.Div(
                card_generator.get_card(
                    card_title="Amazon",
                    card_icon_name="grommet-icons:amazon", 
                    card_icon_color = "#FFB74D",
                    main_kpi_value=amazon_carbon_emission_api.co2_transferred_grams,
                    main_kpi_unit="g CO2",
                    main_kpi_unit_desc="per page load",
                    icon_name="ri:leaf-fill",
                    icon_color=get_icon_color(amazon_carbon_emission_api.get_green_flag()),
                    icon_text = get_icon_text(amazon_carbon_emission_api.get_green_flag()),
                    graph_name='kpi_card_graph'
                ), style=style)
            ], span=3),
        
        dmc.Col([
            netflix_carbon_emission_api.get_carbon_emission_data(),
            html.Div(
                card_generator.get_card(
                    card_title="Netflix",
                    card_icon_name="simple-icons:netflix",
                    card_icon_color = "#d32f2f",
                    main_kpi_value=netflix_carbon_emission_api.co2_transferred_grams,
                    main_kpi_unit="g CO2",
                    main_kpi_unit_desc="per page load",
                    icon_name="ri:leaf-fill",
                    icon_color=get_icon_color(netflix_carbon_emission_api.get_green_flag()),
                    icon_text = get_icon_text(netflix_carbon_emission_api.get_green_flag()),
                    graph_name='kpi_card_graph'
                ), style=style)
            ], span=3),

        dmc.Col([
            instagram_carbon_emission_api.get_carbon_emission_data(),
            html.Div(
                card_generator.get_card(
                    card_title="Instagram",
                    card_icon_name="skill-icons:instagram",
                    # card_icon_color = "#d32f2f",
                    main_kpi_value=instagram_carbon_emission_api.co2_transferred_grams,
                    main_kpi_unit="g CO2",
                    main_kpi_unit_desc="per page load",
                    icon_name="ri:leaf-fill",
                    icon_color=get_icon_color(instagram_carbon_emission_api.get_green_flag()),
                    icon_text = get_icon_text(instagram_carbon_emission_api.get_green_flag()),
                    graph_name='kpi_card_graph'
                ), style=style)
            ], span=3),
        
        dmc.Col([
            twitter_carbon_emission_api.get_carbon_emission_data(),
            html.Div(
                card_generator.get_card(
                    card_title="Twitter",
                    card_icon_name="logos:twitter",
                    # card_icon_color = "#d32f2f",
                    main_kpi_value=twitter_carbon_emission_api.co2_transferred_grams,
                    main_kpi_unit="g CO2",
                    main_kpi_unit_desc="per page load",
                    icon_name="ri:leaf-fill",
                    icon_color=get_icon_color(twitter_carbon_emission_api.get_green_flag()),
                    icon_text = get_icon_text(twitter_carbon_emission_api.get_green_flag()),
                    graph_name='kpi_card_graph'
                ), style=style)
            ], span=3),
        
        dmc.Col([
            linkedin_carbon_emission_api.get_carbon_emission_data(),
            html.Div(
                card_generator.get_card(
                    card_title="LinkedIn",
                    card_icon_name="devicon:linkedin",
                    # card_icon_color = "#d32f2f",
                    main_kpi_value=linkedin_carbon_emission_api.co2_transferred_grams,
                    main_kpi_unit="g CO2",
                    main_kpi_unit_desc="per page load",
                    icon_name="ri:leaf-fill",
                    icon_color=get_icon_color(linkedin_carbon_emission_api.get_green_flag()),
                    icon_text = get_icon_text(linkedin_carbon_emission_api.get_green_flag()),
                    graph_name='kpi_card_graph'
                ), style=style)
            ], span=3),
    ],
    gutter="xs",
    style={"backgroundColor": "#CFD8DC", 'height':'90vh'}
)
