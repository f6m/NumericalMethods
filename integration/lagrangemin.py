from sympy import *
from numpy import *
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [654553,799389,966842,1162375]

pl = lagrange(x, y)

print(pl)
print(pl(5))

xn = arange(-0.1, 5.1, 0.1)

plt.plot(xn, pl(xn), 'b', x, y, 'ro')
plt.title('Polinomio de Lagrange')
plt.grid()
plt.xlabel('x')
plt.ylabel('p')
plt.show()
