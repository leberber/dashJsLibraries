from dash import register_page, callback, html,  Input, Output
import dash_mantine_components as dmc


register_page(__name__, path='/D3Js')

layout = html.Div(
    id = 'D3Js',
    children=[
        dmc.Center(
            style={"height": 600, "width": "100%"},
            children=[
                dmc.Text(
                    "D3Js",
                    variant="gradient",
                    gradient={"from": "#0CC0DF", "to": "#60C9DB", "deg": 45},
                    style={"fontSize": 30},
                )
            ],
        )
     

])