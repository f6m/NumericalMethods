from numpy import *
A=array([[1,0,0,4],[7,1,0,3],[0,0,1,2],[1,1,2,2]])
linalg.det(A)
b=array([1,2,3,4])
linalg.solve(A,b)
A.dot(linalg.solve(A,b))
