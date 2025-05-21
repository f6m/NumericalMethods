from numpy import *
#Declaramos la matriz de coeficientes y el vector del lado derecho
A=array([[26,-12.5,0,0],
	[-12.5,26,-12.5,0],
	[0,-12.5,26,-12.5],
	[0,0,-12.5,26]])
u=array([1/5,2/5,3/5,4/5])
j=0;
N=10;

#Imprimimos los valores u_i,j+1 subsecuentes para j=0,1,2,3
while j<=N:
	print(j)
	v=linalg.solve(A,u)
	print(v)
	j=j+1
	u=v
