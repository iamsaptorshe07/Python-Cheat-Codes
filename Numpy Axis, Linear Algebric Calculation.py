# Axis = 0 Stands for coloumn
# Axis = 1 Stands for Row
import numpy as np
arr1 = np.array([[1,2,3],
                 [4,5,6]])
print(arr1)
print(arr1.sum(axis=0)) # Sum coloumn wise
print(arr1.sum(axis=1)) # Sum Row Wise

arr2 = np.array([[1,2,3],
                 [4,5,6]])

# Transpose Of any Matrix
arr2=arr2.transpose()
print(arr2)

# Performing Matrix Dot product ------> Shape of two Matrix must be diffrent
arr3=arr1.dot(arr2)   # In dot product we must do   product of two different types of matrix
print(arr3)


#Performing Matr Cross Product -------->Shape of Two Matrix must be same
arr4 = np.cross(arr1,arr2.transpose())
print(arr4)

# Perform Sorting Operation
import numpy as np
arr = np.array([[4,0,1],
                [3,-1,0]])
arr.sort(axis=0,kind='mergesort')
print(arr)
arr.sort(axis=1,kind='heapsort')
print(arr)
