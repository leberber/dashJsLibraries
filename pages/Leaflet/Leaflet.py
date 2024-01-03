from dash import register_page, callback, html,  Input, Output

import dash_mantine_components as dmc


register_page(__name__, path='/Leaflet')


layout = html.Div(
    id = 'Leaflet',
    children = [
    dmc.Center(
        style={"height": 600, "width": "100%"},
        children=[
            dmc.Text(
                "Leaflet",
                variant="gradient",
                gradient={"from": "#0CC0DF", "to": "#60C9DB", "deg": 45},
                style={"fontSize": 30},
            )
        ],
    )
])

