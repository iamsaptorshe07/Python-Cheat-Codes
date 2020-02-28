'''
-------------------------------Numpy Stands for Numerical Python-------------------------------
'''
import numpy as np
lst = []
size = int(input('Enter the size of the array :'))
for i in range(size):
    item = int(input('Enter integer type item :'))
    lst.append(item)
lst = np.array(lst)      # This is one way to convert one list to an array using numpy.array(list_name)
print(lst)
print(type(lst))
