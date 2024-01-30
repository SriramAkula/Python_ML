import numpy as np
#L2 Norm (Eulidean Norm) -> pythogorous triplet
x=np.array([[3],[-4]])
Res=np.linalg.norm(x,2)  #2 because L2
print(Res)
#L1 Norm (Manhattan Norm) -> absolute value
Res=np.linalg.norm(x,1) #1 because L1
print(Res)
#Max Norm
Res=np.linalg.norm(x,np.inf) #np.inf because infinity(max norm)
print(Res)