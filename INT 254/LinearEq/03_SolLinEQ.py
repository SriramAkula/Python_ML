# Solving Linear Equations using Gauss Jordan Method
# x+3y+z=7
#6x+7y-2z=0
#-2x-3y+2z=0
import numpy as np
A=np.array([[1,1,1],[1,2,3],[2,3,4]])
B=np.array([[2],[5],[11]])
A_I=np.linalg.inv(A)
Sol=A_I@B
print(Sol)