from dash import  dcc, html, Input, Output, clientside_callback, ClientsideFunction, register_page
import dash_mantine_components as dmc
from pages.data import emissions
from dash_iconify import DashIconify


register_page(__name__, path='/highcharts')


layout = html.Div(
    children = [
        dcc.Store(id = 'HighchartsSampleData', data=emissions ),
        dmc.Paper(
            className = 'ChartAreaDiv',
            shadow="sm",
            children = [
                html.Div(id = 'highchartAreaChart'),
                dmc.Center(
                    children = [
                        dmc.Text("Filter Out A region", p = 20),
                        dmc.SegmentedControl(
                            id="selectRegion",
                            value="null",
                            data=['Europe','Africa','Oceania','North America','South America','Asia'],
                        ),
                        dmc.Button(
                            "Reset",
                            id = 'resetHighChart',
                            variant="subtle",
                            rightIcon=DashIconify(icon="system-uicons:reset"),
                            color="blue",
                        ),
                    ]
                )
            ]
        )  
    ]
)




clientside_callback(
    ClientsideFunction(
        namespace='highcharts',
        function_name='packedbubble'
    ),
 Output("highchartAreaChart", "children"),
 Input("HighchartsSampleData", "data"),
 Input("resetHighChart", "n_clicks"),
 

)


