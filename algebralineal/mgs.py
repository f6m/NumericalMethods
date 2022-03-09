#Aproximacion al sistema Ax=b mediante el método de Gauss-Seidel
#Definicion de las matrices para el esquema iterativo de Gauss-Seidel
from numpy import *
#preciciones
d=0.0001
e=0.0001
N=100
#descompocición para la matriz de coefs. y vector b, Ax=b
A=array([[4,3,0],[1,7,1],[-1,1,3]])
D=array([[4,0,0],[0,7,0],[0,0,3]])
Dinv=linalg.inv(D)
#Dinv
#array([[ 0.25      ,  0.        ,  0.        ],
#       [ 0.        ,  0.14285714,  0.        ],
#       [ 0.        ,  0.        ,  0.33333333]])
L=array([[0,0,0],[-1,0,0],[1,-1,0]])
U=array([[0,-3,0],[0,0,-1],[0,0,0]])
b=array([1,2,3])

#vector inicial 
x0=array([1,1,1])

#primera iteración
n=1
x1=matmul(matmul(linalg.inv(D-L),U),x0)+matmul(linalg.inv(D-L),b)

# Esquema iterativo de Jacobi, xn+1=(D-L)^-1Uxn+(D-L)^-1b
while(n<N and linalg.norm(x1-x0) > e and linalg.norm(matmul(A,x1)-matmul(A,x0)) > d):
	print(n,x1)
	x0=x1
	x1=matmul(matmul(linalg.inv(D-L),U),x0)+matmul(linalg.inv(D-L),b)
	n=n+1

#Comprobacion:

print(matmul(A,x1))
print(b)	
#plot 3D
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
