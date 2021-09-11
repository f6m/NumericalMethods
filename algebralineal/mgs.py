# Aproximacion al sistema Ax=b mediante el método de Gauss-Seidel
# Definicion de las matrices para el esquema iterativo de Gauss-Seidel
import numpy
D=numpy.array([[4,0,0],[0,7,0],[0,0,3]])
Dinv=numpy.linalg.inv(D)
Dinv
array([[ 0.25      ,  0.        ,  0.        ],
       [ 0.        ,  0.14285714,  0.        ],
       [ 0.        ,  0.        ,  0.33333333]])
L=numpy.array([[0,0,0],[-1,0,0],[1,-1,0]])
U=numpy.array([[0,-3,0],[0,0,-1],[0,0,0]])
b=numpy.array([1,2,3])
x0=numpy.array([1,1,1])

# Esquema iterativo de Gauss-Seidel, repetir
x1=numpy.matmul(numpy.matmul(numpy.linalg.inv(D-L),U),x0)+numpy.matmul(numpy.linalg.inv(D-L),b)

