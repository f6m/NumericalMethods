from numpy import *
#preciciones
d=0.0001
e=0.0001
N=100
#descompocición para la matriz de coefs. y vector b, Ax=b
A=array([[4,3,0],[-1,1,3],[1,7,1]])
D=array([[4,0,0],[0,1,0],[0,0,1]])
Dinv=linalg.inv(D)

L=array([[0,0,0],[1,0,0],[-1,-7,0]])
U=array([[0,-3,0],[0,0,-3],[0,0,0]])
b=array([1,2,3])

#vector inicial 
x0=array([1,1,1])

#primera iteración
n=1
x1=matmul(matmul(Dinv,U+L),x0)+matmul(Dinv,b)

# Esquema iterativo de Jacobi, xn+1=D^-1(L+U)xn+D^-1b
while(n<N and linalg.norm(x1-x0) > e and linalg.norm(matmul(A,x1)-matmul(A,x0)) > d):
	print(n,x1)
	x0=x1
	x1=matmul(matmul(Dinv,U+L),x0)+matmul(Dinv,b)
	n=n+1

#Comprobacion:

print(matmul(A,x1))
print(b)
