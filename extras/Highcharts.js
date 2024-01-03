
window.dash_clientside = Object.assign({}, window.dash_clientside, {

    highcharts: {

        lineChart: function (value) {
   
          const no_update = window.dash_clientside.no_update
          // document.getElementById("barChart").innerHTML = "";
  seriesData = [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4];
           let series = {
            series: [{
                data: seriesData
            }]
        };
  
          const chart = Highcharts.chart('container', series);
        
        console.log(document.getElementById('dropdown').value)
  
        document.getElementById('segmented').addEventListener('change', (e) => {
          console.log(e.target.value)
          filtered = seriesData.slice(0, parseInt(e.target.value ) +1 )
            chart.series[0].setData(filtered);
        });
        return no_update
            },



    },
});