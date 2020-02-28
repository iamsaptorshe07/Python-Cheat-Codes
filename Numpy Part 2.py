# Different ways to creating numpy arrays
# row x coloumns
import numpy as np
arr1 = np.array([[2,3,4],[5,6,7]]) # This is the way to create a two dimensional array
print(arr1)
print(arr1.shape) # To know the shape of the array
print(arr1.dtype) # To know the Data Type containing by the Array

arr2 = np.zeros((2,4))  # It will create a 2 X 4 Matrix Array & This is the way to create an array containing zeroes
print(arr2)

arr3 = np.ones((4,5))  #This is the way to create an array containing ones
print(arr3)

arr4 = np.empty((2,3)) # Although most of the time np.zeroes() & np.empty() works simillarly but it is not completely true ,
print(arr4)      # as np.zeroes will contain items the value with exact zero but np.empty() some time contains gurbage value.

