from __future__ import division
#from sympy import *
import math
from numpy import cos,sin,log #funciones cos, sin de numpy
import numpy as np #numerical python como np

#Num. max. de iteraciones n y tolerancias
n=100
e=0.000001
d=0.000001

#funcion a encontrar el cero f(x)=0, actual : Ecuacion de Colebrook-White
def func(x): 
  #return ((40 + 1.1474/(x*x))*(x - 0.03985)) - 0.08314*200
  #return x**5 - sin(x) + 3
  return (1/x**(0.5))-1.14+2*log((0.001/0.025)+(0.19/(3*10**4*x**(0.5))))

#el intervalo de busqueda
x1=.01 #inicial 1
x2=10 #inicial 2

if func(x1)*func(x2)>0:
  print("No hay raiz en el intervalo","[",x1,x2,"]")
  exit()

#biseccion,nuevo punto medio
x3=(x1+x2)/2
t=0

#vector para guardar la sucecion de puntos medios obtenidos y 
#sus respectivos valores de la función objetivo en unas listas
#el contador de iteraciones en una tercera lista

x=[x3]
fx=[func(x3)]
T=[t]

while t <= n and np.abs(x3-x2) >= e and np.abs(func(x3)-func(x2)) >= d:
    print(t,x3,func(x3))
    t=t+1
    T.append(t)
    if (func(x1)*func(x3)<0):
       x2=x3
    else :x1=x3
    x3=(x1+x2)/2
    x.append(x3)
    fx.append(func(x3))

T.append(t+1)

import matplotlib.pyplot as plt
#print(T,x)

plt.plot(x,fx)
plt.xlabel('Busqueda binaria - Puntos medios')
plt.ylabel('F(punto medio)')
plt.show()
