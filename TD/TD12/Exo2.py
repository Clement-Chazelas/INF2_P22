import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

image = plt.imread('C:/Users/clemc/Desktop/UTC/TC02/INF2/TD/TD12/Photo.png')


plt.imshow(image[:,:,0], cmap='Reds')
plt.show()

im=image.copy()
im[:,:,0] = 0 
im[:,:,2] = 0 

im1=image.copy()
im1[:,:,0] = 0 
im1[:,:,1] = 0 

im2=image.copy()
im2[:,:,1] = 0 
im2[:,:,2] = 0 

im3=image.copy() 
im3[:,:,2] = 0 

mat = np.concatenate((im, im1) , axis = 1) 
mat2 = np.concatenate((im2, im3) , axis = 1) 
andy = np.concatenate((mat, mat2) , axis = 0) 

plt.imshow(andy)
plt.show()