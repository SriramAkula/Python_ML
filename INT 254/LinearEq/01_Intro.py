# System of Linear Eq
# x + 2y = 8
# 5x -  3y = 1

import numpy as np
# A=np.array([[0,2]   # 1st row
#             ,[1,4]]) #2nd row
# B=np.array([[3,1]   # 1st row
#             ,[3,-2]]) #2nd row
# print(A)
# print(A.shape)
# print("----------------------")
# print(B)
# print(B.shape)
# print("----------------------")
# print(A+B)
# print(np.add(A,B))
# print("----------------------")

# A=np.array([[1,2,3],[4,5,6],[7,8,9]])
# B=np.array([[9,2,8],[7,-5,6],[5,2,0]])
# print(A)
# print("----------------------")
# print(B)
# print("----------------------")
# C=np.add(A,B)
# print(C)
# print("----------------------")

#Matrix Scalar Multiplication

# A=np.array([[1,2,3],[4,5,6],[7,8,9]])
# alpha=2
# print(A*alpha)

#Matrix Vector Multiplication
A=np.array([[0,2]   # 1st row
             ,[1,4]])
x=np.array([[1],[2]])
print(A@x)
print("----------------------")
C=np.dot(A,x)
print(C)
print("----------------------")
C=np.dot(A.T,x)
print(C)