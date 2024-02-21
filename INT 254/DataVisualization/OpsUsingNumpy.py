import numpy as np
distance = [10,15,17,26]
time=[0.3,0.47,0.55,1.20]
#speed=distance/time List Operations not allowed in python, hence we use numpy arrays
np_distance=np.array(distance)
np_time=np.array(time)
np_speed=np_distance/np_time
print("-------------------------------")
print(np_speed)
print("-------------------------------")

#Classes ANd Attributes of n-dimensional array
np_city=np.array(['NYC','LA','Miami','Jalandhar','Tanuku'])
print(np_city.ndim) #.ndim is an attribute which tells us dimensions of array...
print("-------------------------------")

np_city_with_state=np.array([['NYC','Tanuku','NDD'],['NY','AP','AP']])
print(np_city_with_state.ndim)
print(np_city_with_state.shape)

#Basic operations of an array

first_trail_cyclist=[10,15,17,18]
sec_trail_cyclist=[12,19,27,8]

np_first=np.array(first_trail_cyclist)
np_sec=np.array(sec_trail_cyclist)

tot_dist=np_first+np_sec
print(tot_dist)
print("-------------------------------")

n_sub=np_first-np_sec
print(n_sub)
print("-------------------------------")


n_mul=np_first*np_sec
print(n_mul)
print("-------------------------------")

n_div=np_first/np_sec
print(n_div)
print("-------------------------------")

#LOGICAL OPS
n= np_first.__and__( np_sec) # n1 & n2 also works
print(n)

# Bitwise Ops
n=np_first&np_sec
print(n)
n=np_first|np_sec
print(n)
n=~np_sec
print(n)
n=np_first^np_sec
print(n)

# Accessing Array Elements
first=[10,15,35,54]
second=[12,43,21,37]
n_2d=np.array([first,second])
print(n_2d[0])
print(n_2d[1])
print(n_2d[1][3])
print(n_2d[:,1])
print(n_2d[:,1:3])

#Access elements: Iteration

print("Array using iteration: ")
for i in n_2d:
    print(i)

print(n_2d.size)


#Indexing with boolean Arrays
test_score=np.array([[83,71,98,60],[34,87,56,40]])
pass_score=test_score>60
print("\n")
print(pass_score)
print("\n")
print(test_score[pass_score])


#Copy & Views
np_arr1=np.array([1,2,3,4,5])
np_arr2=np_arr1 #Copying arr1 to arr2
print(np_arr1 is np_arr2)

#View or Shallow copy
np_arrView=np_arr1.view()
print(np_arrView)
print(len(np_arrView))

# In view or shallow copy the original value also changes for the changes in view

np_arrView[3]=20
print(np_arrView)
print(np_arrView is np_arr1) # Creates a copy as another obj but changes in copy will effect original.
print(np_arr1)
print("\n")
# Deep Copy : The Original Array is preserved
n_arrDeep=np_arr1.copy()
print(n_arrDeep)
print(n_arrDeep is np_arr1) # Both are different(Copy Function creates different objects with same element)
n_arrDeep[2]=4
print(n_arrDeep)
print(np_arr1)


# Universal Functions
# sqrt,cos,floor,exp
print("\n")
np_sqrt = np.sqrt(np_distance)
print(np_distance)
print(np_sqrt)

print(np.cos(0))

from numpy import pi

print(np.sin(pi/2))
print(np.cos(pi))

print(np.floor([1.5,8.6,3.6]))
print(np.exp([0,1,5]))

# Shape Manipulation
# ravel, split, flatten, resize, reshape , stack

np_arr2=test_score
print(np_arr2)
n_ravel=np_arr2.ravel()
n_flatten=np_arr2.flatten() #Convert to 1D array along it creates a copy
print(n_ravel)
print(n_flatten)

n_ravel[3]=0 
print(np_arr2)  # Changes in ravel results in the change in Original
n_reshape=np_arr2.reshape(8,1) #Multiplication of elements should be equal to no of elements
print(n_reshape)

print(np.hsplit(np_arr2,4))
print(np.hstack((np_arr2,np_arr2)))