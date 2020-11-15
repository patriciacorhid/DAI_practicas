from flask import Flask, session, request, flash, redirect, url_for
from flask import render_template
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'thesecretprotectsitself'

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo


@app.errorhandler(404)
def page_not_found(e):
  # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/mongo')
def mongo():
    return render_template('p4.html')

@app.route('/lista')
def lista():
    # Encontramos los documentos de la coleccion "samples_friends"
    movies = db.video_movies.find() # devuelve un cursor(*), no una lista ni un iterador

    lista_movies = []
    i = 0

    for t in movies:
        if i< 20:
            app.logger.debug(t) # salida consola
            lista_movies.append(t)
            i+=1

    # a los templates de Jinja hay que pasarle una lista, no el cursor
    return render_template('lista.html', movies=lista_movies)

# Buscar pelicula por titulo
@app.route('/title',methods=['POST'])
def buscar_titulo():
  # Pido datos del formulario
  mtitle = request.form['title']

  # Si el nombre es vacío, muestro mensaje de error
  if mtitle == '':
      flash('Película inválida')
      return redirect(url_for('mongo'))

  lista = db.video_movies.find({"title": mtitle})
  return render_template('lista.html', movies=lista)

# Buscar pelicula por titulo
@app.route('/year',methods=['POST'])
def buscar_year():
  # Pido datos del formulario
  myear = request.form['year']

  # Si el nombre es vacío, muestro mensaje de error
  if myear == '':
      flash('Película inválida')
      return redirect(url_for('mongo'))


  lista = db.video_movies.find({"year": int(myear)})
  return render_template('lista.html', movies=lista)

# Buscar pelicula por titulo
@app.route('/imdb',methods=['POST'])
def buscar_imdb():
  # Pido datos del formulario
  mimdb = request.form['imdb']

  # Si el nombre es vacío, muestro mensaje de error
  if mimdb == '':
      flash('Película inválida')
      return redirect(url_for('mongo'))

  lista = db.video_movies.find({"imdb": mimdb})
  return render_template('lista.html', movies=lista)


# Buscar pelicula por titulo
@app.route('/type',methods=['POST'])
def buscar_tipo():
  # Pido datos del formulario
  mtype = request.form['type']

  # Si el nombre es vacío, muestro mensaje de error
  if mtype == '':
      flash('Película inválida')
      return redirect(url_for('mongo'))

  lista = db.video_movies.find({"type": mtype})
  return render_template('lista.html', movies=lista)
