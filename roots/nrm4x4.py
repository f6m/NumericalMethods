#Aplicacion del metodo de Newton-Raphson multivariable a G(x)=0
#ejecucion python NRM.py

from sympy import * # todo de sympy

#Simbolos 
y1,y2,y3,y4=symbols('y1,y2,y3,y4')

#Funciones multivariables coordenadas G(f1,f2,f3,f4,f5)
f1=y2-2*y1-0.06324616*sqrt(y2)
f2=y3-2*y2+y1-0.06324616*sqrt(y3-y1)
f3=y4-2*y3+y2-0.06324616*sqrt(y4-y2)
f4=2-2*y4+y3-0.06324616*sqrt(2-y3)

import numpy as np #numerical python como np

x=np.array([0.5,0.6,0.7,0.8],dtype=np.float64) #vector inicial aleatorio
N=100 #Numero maximo de iteraciones

#Funcion no lineal multivariable a encontrarle un cero, usamos x[0]=y1,...,x[4]=y5
def G(x): return np.array([x[1]-2*x[0]-0.06324616*sqrt(x[1]),
x[2]-2*x[1]+x[0]-0.06324616*sqrt(x[2]-x[0]),
x[3]-2*x[2]+x[1]-0.06324616*sqrt(x[3]-x[1]),
2-2*x[3]+x[2]-0.06324616*sqrt(2-x[2])],dtype=np.float64)

#Matriz jacobiana de G en vectores fila
k=0.03162308
def J(x): return np.array([[-2,1-k*sqrt(x[1]**(-3)),0,0],
[1+k*sqrt((x[2]-x[0])**(-3)),-2,1-k*sqrt((x[2]-x[0])**(-3)),0],
[0,1+k*sqrt((x[3]-x[1])**(-3)),-2,1-k*sqrt((x[3]-x[1])**(-3))],
[0,0,1+k*sqrt((2-x[2])**(-3)),-2]],dtype=np.float64)

#Calcula el incremento para el vector 2
delta = np.linalg.solve(J(x),-G(x))

#norma entre el vector 1 y 2
norma = np.linalg.norm(x+delta - x)

i=0 #Contador de iteraciones
d=0.0001 #presicion vertical
e=0.0001 #presicion horizontal

while np.linalg.norm(G(x))>d and norma>e and i<N:
 delta=np.linalg.solve(J(x),-G(x))
 norma=np.linalg.norm(x+delta - x)
 x=x+delta
 i+=1

print(x)
print(i)
print(np.linalg.norm(G(x)))
print(norma)
