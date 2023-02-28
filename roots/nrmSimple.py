from sympy import * # todo de sympy
from numpy import *

#Simbolos para las variables independientes
y1,y2,y3,y4,y5=symbols('y1,y2,y3,y4,y5')

#Funciones multivariables coordenadas
f1=y1**2+y2**2-1
f2=y1**2-y2**2-1

i=0 #Contador de iteraciones
d=0.0001 #presicion vertical
e=0.0001 #presicion horizontal
x=array([10,10]) #vector inicial
N=10 #Numero maximo de iteraciones
print(i,x)

#Funcion no lineal multivariable a encontrarle un cero evaluadad en el punto inicial
def G(x): return array([x[0]**2+x[1]**2-1,
x[0]**2-x[1]**2-1])

#Matriz jacobiana de G evaluada en el punto inicial
def J(x): return array([[2*x[0],2*x[1]],[2*x[0],-2*x[1]]])

#Calcula el incremento para el vector 2, matriz inversa.
delta = linalg.solve(J(x), -G(x))

#norma entre el vector 1 y 2
norma = linalg.norm(x+delta - x)
#iteracion 1:
x=x+delta
i+=1
norma=linalg.norm(x+delta - x)
print(i,x,norma)

while linalg.norm(G(x))>d and norma>e and i<N:
 delta=linalg.solve(J(x),-G(x))
 norma=linalg.norm(x+delta - x)
 x=x+delta
 i+=1
 print(i,x,norma)
