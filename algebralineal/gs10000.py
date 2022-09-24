# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 03:53:38 2022

@author: usuario
"""

#Aproximacion al sistema Ax=b mediante el método de Gauss-Seidel
#Definicion de las matrices para el esquema iterativo de Gauss-Seidel
from __future__ import division
from numpy import *
import scipy.linalg
#https://stackoverflow.com/questions/8905501/extract-upper-or-lower-triangular-part-of-a-numpy-matrix

#preciciones
d=0.0001
e=0.0001
N=100
M=10000
#descompocición para la matriz de coefs. y vector b, Ax=b
#A=array([[4,3,0],[1,7,1],[-1,1,3]])
A=array([[(i+j+M) if i==j else 1 for i in range(M)] for j in range(M)])
#P, L, U = scipy.linalg.lu(A) #Descomposicion LU para A
u=triu(A, k=1)
U=-u
l=tril(A, k=-1)
L=-l
D = diag(A)*identity(M) #Formamos la matriz con los elementos de la diagonal de A
#D=array([[4,0,0],[0,7,0],[0,0,3]])
Dinv=linalg.inv(D) #Inversa de la diagonal

#Dinv
#array([[ 0.25      ,  0.        ,  0.        ],
#       [ 0.        ,  0.14285714,  0.        ],
#       [ 0.        ,  0.        ,  0.33333333]])
#L=array([[0,0,0],[-1,0,0],[1,-1,0]])
#U=array([[0,-3,0],[0,0,-1],[0,0,0]])
#b=array([1,2,3])
b=array([i for i in range(M)])

#vector inicial 
#x0=array([1,1,1])
x0=array([1/(i+1) for i in range(M)])

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
#runfile('C:/Users/usuario/Documents/gs10000.py', wdir='C:/Users/usuario/Documents')
#1 [-0.00087876 -0.00072853 -0.00059503 ...  0.26918341  0.26918983
#  0.26919625]
#2 [-0.19239209 -0.19223448 -0.19207693 ...  0.28660635  0.28662
#  0.28663364]
#3 [-0.1401043  -0.13998151 -0.13985878 ...  0.28482241  0.28483682
#  0.28485122]
#4 [-0.1454458  -0.14531619 -0.14518663 ...  0.28479645  0.2848108
#  0.28482515]
#5 [-0.14552455 -0.14539545 -0.14526641 ...  0.28482162  0.28483596
#  0.28485031]
#6 [-0.14544909 -0.14532002 -0.145191   ...  0.2848199   0.28483425
#  0.28484859]
#7 [-0.14545422 -0.14532514 -0.14519611 ...  0.28481969  0.28483404
#  0.28484839]
#[-1.22498001e-03  9.98775649e-01  1.99877628e+00 ...  9.99700000e+03
#  9.99800000e+03  9.99900000e+03]
#[   0    1    2 ... 9997 9998 9999]