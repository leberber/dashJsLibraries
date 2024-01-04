
window.dash_clientside = Object.assign({}, window.dash_clientside, {

    D3Js: {
        bubbleMap: function (children ) {

          var svg = d3.select("#D3JsContainer")
          .append('svg')
          .attr("width", '100%')
          .attr("height", "100%")

          svg.append("text")
            .attr("x", 850/2)             
            .attr("y", 18 )
            .style("font-size", "18px") 
            .attr("text-anchor", "middle")  
            .style('font-family', '"Open Sans", sans-serif')
            .text("Carbon emissions around the world (2014)");

          // Map and projection
          var projection = d3.geoMercator()
              .center([10,20])                // GPS of location to zoom on
              .scale(120)                       // This is like the zoom
              .translate([ 850/2, 700/2 ])

          // Create data for circles:
          var markers = [
            {long: 52.5244 , lat: 13.4105,   group: "Europe",  size: 767,   country:'Germany'}, 
            {long: 48.8534 , lat: 2.3488,    group: "Europe",  size: 323,   country:'France'},
            {long: 41.8947,  lat: 12.4811,   group: "Europe",  size: 337,   country:'Italy'}, 
            {long: 55.7550,  lat: 37.6218,   group: "Europe",  size: 1766,  country:'Russia'}, 
            {long: 38.8951 , lat: -77.0364,  group: "America", size: 5334,  country:'USA'}, 
            {long: 50.4166,  lat: -100.6980, group: "America", size: 566,   country:'Canada'}, 
            {long: -15.7797, lat: -47.9297,  group: "America", size: 501,   country:'Brazil'}, 
            {long: -33.4569, lat: -70.6483,  group: "America", size: 78,    country:'Chile'}, 
            {long: 39.9075,  lat: 116.3972,  group: "Asia",    size: 10540, country:'China'},
            {long: 28.6667,  lat: 77.2167,   group: "Asia",    size: 2341,  country:'India'}, 
            {long: 35.6944,  lat: 51.4215,   group: "Asia",    size: 618,   country:'Iran'}, 
            {long: -35.2835, lat: 149.1281,  group: "Oceania", size: 409,   country:'Australia'}, 
            {long: -41.2866, lat: 174.7756,  group: "Oceania", size: 34,    country:'New Zealand'}, 
            {long: 36.7525,  lat: 3.0420,    group: "Africa",  size: 160,   country:'Algeria'}, 
            {long: 9.0250,   lat: 38.7469,   group: "Africa",  size: 100,   country:'Ethiopia'}, 
            {long: -33.9258, lat: 18.4232,   group: "Africa",  size: 392,   country:'South Africa'}, 
          ];

          // Load external data and boot
          d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson", function(data){

          // Create a color scale
          var color = d3.scaleOrdinal()
            .domain(["Europe", "America", "Asia", "Oceania", "Africa" ])
            .range([ "#402D54", "#D18975", "#8F3175", "#6FD175", "#D98975"])

          // Add a scale for bubble size
          var size = d3.scaleLinear()
            .domain([1,10000])  // What's in the data
            .range([ 4, 50])  // Size in pixel

          // Draw the map
          svg.append("g")
              .selectAll("path")
              .data(data.features)
              .enter()
              .append("path")
                .attr("fill", "#b8b8b8")
                .attr("d", d3.geoPath()
                    .projection(projection)
                )
              .style("stroke", "none")
              .style("opacity", .3)

          // Add circles:
          svg
            .selectAll("myCircles")
            .data(markers)
            .enter()
            .append("circle")
              .attr("class" , function(d){ return d.group+" _circles" })
              .attr("cx", function(d){ return projection([d.lat, d.long])[0] })
              .attr("cy", function(d){ return projection([d.lat, d.long])[1] })
              .attr("r", function(d){ return size(d.size) })
              .style("fill", function(d){ return color(d.group) })
              .attr("stroke", function(d){ return color(d.group) })
              .attr("stroke-width", 3)
              .attr("fill-opacity", .4)

          document.getElementById('d3Segmented').addEventListener('change', (e) => {
            var selectedCountry = e.target.value
              svg.selectAll("._circles").transition().duration(1000).style("opacity", 0.1).attr("r", function(d){ return size(d.size / 2) })
              svg.selectAll("."+selectedCountry).transition().duration(1000).style("opacity", 1).attr("r", function(d){ return size(d.size * 2) })
            });
          })

        return window.dash_clientside.no_update
            },
    },
});

