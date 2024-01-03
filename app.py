from dash import Dash,  html, dcc, Output,Input, callback, page_container,  ALL
import dash_mantine_components as dmc

app = Dash(
     __name__, 
     use_pages=True,  
     suppress_callback_exceptions=True,
     external_scripts=[
        'https://cdn.jsdelivr.net/npm/apexcharts',
        'https://code.highcharts.com/highcharts.js', 
    ]
    )

focusLinkStyle = { 
     'width':'70px', 
     'height':'70px', 
     'margin':'-20px', 
     'backgroundColor':'rgb(255, 255, 255)', 
     'borderRadius':'50%', 
     'padding':'15px', 
     'boxShadow': '0 0 50px #ccc'
}

def page_link (pageHref):
    if pageHref == 'apexCharts':
        href = "/"
        style = focusLinkStyle
    else:
        href = pageHref
        style = {}

    return dcc.Link(
        href= href,  
        children =[
            dmc.ActionIcon(
                id={"type": "pages-links", "index": pageHref},
                n_clicks = 0,
                style = style,
                children = [
                    dmc.Image(src=f"/assets/svg/{pageHref}.svg", width='100%')
                ]
            )
        ]
    )

_pages = ['apexCharts','Highcharts', 'Leaflet', 'D3Js']

app.layout = html.Div(
    id = 'dash-app-layout',
    children = [
         html.Div(id = 'unUsedInput'),
        html.Div(
            id = 'dash-page-navigation-bar',
            children = [
                page_link(p) for p in _pages
            ] 
        ),
            
        html.Div(
            id = 'dash-page-container',
            children = [
                page_container
            ]
        )
    ]
)

@callback(
    Output({'type': 'pages-links', 'index': ALL}, 'style'),
    Output({'type': 'pages-links', 'index': ALL}, 'n_clicks'),
    Input({'type': 'pages-links', 'index': ALL}, 'n_clicks'),
    prevent_initial_call = True
)
def styleCurrentPage(id):
    pageIndex = id.index(1)
    styles = [{'backgroundColor':'transparent'}] * len(id)
    styles[pageIndex] = focusLinkStyle
    return [styles, [0] * len(id)]



if __name__ == '__main__':
	app.run_server(
     port=8070,  debug = True
    )