#Hardamard product
import numpy as np
# B=A=np.array([[0,2],[1,4]])
# print(A*B)

#Guassian Elimination Method

#Rules:
# 1 Addition or Substraction of two equations
# 2 Multiplication of an equation by Num
# 3 Switching Equations

M=np.array([[1,3,5],
            [2,2,-1],
            [1,3,2]])

y=np.array([[-1],[1],[2]])

sol=np.linalg.solve(M,y)
print(sol)


# A set of n linearly independent column