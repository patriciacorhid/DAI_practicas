# Patricia Córdoba

import time
import math as m
import re
 

#------------------------------- EJERCICIO 2 ----------------------------------
def burbuja(v):
  n = len(v) 
  
  for i in range(0, n): 
    for j in range(0, n-i-1): 
      if v[j] > v[j+1] : 
        v[j], v[j+1] = v[j+1], v[j]

  return v

def insercion(v):
  n = len(v)
    
  for i in range(1, n): 
    minimo = v[i] 
    j = i-1
    while j >=0 and minimo < v[j] : 
      v[j+1] = v[j] 
      j -= 1
    v[j+1] = minimo

  return v

def seleccion(v):
  n = len(v)
    
  for i in range(0, n): 
    id_min = i
    for j in range(i+1, n): 
      if v[id_min] > v[j]:
        id_min = j 
                       
    v[i], v[id_min] = v[id_min], v[i]

  return v

#------------------------------- EJERCICIO 3 ----------------------------------
def criba(n):
  marks = [True for i in range(n+1)]
  v=[]

  for i in range (2, int(m.sqrt(n))):
    if (marks[i == True]):
      for j in range(i*i, n+1, i):
        marks[j] = False

  for p in range(2, n+1):
    if marks[p]:
      v.append(p)
      
  return v

#------------------------------- EJERCICIO 4 ----------------------------------
def fib(n):
  
  if n<0: 
    return "Incorrect input"
  elif n==0: 
    return 0
  elif n==1: 
    return 1
  else: 
    return fib(n-1)+fib(n-2)

#------------------------------- EJERCICIO 5 ----------------------------------
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

#------------------------------- EJERCICIO 6 ----------------------------------

#Identificar cualquier palabra seguida de un espacio y una única letra mayúscula
def reg1(v):
  exp = re.findall(r'\w+ [A-Z] ', v)
  return ",".join(exp)

#Identificar correos electrónicos válidos
def reg2(v):
  exp = re.findall(r'\w+\@\w+\.\w+', v)
  return ",".join(exp)

#Identificar números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos
def reg3(v):
  exp = re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}|\d{4} \d{4} \d{4} \d{4}', v)
  return ",".join(exp)
