import numpy as np
x=np.array([[1],[5],[9]])
y=np.array([[11],[15],[19]]).reshape(1,3)#Should Transpose  -> X.YT
z=np.array([[11],[15],[19]])
print(x)
print("---------------------------")
print(y)
print("---------------------------")
print(np.dot(x,y))
print("---------------------------")
print(np.dot(y,x))
print("---------------------------")
print(x.T@z)# @ -> dot product
