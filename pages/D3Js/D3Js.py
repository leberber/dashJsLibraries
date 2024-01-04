from dash import register_page, callback, html,  Input, Output, clientside_callback, ClientsideFunction
import dash_mantine_components as dmc


register_page(__name__, path='/')



layout = html.Div(
    id = 'd3js',
    children = [
        dmc.Paper(
            className = 'ChartAreaDiv',
            shadow="sm",
            children = [
                html.Div(id = 'D3JsContainer', style = {"height":"80%", "width":"100%"}),
                dmc.Center(
                    children = [
                        dmc.Text("Highlight a Region", p = 40, weight=500, size="md"),
                         dmc.SegmentedControl(
                            id="d3Segmented",
                            value="Canada",
                            data=['Europe', 'America', 'Asia', 'Oceania','Africa'],
                        ),
                    ]
                )
            ]
        ),
        dmc.Group(id = 'D3JsUnsedInput'),  
    ]
)

clientside_callback(
    ClientsideFunction(
        namespace='D3Js',
        function_name='bubbleMap'
    ),
    Output("D3JsContainer", "children"),
    Input("D3JsUnsedInput", "children"),

)