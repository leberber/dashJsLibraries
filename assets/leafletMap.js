
window.dash_clientside = Object.assign({}, window.dash_clientside, {

    leaflet: {
        leafletFlyTo: function (locations) {
            
            var map = L.map('map',  {attributionControl: false}).setView([51.505, -0.09], 13);
            googleMap = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{ maxZoom: 24, subdomains:['mt0','mt1','mt2','mt3'] });
            googleMap.addTo(map)

            document.getElementById('flytoLocations').addEventListener('change', (e) => {
                let coordinates = e.target.value.split(",").map(Number)
                map.flyTo([coordinates[0], coordinates[1]], 12, {
                    animate: true,
                    duration: 3 
                });
            });

            return  window.dash_clientside.no_update
        }
    }
});