import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1)
print(arr1[0:5])
print(arr1.size)
print(arr1[::-1])


#Copying a Array
arr2 = arr1[5:].copy()
print(arr2)

#Reverse an Array
arr3 = arr1[::-1].copy()
print(arr3)