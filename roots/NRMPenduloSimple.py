from sympy import *

y1,y2,y3,y4,y5=symbols('y1,y2,y3,y4,y5')

f1=3-2*y1+y2+0.111*sin(y1)
f2=y1-2*y2+y3+0.111*sin(y2)
f3=y2-2*y3+y4+0.111*sin(y3)
f4=y3-2*y4+y5+0.111*sin(y4)
f5=y4-2*y5+1+0.111*sin(y5)

from numpy import *


i=0 #Contador de iteraciones
d=0.0001 #presicion vertical
e=0.0001 #presicion horizontal
x=array([2,-1,1,1,2]) #vector inicial
N=10 #Numero maximo de iteraciones
print(i,x)


def G(x): return array([3-2*x[0]+x[1]+0.111*sin(x[0]),
x[0]-2*x[1]+x[2]+0.111*sin(x[1]),
x[1]-2*x[2]+x[3]+0.111*sin(x[2]),
x[2]-2*x[3]+x[4]+0.111*sin(x[3]),
x[3]-2*x[4]+1+0.111*sin(x[4])])

#matriz jacobiana evaluada en el punto inicial

def J(x): return array(
[[0.111*cos(x[0]) - 2,1,0,0,0],
[1,0.111*cos(x[1]) - 2,1,0,0],
[0,1,0.111*cos(x[2]) - 2,1,0],
[0,0,1,0.111*cos(x[3]) - 2,1],
[0,0,0,1,0.111*cos(x[4]) - 2]])

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
