''' Performing some mathematical operation on numpy array'''

# Note  : Not Linear Algebric Calculation

import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = arr1 + arr2
arr4 = arr1 * arr2
arr5 = arr1 ** arr2
print(arr1,end='\n')
print(arr2,end='\n')
print(arr3,end='\n\n')
print(arr4,end='\n\n')
print(arr5,end='\n')

# It performs element wise opeartions