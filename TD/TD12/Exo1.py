from cmath import sin
import math
import numpy as np
from math import *
import matplotlib.pyplot as plt

f : lambda x, y : np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
z = sin(sqrt(x**2 + y**2))

x, y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
res = ax.plot_surface(X, Y, Z, cmap)