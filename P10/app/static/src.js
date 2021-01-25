// Cambia el Dark Mode al darle al botón 
function darkMode(){
    
    var content = document.body;
    var DARKMODE = (localStorage.getItem('DARKMODE') == "ON");

    if (DARKMODE){
	content.classList.remove("darkMode");
	localStorage.setItem('DARKMODE', "OFF");
    } else {
	content.classList.add("darkMode");
	localStorage.setItem('DARKMODE', "ON");
    }
}

// Compureba si está el DarkMode activo para ponerlo
function check_darkMode(){
    var content = document.body;
    
    if (localStorage.getItem('DARKMODE') == "ON"){
	content.classList.add("darkMode");
    } else {
	content.classList.remove("darkMode");
    }
}

// Cada vez que cambio de página compruebo si estaba el Dark Mode activo y
// lo pongo en caso afirmativo
check_darkMode()

// --------------  Muestra películas recomendadas -------------
var images=["/static/recomendadas/west_side_story.jpeg", "/static/recomendadas/star_wars5.jpeg", "/static/recomendadas/show_truman.jpeg", "/static/recomendadas/pretty_woman.jpeg", "/static/recomendadas/lost_translation.jpeg", "/static/recomendadas/planeta_tesoro.jpeg", "/static/recomendadas/into_wild.jpeg", "/static/recomendadas/club_poetas_muertos.jpeg"];

// Número de la imagen que se muestra
var pos = 0;

// Pasar a imagen previa
function prev(){
    var cartelera = document.getElementById("pelis");
    pos--;
    if(pos<0){
	pos = images.length-1;
    }
    cartelera.src = images[pos];
}

// Pasar a imagen siguiente
function next(){
    var cartelera = document.getElementById("pelis");
    pos++;
    if(pos>=images.length){
	pos = 0;
    }
    cartelera.src = images[pos];
}

// --------------------- Estilo de las gráficas --------------------
  Highcharts.setOptions({
      colors: ['#6AF9C4', '#cc0099', '#4d0085', '#ff9933', '#ffff66', '#ff6666', '#0033cc', '#66ffff', '#ccff66', '#cc0000'],
      chart: {
          backgroundColor: {
              linearGradient: [0, 0, 500, 500],
              stops: [
                  [0, 'rgb(255, 255, 255)'],
                  [1, 'rgb(240, 240, 255)']
              ]
          },
          borderWidth: 2,
	  borderColor: 'rgba(183, 63, 255, .9)',
          plotBackgroundColor: 'rgba(255, 255, 255, .9)',
          plotShadow: true,
          plotBorderWidth: 1
      }
  });

// ---------------------------- Mapa -------------------------------

var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984 / Original
var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection / Google Maps

// Posición de marcador 1:
var lat1 = 37.18016780456436; // Latitud
var lon1 = -3.6088907718658447; // Longitud
var position1 = new OpenLayers.LonLat(lon1, lat1).transform(fromProjection, toProjection);

// Posición de marcador 2:
var lat2 = 37.19707402164348; // Latitud
var lon2 = -3.6234471201896667; // Longitud
var position2 = new OpenLayers.LonLat(lon2, lat2).transform(fromProjection, toProjection);

// Posición del centro del mapa:
var lat_center = 37.18954874379851; // Latitud
var lon_center = -3.614630699157715; // Longitud
var center = new OpenLayers.LonLat(lon_center, lat_center).transform(fromProjection, toProjection);

// Zoom inicial del mapa
var zoom = 14;

map = new OpenLayers.Map("mapa"); // Asignamos el mapa al contenedor
map.addLayer(new OpenLayers.Layer.OSM()); // Agregamos la capa de OpenStreetMap
map.setCenter(center, zoom) /// Asignamos el centro, la posicion y el zoom inicial

var markers = new OpenLayers.Layer.Markers( "Markers" ); // Creamos una capa para los marcadores
map.addLayer(markers); // Agregamos la capa al mapa 
markers.addMarker(new OpenLayers.Marker(position)); // Agregamos el marcador 1
markers.addMarker(new OpenLayers.Marker(position2)); // Agregamos el marcador 2
