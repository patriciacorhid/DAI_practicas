from flask import Flask, session, request, flash, redirect, url_for, jsonify
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

    for t in movies:
        app.logger.debug(t) # salida consola
        lista_movies.append(t)

    # a los templates de Jinja hay que pasarle una lista, no el cursor
    return render_template('lista.html', movies=lista_movies, buscar = False)

# Buscar película
@app.route('/buscar')
def buscar():
    return render_template('busqueda.html')

# Buscar pelicula por titulo
@app.route('/title',methods=['POST'])
def buscar_titulo():
  # Pido datos del formulario
  mtitle = request.form['title']

  # Si el nombre es vacío, muestro mensaje de error
  if mtitle == '':
      flash('Película inválida')
      return redirect(url_for('buscar'))

  lista = db.video_movies.find({"title": {"$regex":mtitle}})
  #lista = db.video_movies.find({"title": mtitle})
  return render_template('lista.html', movies=lista, buscar = True)

# Buscar pelicula por titulo
@app.route('/year',methods=['POST'])
def buscar_year():
  # Pido datos del formulario
  myear = request.form['year']

  # Si el nombre es vacío, muestro mensaje de error
  if myear == '':
      flash('Película inválida')
      return redirect(url_for('buscar'))


  lista = db.video_movies.find({"year": int(myear)})
  return render_template('lista.html', movies=lista, buscar = True)

# Buscar pelicula por titulo
@app.route('/imdb',methods=['POST'])
def buscar_imdb():
  # Pido datos del formulario
  mimdb = request.form['imdb']

  # Si el nombre es vacío, muestro mensaje de error
  if mimdb == '':
      flash('Película inválida')
      return redirect(url_for('buscar'))

  lista = db.video_movies.find({"imdb": {"$regex":mimdb}})
  return render_template('lista.html', movies=lista, buscar = True)


# Buscar pelicula por titulo
@app.route('/type',methods=['POST'])
def buscar_tipo():
  # Pido datos del formulario
  mtype = request.form['type']

  # Si el nombre es vacío, muestro mensaje de error
  if mtype == '':
      flash('Película inválida')
      return redirect(url_for('buscar'))

  lista = db.video_movies.find({"type": {"$regex":mtype}})
  return render_template('lista.html', movies=lista, buscar = True)

# Añadir película acceso a formulario
@app.route('/insertar')
def insertar():
    return render_template('insertar.html')

# Añadir pelicula recoger datos de formulario
@app.route('/insert',methods=['POST'])
def insert():
    # Pido datos del formulario
    mtitle = request.form['title']
    myear = request.form['year']
    mimdb = request.form['imdb']
    mtype = request.form['type']

    # Compruebo que todos los campos estén rellenos
    if mtitle == '' or myear == '' or mimdb == '' or mtype == '':
        flash('Película inválida')
        return redirect(url_for('insertar'))

    # Compruebo que la película no esté ya en la BD
    movies = db.video_movies.find({'title': mtitle, 'year': int(myear), 'imdb': mimdb, 'type': mtype})
    lista_movies = []

    for t in movies:
        app.logger.debug(t) # salida consola
        lista_movies.append(t)

    # Si ya estaba, devuelvo mensaje de error
    if(len(lista_movies)>0):
        flash('Película inválida. Ya existe en la base de datos.')
        return redirect(url_for('insertar'))

    # Si no estaba la inserto
    db.video_movies.insert({'title': mtitle, 'year': int(myear), 'imdb': mimdb, 'type': mtype})
    flash('La película ' + mtitle + ' se ha insertado correctamente')
    return render_template('insertar.html')

# Modificar película acceso a formulario
@app.route('/modificar')
def modificar():
    return render_template('modificar.html')

# Busco la película a modificar
@app.route('/mod_title',methods=['POST'])
def modify():
    # Pido datos del formulario
    mtitle = request.form['title']

    # Compruebo que el campo no es vacía
    if mtitle == '':
        flash('Película inválida')
        return redirect(url_for('modificar'))

    # Compruebo que la película esté ya en la BD
    movies = db.video_movies.find({'title': mtitle})
    lista_movies = []

    for t in movies:
        app.logger.debug(t) # salida consola
        lista_movies.append(t)

    # Si no está, devuelvo mensaje de error
    if(len(lista_movies)==0):
        flash('Película inválida.')
        return redirect(url_for('modificar'))

    return render_template('modify.html', movie=lista_movies[0])

