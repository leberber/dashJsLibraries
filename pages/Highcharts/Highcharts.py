from dash import  html, Input, Output, clientside_callback, ClientsideFunction, register_page

register_page(__name__, path='/Highcharts')

import dash_mantine_components as dmc




layout = html.Div(
    id = 'Highcharts',
    children=[
    dmc.Select(
            label="Select framework",
            placeholder="Select one",
            id="dropdown",
            value="9",
            searchable = True,
            data=['1','2','3','4','5','6','7','8','9'],
            style={"width": 200, "marginBottom": 10},
        ),

        dmc.SegmentedControl(
            id="segmented",
            value="1",
            data=['1','2','3','4','5','6','7','8','9', '10', '11'],
            mt=10,
        ),
        html.Div(id = 'containers'),
])




clientside_callback(
    ClientsideFunction(
        namespace='highcharts',
        function_name='lineChart'
    ),
 Output("containers", "children"),
    Input("dropdown", "value"),

)


