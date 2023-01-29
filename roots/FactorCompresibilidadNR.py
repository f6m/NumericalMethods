from __future__ import division
#from sympy import *
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np
import matplotlib.pyplot as plt

#PARAMETROS DEL PROGRAMA: Num. max. de iteraciones n y tolerancias
n=50
e=0.0001
d=0.0001
#vectores para guardar la sucesión de factores de compresibilidad
Z=[]
Z1=[]

#FUNCIONES PARA EL METODO NUMERICO
#funcion a encontrar el cero f(V)=0
def func(V): 
  return ((R*T)/V)+(beta/(V**2))+(gama/(V**3))+(delta/(V**4))-P
def dfunc(V):
  return -((R*T)/(V**2))-((beta*2)/(V**3))-((gama*3)/(V**4))-((delta*4)/(V**5))
def nr(V):
  return V-(func(V)/dfunc(V))

#PARAMETROS DE LA FUNCION R,P,T,Ao,Bo,a,b,c
temperaturas = [273.15,473.15] #0C+273.15,200C+273.15
presiones = [1,2,5,10,20,40,60,80,100,120,140,160,180,200]

#iterar sobre los rangos de T,P
for T in temperaturas:
  for P in presiones:
    #T=temperaturas[0]
    #P=presiones[0]
    R=0.08205
    A0=2.2769
    B0=0.05587
    a=0.01855
    b=-0.01587
    c=128300
    beta=R*T*B0-A0-(R*c)/T**2
    gama=-R*T*B0*b+A0*a-(R*c*B0)/T**2
    delta=(R*B0*b*c)/T**2
    V0=(R*T)/P

#vector para guardar la sucecion de puntos obtenidos en una lista
    V=[V0]

#nuevo punto conforme al metodo de nr
    V1=nr(V0)

#guardamos el punto
    V.append(V1)

    Tiempo=[0,1]
    print(Tiempo,V)

    t=2
    while t <= n and np.abs(V1-V0) >= e and np.abs(func(V1)-func(V0)) >= d:
        t=t+1
        Tiempo.append(t)
        V0=V1
        V1=nr(V0)
        print(t,V1)
        V.append(V1)

#FACTOR DE COMPRESIBILIDAD de acuerdo a la temperatura
    if T == 273.15:
      Z.append((P*V1)/(R*T))
    else: Z1.append((P*V1)/(R*T))

#T.append(t+1)
#print(Tiempo)
#print(V)

plt.plot(presiones,Z,marker="o")
plt.plot(presiones,Z1,marker="o")
plt.xlabel('Presion')
plt.ylabel('Factor de compresibilidad - Metano')
plt.show()