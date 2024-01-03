
window.dash_clientside = Object.assign({}, window.dash_clientside, {

    apexCharts: {

        areaChart: function (trade) {

            data = trade.filter(item=>  item.country==='Canada') 
            var options = {
                series: [
                    {
                        name: 'USD',
                        type: 'column',
                        data: data.map( (item) => item.trade_usd)
                    }, 
                    {
                        name: 'Weight',
                        type: 'area',
                        data: data.map( (item) => item.weight_kg)
                    },
                 
                ],
                labels: [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
                xaxis: { type: 'category'},
                yaxis: [
                    { 
                        labels: { formatter:  BillionFormatter},
                        title: { text: "Billions (USD) "},
                    },
                    {
                        opposite: true,
                        labels: { formatter: GigatonneFormatter},
                        title: { text: 'Gigatonne'}
                    }
                ],
                fill: {
                    opacity: [0.85, 0.25, 1],
                    gradient: {
                        inverseColors: false,
                        shade: 'light',
                        type: "vertical",
                        opacityFrom: 0.85,
                        opacityTo: 0.55,
                        stops: [0, 100, 100, 100]
                    }
                },
                chart: { height: '85%'},
                stroke: { width: [0, 4],  curve: 'smooth'},
                title: {
                    text: "Global Import of Cereals",
                    align: 'center',
                    style: {
                        fontSize:  '22px',
                        fontWeight:  'bold',
                    },
                },
                dataLabels: {
                    enabled: true,
                    enabledOnSeries: [1],
                    formatter: GigatonneFormatter
                  },
              };
              var chart = new ApexCharts(document.querySelector("#apexAreaChart"), options);

              document.getElementById('selectCountryChip').addEventListener('change', (e) => {
                data = trade.filter(item=>  item.country===e.target.value) 
                usd = data.map( (item) => item.trade_usd)
                weight = data.map( (item) => item.weight_kg)
                console.log([usd, weight])
                chart.updateSeries([
                    { name: 'USD', data: usd}, 
                    { name: 'Weight', data: weight}
                ])
            });
              
            chart.render();

        return window.dash_clientside.no_update
            },
    },
});

