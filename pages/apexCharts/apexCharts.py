
from dash import html, dcc,Input, Output, clientside_callback, ClientsideFunction, register_page

import dash_mantine_components as dmc
from pages.data import imports


register_page(__name__, path='/apexcharts')

layout = html.Div(
    children = [
        dcc.Store(id = 'ApexchartsSampleData', data=imports ),
        dmc.Paper(
            className = 'ChartAreaDiv',
            shadow="sm",
            children = [
                html.Div(id = 'apexAreaChart'),
                dmc.Center(
                    children = [
                        dmc.SegmentedControl(
                            id="selectCountryChip",
                            value="Canada",
                            data=['Canada', 'USA', 'Australia'],
                        )
                    ]
                )
            ]
        )  
    ]
)


clientside_callback(
    ClientsideFunction(
        namespace='apexCharts',
        function_name='areaChart'
    ),
    Output("apexAreaChart", "children"),
    Input("ApexchartsSampleData", "data"),

)