# Modificar pelicula
@app.route('/mod/<v>',methods=['POST'])
def modif(v):
    # Pido datos del formulario
    mtitle = v
    myear = request.form['year']
    mimdb = request.form['imdb']
    mtype = request.form['type']

    # Modifico la película
    flash('La película ' + mtitle + ' se ha modificado correctamente')
    db.video_movies.find_one_and_update({'title': mtitle}, {"$set":{'year': int(myear), 'imdb': mimdb, 'type': mtype}})
    return redirect(url_for('modificar'))

# Borrar pelicula formulario
@app.route('/borrar')
def borrar():
    return render_template('borrado.html')

# Borrar pelicula
@app.route('/borrado',methods=['POST'])
def borrado():
    # Pido datos del formulario
    mtitle = request.form['title']

    # Borro la película
    flash('La película ' + mtitle + ' se ha borrado correctamente')
    db.video_movies.delete_one({'title': mtitle})
    return redirect(url_for('borrar'))



#------------------------------------ PRACTICA 5 ------------------------------------------------
@app.route('/api/movies',methods=['GET', 'POST'])
def api_1():

    # Busca películas en la base de datos
    if request.method == 'GET':
        args = request.args

        # Busco por cada uno de los 4 posibles campos
        # Si no hay campos especificados en los argumentos
        # devuelve todas las películas
        if 'title' in args:
            movies = db.video_movies.find({'title': {"$regex": args['title']}})
        elif 'year' in args:
            movies = db.video_movies.find({'year': int(args['year'])})
        elif 'imdb' in args:
            movies = db.video_movies.find({'imdb': {"$regex": args['imdb']}})
        elif 'type' in args:
            movies = db.video_movies.find({'type': {"$regex": args['type']}})
        else:
            movies = db.video_movies.find()

        lista = []

        for movie in movies:
            lista.append({
                'id': str(movie.get('_id')),
                'title' : movie.get('title'),
                'year': movie.get('year'),
                'imdb': movie.get('imdb'),
                'type' : movie.get('type')
            })

        return jsonify(lista)

    # Añado una nueva película a la base de datos
    if request.method == 'POST':
        
        # Guardo los argumentos pasados como parámetros
        args = request.json
        mtitle = args['title']
        myear = args['year']
        mimdb = args['imdb']
        mtype = args['type']

        # Si no están todos los campos completos se considera inválida
        if mtitle == '' or myear == '' or mimdb == '' or mtype == '':
            return jsonify({'error':'Se intenta introducir película inválida'})
        
        # Compruebo que la película no esté ya en la BD
        movies = db.video_movies.find({'title': mtitle, 'year': int(myear), 'imdb': mimdb, 'type': mtype})
        lista_movies = []

        for t in movies:
            lista_movies.append(t)

        # Si ya estaba, devuelvo mensaje de error
        if(len(lista_movies)>0):
            return jsonify({'error':'La película ya existe'})

        # Inserto la película
        db.video_movies.insert({'title': mtitle, 'year': int(myear), 'imdb': mimdb, 'type': mtype})
        return jsonify({'title': mtitle, 'year': int(myear), 'imdb': mimdb, 'type': mtype})


@app.route('/api/movies/<id>',methods=['PUT', 'DELETE'])
def api_2(id):
    
    if request.method == 'PUT':

        # Compruebo que la película exista
        movies = db.video_movies.find({'imdb': id})
        lista_movies = []

        for t in movies:
            lista_movies.append(t)

        # Si no existe la película, devuelvo mensaje de error
        if(len(lista_movies)==0):
            return jsonify({'error':'La película no existe'}), 404

        # Guardo los argumentos pasados como parámetros
        args = request.json
        mtitle = args['title']
        myear = args['year']
        mimdb = id
        mtype = args['type']

        # Si no están todos los campos completos se considera inválida
        if mtitle == '' or myear == '' or mtype == '':
            return jsonify({'error':'Se intenta introducir película inválida'})

        # Modifico la película
        db.video_movies.find_one_and_update({'imdb': mimdb}, {"$set":{'year': int(myear), 'title': mtitle, 'type': mtype}})
        return jsonify({'title': mtitle, 'year': int(myear), 'imdb': mimdb, 'type': mtype})

    if request.method== 'DELETE':

        # Compruebo que la película exista
        movies = db.video_movies.find({'imdb': id})
        lista_movies = []

        for t in movies:
            lista_movies.append(t)

        # Si no existe la película, devuelvo mensaje de error
        if(len(lista_movies)==0):
            return jsonify({'error':'La película no existe'}), 404
        
        # Elimino la película
        db.video_movies.delete_one({'imdb': id})
        return jsonify({'imdb': id})
        
