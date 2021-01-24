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
var num = 0;

// Pasar a imagen previa
function prev(){
    var cartelera = document.getElementById("pelis");
    num--;
    if(num<0){
	num = images.length-1;
    }
    cartelera.src = images[num];
}

// Pasar a imagen siguiente
function next(){
    var cartelera = document.getElementById("pelis");
    num++;
    if(num>=images.length){
	num = 0;
    }
    cartelera.src = images[num];
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
