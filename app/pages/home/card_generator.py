import dash_bootstrap_components as dbc
import dash

from datetime import datetime
from utils.utility import get_icon 

import friendlywords as fw




import numpy as np
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

def get_card(card_title="loading",
             card_icon_name='ri:leaf-fill', 
             card_icon_color='#00D084',
             main_kpi_value=0, 
             main_kpi_unit = '', 
             main_kpi_unit_desc = '',
             icon_name='ri:leaf-fill', 
             icon_color='#00D084', 
             icon_text='Uses green energy', 
             graph_name = None):

 # generate a random graph name if not provided
    if graph_name is None:
        graph_name =  fw.generate('po', separator='-')
    else:
        graph_name = graph_name + str(np.random.randint(1, 100000))

        
    @dash.callback(
        [Output({"type": graph_name, "index": MATCH}, 'figure'),],
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
                template='none',
                log_y=True
            )

            fig.update_yaxes(visible=False),
            fig.update_xaxes(visible=False),
        
            fig.update_traces(
                line={'color': str(line_color_list[random_color_picker])},
                fillcolor=str(fill_color_list[random_color_picker]),
            ),
            fig.update_layout(
                margin={'t': 0, 'l': 0, 'b': 0, 'r': 0},
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                template='none',

            )
            return [fig]

   

    return dbc.Card([
                dbc.CardBody([
                        # html.P([
                        #     html.I(get_icon(icon=icon_name, height = 25, color=icon_color)),
                        #     html.H6(card_title + f' {datetime.now().strftime("%Y")}', className="card-title up"),
                        # ]),
                        html.P([
                                html.I(get_icon(icon=card_icon_name, height = 60, color=card_icon_color)),
                                # html.Span(' ' + card_title + f' {datetime.now().strftime("%Y")}', className="card-title")
                                ]),
                        dcc.Location(id='url', refresh=False),
                        html.H2(
                            str(main_kpi_value) + ' ' +main_kpi_unit,
                            className="card-value",
                        ),
                        html.Span(main_kpi_unit_desc, 
                                  style={
                                       'font-size': '0.8rem', 
                                       'padding': '-3rem', 
                                       'margin-top': '-30px'}),
                        html.P([
                                html.I(get_icon(icon=icon_name, height = 20, color=icon_color)),
                                html.Span(icon_text, className="up")]
                        ),
                                     html.Div([ 
                            dcc.Loading(
                                dcc.Graph(
                                    id={"type": graph_name, "index": np.random.randint(1, 100000)},
                                   
                                    config={
                                        'displayModeBar': False,
                                        'staticPlot': True
                                    },
                                    responsive=True,
                                    style={'height': 60, 'margin': '0.1rem', 'padding': '0rem', 'background-color': '#455A64'}),
                                type='circle',
                                color='#0693E3',
                            )
                        ]),
                        

                    ])
                ],
                style={'border-radius': '20px', 
                       'border': '0px solid #e0e0e0', 
                       'color':'#D9D9D9', 
                       'background-color': '#455A64'}
                ),
                           
                        
                    

