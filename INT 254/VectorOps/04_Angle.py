import numpy as np
x,y=np.array([[2],[0]]),np.array([[0],[2]])
#Angle b/w Vectors
cos_theta = (x.T@y)/((np.linalg.norm(x,2))*(np.linalg.norm(y,2)))
print(cos_theta)
cos_theta=np.round(cos_theta,3)
print(cos_theta)
cos_inverse=np.arccos(cos_theta)#arcsin -> sin inverse
print(cos_inverse)
degree=cos_inverse*((180)/np.pi)
print(degree)