from dash import register_page, callback, html,  Input, Output, ClientsideFunction, clientside_callback
import dash_mantine_components as dmc

register_page(__name__, path='/Leaflet')


layout = html.Div(
    id = 'Leaflet',
    children = [
        html.Div(
             id='mapContainer',
             children = [
                html.Div(id='map'),
            ]     
        ),
        html.Div(id='leafletUnusedOutput'),
        html.Div(id='leafletUnusedInput'),
        dmc.Group(
            className = 'locationGroup',
            children = [
                dmc.Text ('Fly to ', weight=700, size="lg", px = 7 ),
                dmc.SegmentedControl(
                    id="flytoLocations",
                    size = 'md',
                    value = '51.5192428,-0.1026286',
                    data=[
                        {"value": "45.508888,-73.561668", "label": "Montreal"},
                        {"value": "47.6475289,-122.3429879", "label": "Seattle"},
                        {"value": "51.5192428,-0.1026286", "label": "London"},
                    ]
                )
            ]
        )
    ]
)

clientside_callback(
    ClientsideFunction(
        namespace='leaflet',
        function_name='leafletFlyTo'
    ),
    Output("leafletUnusedOutput", "children"),
    Input("leafletUnusedInput", "children"),

)
