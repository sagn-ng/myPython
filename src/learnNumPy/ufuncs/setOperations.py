#We can use NumPy's unique() method to find unique elements from any array.
import numpy as np
x = np.unique([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(x) #ouput: [1 2 3 4 5 6 7]

arr1 = np.array([1, 2, 3, 3, 4, 2, 3])
arr2 = np.array([3, 4, 5, 6])

eg0 = np.union1d(arr1, arr2) #union of 2 arrays
print('Union:', eg0) #output: [1 2 3 4 5 6]

eg1 = np.intersect1d(arr1, arr2, assume_unique=False)

#note: if we know elements in arr1 are unique and so do elements in arr2,
# 'assume_unique=True' may speed up the computation. And if we're not sure,
#we must take False instead of True.
print('Intersection:', eg1)

eg2=np.setdiff1d(arr1, arr2, assume_unique=False) #the difference: arr1 / arr2
print('Difference of arr1 from arr2:', eg2)

eg3=np.setxor1d(arr1, arr2, assume_unique=False) #the symmetric difference
print('Symmetric difference of arr1 and arr2:', eg3)