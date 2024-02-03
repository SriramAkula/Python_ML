# Solving Linear Equations using Gauss Jordan Method
# x+3y+z=7
#6x+7y-2z=0
#-2x-3y+2z=0
import numpy as np
A=np.array([[1,3,1],[6,7,-2],[-2,-3,2]])
B=np.array([[7],[0],[0]])
A_I=np.linalg.inv(A)
Sol=A_I@B
print(Sol)