import numpy as np
x,y=np.array([[-2],[2]]),np.array([[4],[-3]])
distance=np.linalg.norm(x-y,2)
print(distance)