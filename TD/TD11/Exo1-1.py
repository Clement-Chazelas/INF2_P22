from random import randint
from numpy import *

def Matrice(n, m) :
    matrice = random.randint(0, 10, [n,m])
    matrice3 = c_[matrice, ones(matrice.shape[0])]
    print(matrice3)

Matrice(8,8)