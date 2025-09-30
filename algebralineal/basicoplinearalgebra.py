from numpy import *
#Matriz cuadrada
A=array([[1,0,0,4],[7,1,0,3],[0,0,1,2],[1,1,2,2]])
linalg.det(A)
b=array([1,2,3,4])
linalg.solve(A,b)
A.dot(linalg.solve(A,b))

#Matriz con mas ecuaciones que variables
C=array([[1,1],[2,1],[0,1]])
b=array([1,2,3])
x,residuo,rango, s=linalg.lstsq(C,b,rcond=None)
print(x)

#Matriz con mas ecuaciones que variables
D=array([[1,1,1],[0,1,2]])
b=array([1,2])
Ap=linalg.pinv(D)
print(Ap)
x=dot(Ap,b)
print(x)
