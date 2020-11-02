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

db['Pepe'] = dict()
db['Pepe']['pass'] = '1234'
db['Pepe'] = db['Pepe']

db['Maria'] = dict()
db['Maria']['pass'] = '1111'
db['Maria'] = db['Maria']

db['David'] = dict()
db['David']['pass'] = '0000'
db['David'] = db['David']
          
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
  
  s = "El vector ordenado es: " + str(v) + "." + "<br>" + "Ha tardado " + str(start_time - end_time) + " segundos."

  return s

@app.route('/insercion/<v>')
def ordena_insercion(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  v = insercion(v)
  end_time = time.time()
  
  s = "El vector ordenado es: " + str(v) + "." + "<br>" + "Ha tardado " + str(start_time - end_time) + " segundos."
  return s

@app.route('/seleccion/<v>')
def ordena_seleccion(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  v = seleccion(v)
  end_time = time.time()
  
  s = "El vector ordenado es: " + str(v) + "." + "<br>" + "Ha tardado " + str(start_time - end_time) + " segundos."
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
@app.route('/p3/')
def p3():
    return render_template('p3.html')

@app.route('/p1ej1/')
def p1ej1():
  return render_template('p1ej1.html')

@app.route('/login/',methods=['POST', 'GET'])
def login():
  username = request.form['username']
  password = request.form['password']

  if username in db:
    if db[username]['pass'] == password:
      session['username'] = username
      flash('Welcome ' + username)

    else:
      flash('Invalid password')

  else:
    flash('Invalid username')

  return redirect(url_for('p3'))
      
