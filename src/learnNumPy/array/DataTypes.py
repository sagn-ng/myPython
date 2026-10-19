#read more about the list of data types in NumPy at: https://www.w3schools.com/python/numpy/numpy_data_types.asp
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S') #create an array with a defined data type
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i') #convert the data type on the existing array
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool) #convert from integer -> boolean
print(newarr)
print(newarr.dtype)