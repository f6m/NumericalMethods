import matplotlib.pyplot as plt
import numpy as np
def y(n): return 1-n**3
npoints = np.linspace(0,10,11)
ynpoints = y(npoints)
print(ynpoints)
plt.plot(npoints, ynpoints,'o')
plt.show()
