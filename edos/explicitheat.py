from numpy import *
#Declaramos la matriz y el vector de las condiciones iniciales
A=array([[-49,25,0,0],
	[25,-49,25,0],
	[0,25,-49,25],
	[0,0,25,-49]])

u=array([1/5,2/5,3/5,4/5])
j=0;
N=5;

#Mostramos los valores u_i,j+1 subsecuentes para j=0,1,2,3
while j<=N:
	print(j)
	print(u)
	v=matmul(A,u)
	j=j+1
	u=v
