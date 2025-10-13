from __future__ import division
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np
from numpy import linalg
import matplotlib.pyplot as plt

#Numero maximo de iteraciones n
#Error en la aproximacion permitido: e(horizontal) y d (vertical)
n=100
e=0.0001
d=0.0001

#Sistema de ecuaciones para aproximar usando método de Gauss-Seidel explicito
#x-y=1/3
#-2x+y=-3
#Solución (8/3,7/3).

def f(x,y): return (1/3)+y
def g(x,y): return -3 + f(x,y)/6
def norma(a,b,c,d): return ((c-a)**2+(d-b)**2)**(0.5)

#punto inicial
x0=0.5 #inicial 1
y0=0.1 #inicial 2

#vectores para guardar la sucecion de coordenadas generadas en una lista
x=[x0]
y=[y0]

#nuevo punto conforme al metodo de Gauss-Seidel
x1=f(x0,y0)
y1=g(x0,y0)

#guardamos el punto
x.append(x1)
y.append(y1)

T=[0,1]
t=2
while t <= n and norma(x1,y1,x0,y0)>e and norma(f(x0,y0),g(x0,y0),f(x1,y1),g(x1,y1))>d:
    T.append(t)
    t=t+1
    x0=x1
    y0=y1
    x1=f(x0,y0)
    y1=g(x0,y0)
    print(t,x1,y1)
    x.append(x1)
    y.append(y1)

#T.append(t+1)
print(T,x,y)

plt.plot(T,x, marker="o")
plt.xlabel('Iteraciones')
plt.ylabel('Metodo del Gauss-Seidel')
plt.show()
