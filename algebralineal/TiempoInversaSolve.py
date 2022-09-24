# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 02:14:54 2022

@author: usuario
"""
N=10000
from numpy import *
#values=array([i for i in range(N)])
A=array([[(i+j+N) if i==j else 1 for i in range(N)] for j in range(N)])
b=[i for i in range(N)]
#print(values)
print(A)
print(b)
print(linalg.det(A))
print(linalg.solve(A,b)) #Con un algoritmo de python
#print(linalg.inv(A).dot(b)) #Con el calculo de la inversa
#print(linalg.det(A))