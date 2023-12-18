import numpy as np
import pandas as pd
from scipy import linalg
from scipy.linalg import lu,lu_factor,lu_solve
A=np.array([[2, -1,0], [-1, 2,-1], [0,-1,2]])
print("Matrix A=",A)
L=np.matrix([[1, 0,0], [-0.5,1,0], [0,-2/3,1]])
print("Matrix L=",L)
U=np.matrix([[2, -1,0], [0,3/2,-1], [0,0,4/3]])
print("Matrix U=",U)
b=np.array([[3],[6],[9]])
print("b =",b)
#Ax=b
#A=LU
#LUx=b
#Let Ux=z
#Lz=b
z = linalg.solve(L, b)
print("z =",z)
#Ux=z
x=linalg.solve(U,z)
print("x =",x)
# i=np.dot(U,x)
# print("i=",i)
# print(b-i)
# b-i