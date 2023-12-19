import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

face_c= misc.face()
dim = face_c.shape
l = dim[0]
L = dim[1]
l = int(l - l/4)
L = int(L - L/4)
zoom = face_c[l:l , L:L]
plt.imshow(zoom)
plt.show()
