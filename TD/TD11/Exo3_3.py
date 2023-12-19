import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

face= misc.face()
val , nb = np.unique(face, return_counts=True)
somme = np.cumsum(nb)
pixels = somme[len(somme)-1]
face[] = 255
face[] = 168
face[] = 84
face[] = 0