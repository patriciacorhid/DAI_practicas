#./app/app.py
from flask import Flask
import time
import math as m
import re

app = Flask(__name__)
          
@app.route('/')
def hello_world():
  return 'Hello, World!'      

#Ejercicio 2
@app.route('/burbuja/<v>')
def burbuja(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  n = len(v) 
  
  for i in range(0, n): 
    for j in range(0, n-i-1): 
      if v[j] > v[j+1] : 
        v[j], v[j+1] = v[j+1], v[j]

  end_time = time.time()
  s = "El vector ordenado es: " + str(v) + "." + "<br>" + "Ha tardado " + str(start_time - end_time) + " segundos."
  return s

@app.route('/insercion/<v>')
def insercion(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  n = len(v)
    
  for i in range(1, n): 
    minimo = v[i] 
    j = i-1
    while j >=0 and minimo < v[j] : 
      v[j+1] = v[j] 
      j -= 1
    v[j+1] = minimo

  end_time = time.time()
  s = "El vector ordenado es: " + str(v) + "." + "<br>" + "Ha tardado " + str(start_time - end_time) + " segundos."
  return s

@app.route('/seleccion/<v>')
def seleccion(v):
  v = v.split(",")
  v = [int(x) for x in v]
  
  start_time = time.time()
  n = len(v)
    
  for i in range(0, n): 
    id_min = i
    for j in range(i+1, n): 
      if v[id_min] > v[j]:
        id_min = j 
                       
    v[i], v[id_min] = v[id_min], v[i]

  end_time = time.time()
  s = "El vector ordenado es: " + str(v) + "." + "<br>" + "Ha tardado " + str(start_time - end_time) + " segundos."
  return s

#Ejercicio 3
@app.route('/criba/<n>')
def criba(n):
  n = int(n)
  marks = [True for i in range(n+1)]
  v=[]

  for i in range (2, int(m.sqrt(n))):
    if (marks[i == True]):
      for j in range(i*i, n+1, i):
        marks[j] = False

  for p in range(2, n+1):
    if marks[p]:
      v.append(p)
      
  return "Los números primos anteriores a " + str(n) + " son " + str(v)

#Ejercicio 4
@app.route('/fibonacci/<n>')
def Fibonacci(n): #Cambiar n por f
  #fib = open(f, "r")
  #n = int(fib.read())
  n = int(n)

  if n<0: 
    return "Incorrect input"
  elif n==0: 
    return str(0)
  elif n==1: 
    return str(1)
  else: 
    return str(int(Fibonacci(n-1))+int(Fibonacci(n-2)))

#Ejercicio 5
@app.route('/parentesis/<v>')
def parentesis(v):
  suma = 0
  s = "Correcto"

  for i in v:
    if i=="[":
      suma += 1
    if i =="]":
      suma -= 1
      if suma < 0:
        s = "Incorrecto"
        break

  if suma != 0:
    s = "Incorrecto"

  return s

#Ejercicio 6
@app.route('/reg1/<v>')
#Identificar cualquier palabra seguida de un espacio y una única letra mayúscula
def reg1(v):
  exp = re.findall(r' [A-Z]', v)
  return ",".join(exp)

@app.route('/reg2/<v>')
#Identificar correos electrónicos válidos
def reg2(v):
  exp = re.findall(r'\w+\@\w+\.\w+', v)
  return ",".join(exp)

@app.route('/reg3/<v>')
#Identificar números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos
def reg3(v):
  exp = re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}|\d{4} \d{4} \d{4} \d{4}', v)
  return ",".join(exp)
