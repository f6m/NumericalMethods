from __future__ import division
import math
from sympy import *
from numpy import cos,sin,log,tanh #funciones cos, sin de numpy
import numpy as np #numerical python como np
import matplotlib.pyplot as plt

#Numero maximo de iteraciones n
#Error en la aproximacion permitido: e(horizontal) y d (vertical)
n=100
e=0.0001
d=0.0001

#funcion para encontrar el cero f(x)=0
#def func(x): return ((5/tanh((2*9.8*x)**(0.5)*(2.5/8)))**(2))/(2*9.8)
  #return (1.14-2*log((0.0025/0.1)+(9.35/(3*10**4*f**(0.5)))))**(-2)
def funx(x): return (2*9.8*x)**(0.5)*tanh((2*9.8*x)**(0.5)*(2.5/8))-5
#def funr(r): return (2*9.8*r)**(0.5)*((exp((2*9.8*r)**(0.5)*(2.5/8))-exp((2*9.8*r)**(0.5)*(-2.5/8)))/(exp((2*9.8*r)**(0.5)*(2.5/8))+exp((2*9.8*r)**(0.5)*(-2.5/8))))-5
#4+0.0333*sin(2*x)
#return ((40 + 1.1474/(x*x))*(x - 0.03985)) - 0.08314*200

#f=((5*exp((2*9.8*r)**(0.5)*(-2.5/8))+exp((2*9.8*r)**(0.5)*(2.5/8)))/(exp((2*9.8*r)**(0.5)*(-2.5/8))-exp((2*9.8*r)**(0.5)*(2.5/8))))**(2)/(2*9.8)
#ff=diff(funr(r),r,1)
#print(ff)
#f1=lambdify(r,ff)
#print(f1(2))

#puntos iniciales
x0=0 #inicial 1
x1=3

if(funx(x0)*funx(x1)<0):
  print("si hay raiz en el intervalo","[",x0,x1,"]")
else: 
  print("si hay raiz en el intervalo","[",x0,x1,"]")
  exit(1)
#print(funx(x0),funr(x0))

#x2=0.8 #inicial 2
#print(x0,func(x0),ff(x0),func(x0)/ff(x0))
#vector para guardar la sucecion de puntos obtenidos en una lista
x=[x0,x1]
print(x0,x1,funx(x0),funx(x1))
#nuevo punto conforme al metodo de la secante

x2=x1-(funx(x1)*(x1-x0))/(funx(x1)-funx(x0))

#guardamos el punto
x.append(x2)
print(x2,funx(x2))
T=[0,1,2]

#print(T,x)

t=3
while t <= n and np.abs(x2-x1) >= e and np.abs(funx(x2)) >= d:
    T.append(t)
    t=t+1
    #x1=func(x0)
    #print(funr(x0))
    x2=x1-(funx(x1)*(x1-x0)/(funx(x1)-funx(x0)))
    if (funx(x2)*funx(x1)<0):
        x0=x2
    else: x1=x2
    print(t,x2,funx(x2))
    x.append(x2)

#T.append(t+1)
print(T,x)


plt.plot(T,x, marker="o")
plt.xlabel('Iteraciones')
plt.ylabel('Metodo de la falsa posición')
plt.show()
