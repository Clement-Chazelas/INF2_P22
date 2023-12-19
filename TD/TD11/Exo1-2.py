from numpy import *

def MatriceImage(n) :
    A = random.randint(0, 255, (n,n))
    A[0:2, :] = 0
    A[:, 0:2] = 0
    A[n-2:n, :] = 0
    A[:, n-2:n] = 0
    print(A)

MatriceImage(10)