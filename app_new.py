
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
from utils import sidebar, header, drawer
from dash import Output, Input, State, html


app = Dash(__name__, 
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"}
             ],
            suppress_callback_exceptions=False
           )
server = app.server

app.layout = html.Div([
	dmc.MantineProvider(
        theme={
            'fontFamily': '"Inter", sans-serif',
            "components": {
                "NavLink":{'styles':{'label':{'color':'#c2c7d0'}}}
                },
            },
        children=[
            dmc.Container([
                sidebar.get_sidebar(),
                drawer.get_drawer(),
                header.get_header(),

            ],
             size='100%', p=0,m=0, style={'display':'flex'})
]),
	
])

@dash.callback(
    Output("sidebar", "width"),
    Input("sidebar-button", "n_clicks"),
    State('sidebar','width'),
    prevent_initial_call=True,
    )
def drawer_demo(opened, width):
    if opened:
        if width['base'] == 300:
            return {"base": 70}
        else:
            return {'base':300}
    else:
        raise PreventUpdate

        
@dash.callback(
    Output("drawer-simple", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
    )
def drawer_dem(n_clicks):
    return True
        

if __name__ == '__main__':
	app.run_server(debug=True, port=8051)