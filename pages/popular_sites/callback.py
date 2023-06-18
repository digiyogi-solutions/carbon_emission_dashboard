import pandas as pd
import plotly.express as px
from dash import Output, Input, State, html, register_page, dcc, ALL, MATCH
import dash
from datetime import datetime
import numpy as np

line_color_list = ['rgba(33, 150, 243, 1)',
                   'rgba(153, 0, 239, 1)',
                    'rgba(255, 105, 0, 1)',
                     'rgba(0, 188, 212, 1)',
                      'rgba(156, 39, 176, 1)',
                       'rgba(31, 119, 180, 1)',
                         'rgba(255, 193, 7, 1)', ]

fill_color_list = ['rgba(33, 150, 243, 0.7)',
                   'rgba(153, 0, 239, 0.7)',
                    'rgba(255, 105, 0, 0.7)',
                     'rgba(0, 188, 212, 0.7)',
                      'rgba(156, 39, 176, 0.7)',
                       'rgba(31, 119, 180, 0.7)',
                        'rgba(255, 193, 7, 0.7)' 
                        ]

@dash.callback(
    [Output({"type": "popular_sites_kpi_graph", "index": MATCH}, 'figure'),],
    Input('url', 'pathname')
)
def update_page(url):
        
        random_color_picker = np.random.choice(range(1,7),size = 1, replace=False)[0]

        area_df = pd.DataFrame({
            'x': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            'y': np.random.choice(range(100,1000), size=10, replace=False)
        }, index=[1990, 1997, 2003, 2009, 2014, 2016, 2017, 2018, 2019, 2020])

        fig = px.area(
            area_df,
            x="x", y="y",
            template='simple_white',
            log_y=True
        )

        fig.update_yaxes(visible=False),
        fig.update_xaxes(visible=False),
        # print(random_color_picker)
        # print(line_color_list[random_color_picker])
        # print(fill_color_list[random_color_picker])
        fig.update_traces(
            line={'color': str(line_color_list[random_color_picker])},
            # fillcolor='rgba(31, 119, 180, 0.4)',
            fillcolor=str(fill_color_list[random_color_picker]),
        ),
        fig.update_layout(
            margin={'t': 0, 'l': 0, 'b': 0, 'r': 0},
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            # border_radius=20,

        )

        kpi_val = f'42.5 MT'

        now = datetime.now()
        tot_inv_title = f'Carbon Emissions {now.strftime("%Y")}'

        # return kpi_val, fig, tot_inv_title
        return [fig]