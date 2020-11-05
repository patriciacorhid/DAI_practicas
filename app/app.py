#./app/app.py
from flask import Flask, session, request, flash, redirect, url_for
from flask import render_template
from pickleshare import *

from ejercicios import burbuja
from ejercicios import insercion
from ejercicios import seleccion
from ejercicios import criba
from ejercicios import fib
from ejercicios import parentesis
from ejercicios import reg1
from ejercicios import reg2
from ejercicios import reg3

import time
import math as m
import re

from random import randint 

app = Flask(__name__)
app.secret_key = 'thesecretprotectsitself'

# Usuarios de Cactus Web (P3) 
db = PickleShareDB('miBD')

# Para eliminar usuarios creados anteriormente en la base de datos
db.clear()

# Creo un par de usuarios de prueba
db['Pepe'] = dict()
db['Pepe']['pass'] = '1234'
db['Pepe'] = db['Pepe']

db['Maria'] = dict()
db['Maria']['pass'] = '1111'
db['Maria'] = db['Maria']
          
@app.route('/')
def hello_world():
  return 'Hello, World!'      

#------------------------------- EJERCICIO 1: Interfaz para los ejercicios del 2 al 6 de la práctica anterior ----------------------------------

#Ejercicio 2
@app.route('/burbuja/<v>')
def ordena_burbuja(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  v = burbuja(v) 
  end_time = time.time()
  
  s = "El vector ordenado es: " + str(v) + ". Ha tardado " + str(start_time - end_time) + " segundos."

  return s

@app.route('/insercion/<v>')
def ordena_insercion(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  v = insercion(v)
  end_time = time.time()
  
  s = "El vector ordenado es: " + str(v) + ". Ha tardado " + str(start_time - end_time) + " segundos."
  return s

@app.route('/seleccion/<v>')
def ordena_seleccion(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  v = seleccion(v)
  end_time = time.time()
  
  s = "El vector ordenado es: " + str(v) + ". Ha tardado " + str(start_time - end_time) + " segundos."
  return s

#Ejercicio 3
@app.route('/criba/<n>')
def criba_erastotenes(n):
  n = int(n)

  v = criba(n)
      
  return "Los números primos anteriores a " + str(n) + " son " + str(v)

#Ejercicio 4
@app.route('/fibonacci/<n>')
def Fibonacci(n):
  n = int(n)
  num = fib(n)
  
  return 'El número de Fibonacci en la posición ' + str(n) + ' es ' + str(num)

#Ejercicio 5
@app.route('/parentesis/<v>')
def func_parentesis(v):
  s = parentesis(v)

  return s

#Ejercicio 6
@app.route('/reg1/<v>')
#Identificar cualquier palabra seguida de un espacio y una única letra mayúscula
def func_reg1(v):
  s = reg1(v)
  
  return s

@app.route('/reg2/<v>')
#Identificar correos electrónicos válidos
def func_reg2(v):
  s = reg2(v)
  
  return s


@app.route('/reg3/<v>')
#Identificar números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos
def func_reg3(v):
  s = reg3(v)
  
  return s


#------------------------------- EJERCICIO 2 ----------------------------------
@app.route('/ejercicio2/')
def ejercicio2():
    return render_template('ejercicio2.html')
  #------------------------------- EJERCICIO 3 ----------------------------------
@app.errorhandler(404)
def page_not_found(e):
  # note that we set the 404 status explicitly
    return render_template('404.html'), 404
  #------------------------------- EJERCICIO 4 (Subir Nota) ----------------------------------
@app.route('/svg/')
def visualize_svg():
   # Figura
   n = randint(0, 2)

   # Posición
   cx = randint(100, 500)
   cy = randint(100, 500)

   # Color
   r = randint(0, 255)
   g = randint(0, 255)
   b = randint(0, 255)

   s = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"

   if n == 0:
     return render_template('circulo.html', x = str(cx), y = str(cy), f = s)
   elif n == 1:
     return render_template('rectangulo.html', x = str(cx), y = str(cy), f = s)
   else:
     return render_template('elipse.html',  x = str(cx), y = str(cy), f = s)


#******************************* PRACTICA 3 ********************************

# Página principal de la práctica 3
@app.route('/p3/')
def p3():
    return render_template('p3.html')

# Sign in (Acceso a usuario registrado)
@app.route('/login/',methods=['POST', 'GET'])
def login():
  # Pido datos del formulario
  username = request.form['username']
  password = request.form['password']

  if username in db:
    if db[username]['pass'] == password:
      # Si ya está resistrado y su contraseña coincide,
      # iniciar sesión y mostrar mensaje de bienvenida
      session['username'] = username
      session['url'] = []
      session['nurl'] = [] # Nombre de las url
      flash('Bienvenid@ ' + username)

    else:
      # Si ya está resistrado y su contraseña no coincide,
      # mostrar mensaje de error
      flash('Contraseña inválida')

  else:
    # Si no está resistrado, mostrar mensaje de error
    flash('Usuario inválido')

  #Volver a la página principal con el mensaje correspondiente.
  return redirect(url_for('p3'))

# Salir de la sesión de una persona
@app.route('/exit/')
def exit():
  # Poner sesión vacía
  session['username'] = ''

  #Volver a la página inicial
  return redirect(url_for('p3'))

# Registrarse
@app.route('/signup/',methods=['POST', 'GET'])
def signup():
  # Mostrar el template de registro
  return render_template('signup.html')

# Guardar cuenta recien creada
@app.route('/account_created/',methods=['POST', 'GET'])
def account_created():
  # Pido datos del formulario
  username = request.form['username']
  password = request.form['password']

  # Si el nombre es vacío, muestro mensaje de error
  if username == '':
    flash('Usuario inválido')
    return redirect(url_for('signup'))

  # Si el nombre ya existe, muestro mensaje de error
  if username in db:
    flash('Usuario inválido. Este usuario ya existe')
    return redirect(url_for('signup'))

  # Guardo los datos en la base de datos
  db[username] = dict()
  db[username]['pass'] = password
  db[username] = db[username]

  # Inicio sesión con este nuevo individuo y pongo mensaje de bienvenida
  session['username'] = username
  session['url'] = []
  session['nurl'] = []
  flash('Bienvenid@ ' + username)

  # Redirijo a la página oficial
  return redirect(url_for('p3'))

# Visualizar datos usuario
@app.route('/datos/')
def datos():
  return render_template('datos.html', user=session['username'], pwd=db[session['username']]['pass'])

# Modificar datos
@app.route('/modify/',methods=['POST', 'GET'])
def modify():
  # Pido datos del formulario
  username = request.form['username']
  password = request.form['password']

  # Si el nombre es vacío, muestro mensaje de error
  if username == '':
    flash('Usuario inválido')
    return redirect(url_for('datos'))

  # Si el nombre ya existe, muestro mensaje de error
  if username in db and username != session['username']:
    flash('Usuario inválido. Este usuario ya existe')
    return redirect(url_for('datos'))

  #Elimino el usuario anterior
  del db[session['username']]

  # Guardo los datos en la base de datos
  db[username] = dict()
  db[username]['pass'] = password
  db[username] = db[username]

  # Inicio sesión con este nuevo individuo y pongo mensaje de bienvenida
  session['username'] = username
  flash('Datos de ' + username + ' actualizados correctamente.')

  # Redirijo a la página oficial
  return redirect(url_for('datos'))


#-------------------------------------------------------------------


# Página donde se encuentra el ejercicio 1 de la práctica 1
@app.route('/p1ej1/', methods=['POST', 'GET'])
def p1ej1():

  if request.method == 'GET':
    # Guardamos el haber visitado la página en la base de datos
    if session['username']:
      #Url
      temp = session['url']
      temp.append("/p1ej1/")
      session['url'] = temp
    
      #Nombre de la url
      temp = session['nurl']
      temp.append("Ejercicio 1")
      session['nurl'] = temp
    
      # Solo queremos las 3 últimas páginas visitadas
      if len(session['url']) > 3:
        session['url'].pop(0)
        session['nurl'].pop(0)

    # Es la primera vez, generamos el número aleatorio
    session['intentos'] = 0
    session['n'] = randint(0,100)

    return render_template('p1ej1.html', title="Ejercicio 1", enunciado="Adivina el número del 1 al 100")

  else:
    # Si es el último intento, volvemos a la página inicial
    if session['intentos'] > 9:
      flash("Mala suerte. El número era el " + str(session['n']))
      session['intentos'] = 0
      session['n'] = randint(0,100)
      return render_template('p1ej1.html', title="Ejercicio 1", enunciado="Adivina el número del 1 al 100")

    num  = int(request.form['num'])
    session['intentos']+=1

    if num == session['n']:
      session['intentos'] = 0
      session['n'] = randint(0,100)
      flash('Has adivinado el número, felicidades.')
      return render_template('p1ej1.html', title="Ejercicio 1", enunciado="Adivina el número del 1 al 100")
    elif num < session['n']:
      flash('Mala suerte. El número buscado es mayor.')
      return render_template('p1ej1.html', title="Ejercicio 1", enunciado="Adivina el número del 1 al 100")
    else:
      flash('Mala suerte. El número buscado es menor.')
      return render_template('p1ej1.html', title="Ejercicio 1", enunciado="Adivina el número del 1 al 100")
  

# Página donde se encuentra el ejercicio 2 de la práctica 1
@app.route('/p1ej2_insercion/<v>')
def p1ej2_insercion(v):

  # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    # Url
    temp = session['url']
    temp.append("/p1ej2_insercion/0,-3,8,5,11,2,4")
    session['url'] = temp

    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 2 - Insercion")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)

  return render_template('ejerciciosp1.html', title="Ejercicio 2", enunciado="Ordenación por inserción del vector [" + str(v) + "]", resultado=ordena_insercion(v))


# Página donde se encuentra el ejercicio 2 de la práctica 1
@app.route('/p1ej2_seleccion/<v>')
def p1ej2_seleccion(v):

  # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    # Url
    temp = session['url']
    temp.append("/p1ej2_seleccion/0,-3,8,5,11,2,4")
    session['url'] = temp

    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 2 - Seleccion")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)
  
  return render_template('ejerciciosp1.html', title="Ejercicio 2", enunciado="Ordenación por selección del vector [" + str(v) + "]", resultado=ordena_seleccion(v))


# Página donde se encuentra el ejercicio 3 de la práctica 1
@app.route('/p1ej3/<n>')
def p1ej3(n):

  # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    # Url
    temp = session['url']
    temp.append("/p1ej3/200")
    session['url'] = temp

    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 3")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)
  
  return render_template('ejerciciosp1.html', title="Ejercicio 3", enunciado="Criba de Erastótenes del número " + str(n), resultado=criba_erastotenes(n))


# Página donde se encuentra el ejercicio 4 de la práctica 1
@app.route('/p1ej4/<n>')
def p1ej4(n):

  # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    # Url
    temp = session['url']
    temp.append("/p1ej4/9")
    session['url'] = temp

    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 4")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)
  
  return render_template('ejerciciosp1.html', title="Ejercicio 4", enunciado="Número de Fibonacci en la posición " + str(n), resultado=Fibonacci(n))


# Página donde se encuentra el ejercicio 5 de la práctica 1
@app.route('/p1ej5/<v>')
def p1ej5(v):

   # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    # Url
    temp = session['url']
    temp.append("/p1ej5/[[][[]]]")
    session['url'] = temp

    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 5")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)
      
  return render_template('ejerciciosp1.html', title= "Ejercicio 5", enunciado="Comprobar si la secuencia " + str(v) + " es o no correcta", resultado=func_parentesis(v))

# Página donde se encuentra el ejercicio 6 de la práctica 1
@app.route('/p1ej61/<v>')
def p1ej61(v):

   # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    # Url
    temp = session['url']
    temp.append("/p1ej61/El%20agente%20A%20preparaba%20los%20planes%20de%20su%20misión.%20Esta%20noche%20se%20encontraría%20con%20su%20archienemigo%20B%20y%20esperabo%20poder%20derrotarlo%20de%20una%20vez%20por%20todas.")
    session['url'] = temp
    
    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 6 - Mayúscula")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)
  
  return render_template('ejerciciosp1.html', title="Ejercicio 6", enunciado= "Palabras que empiezan con mayúscula tras un espacio del texto: " + str(v), resultado=func_reg1(v))

# Página donde se encuentra el ejercicio 6 de la práctica 1
@app.route('/p1ej62/<v>')
def p1ej62(v):

   # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    # Url
    temp = session['url']
    temp.append("/p1ej62/Busqué%20su%20correo%20desesperadamente%20entre%20aquella%20larga%20lista:%20maria223@gmail.com,%20pepito_chiquitito@yahoo.es,%20jose28ramirez@google45.org...%20Aquí%20está:%20lola_la_ola_6544@sss.es")
    session['url'] = temp
    
    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 6 - Correo")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)
  
  return render_template('ejerciciosp1.html', title="Ejercicio 6", enunciado= "Correos electrónicos del texto: " + str(v),  resultado=func_reg2(v))

# Página donde se encuentra el ejercicio 6 de la práctica 1
@app.route('/p1ej63/<v>')
def p1ej63(v):

   # Guardamos el haber visitado la página en la base de datos
  if session['username']:
    temp = session['url']
    temp.append("/p1ej63/%20No%20me%20acordaba%20de%20su%20cuenta%20bancaria:1234-1234-5678-5678,%201111-1111-1111-1111,9874%205632%201447%201444.%20Todos%20intentos%20fallidos.%20Ya%20era%2019-03-2020,%20necesitaba%20la%20cuenta%20urgentemente")
    session['url'] = temp

    # Nombre de la url
    temp = session['nurl']
    temp.append("Ejercicio 6 - Cuentas")
    session['nurl'] = temp
    
    # Solo queremos las 3 últimas páginas visitadas
    if len(session['url']) > 3:
      session['url'].pop(0)
      session['nurl'].pop(0)
  
  return render_template('ejerciciosp1.html', title="Ejercicio 6", enunciado= "Cuentas bancarias del texto: " + str(v), resultado=func_reg3(v))
