import numpy as np
#Matrix Inverse

A=np.array([[1,2,1],[4,4,5],[6,7,7]])
A_inverse=np.linalg.inv(A)
print(A_inverse)
I=A@A_inverse
I=np.round(I)
print("Identity \n",I)
print("---------------------")


#Matrix Transpose
A=np.array([[1,2,1],[4,4,5]])
print(A)
print(A.shape)
print("\n")
A_T=A.T
print(A_T)
print(A_T.shape)
print("---------------------")