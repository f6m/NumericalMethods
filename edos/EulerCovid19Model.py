#Simulacion del modelo epidemiologico 
#https://modelo.covid19.cdmx.gob.mx/modelo-epidemico
#falta la condicion inicial S+ E +I + L + G + H + ICU + R+ M=1

from __future__ import division
from sympy import *
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np

h=1/5 #tamano de paso
t=0 #valor inicial del tiempo
z=np.array([0,0,0,0,0,1,1,1,1]) #vector inicial en t=0
#   S,   E,   I,   L,   G,   H, ICU,   R,  M
#z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8]

Ro=2.83
Dm=8
Dricu=7
Dicu=1
pm=0.03
Drh=12
picu=0.05
Dhosp=4
Drl=14
pgrave=13.8
Dincub=5.2
Dinfect=5.9

time=[t] #Guardamos el tiempo en una lista
CV19=[z] #Guardamos el tiempo en una lista el vector inicial de longitud 9
M=[z[8]] #Muertos

# vector en R^2 derivada
def D(z): return np.array([-(Ro/Dinfect)*z[2]*z[0],
            (Ro/Dinfect)*z[2]*z[0]-(1/Dincub)*z[1],
                  (1/Dincub)*z[1]-(1/Dinfect)*z[2],
          (1-pgrave)*(1/Dinfect)*z[2]-(1/Drl)*z[3],
              (pgrave/Dinfect)*z[2]-(1/Dhosp)*z[4],
              (1/Dhosp)*z[4]-(1-picu)*(1/Drl)*z[5]-(picu/Dicu)*z[5],
            (picu/Dicu)*z[5]-(1-pm)*(1/Dricu)*z[6]-(pm/Dm)*z[6],
          (1/Drl)*z[3]+(1-picu)*(1/Drh)*z[5]+(1-pm)*(1/Dricu)*z[6],
                           (pm/Dm)*z[6]])


print(t,z)
zth=z+h*D(z)

while(t <= 5):
    z=zth
    t=t+h
    time.append(t) #Guardamos el tiempo en una lista
    CV19.append(z) #Guardamos el tiempo en una lista
    M.append(z[8])
    print(t,z)
    zth=z+h*D(z)

import matplotlib.pyplot as plt

plt.plot(time, M)
plt.xlabel('Tiempo')
plt.ylabel('Muertos*')
plt.show()
