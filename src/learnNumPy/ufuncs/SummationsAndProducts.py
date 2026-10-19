import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
arr3 = np.array([2, 3, 4])

print(np.sum([arr1, arr2])) #the sum of all the elements in 2 arrays
print(np.prod([arr1, arr2])) #the product of all the elements in 2 arrays

#adding 'axis=1' means performing summations/multiplications on each array
newarr=np.sum([arr1, arr2], axis=1)
print(newarr)
newarr=np.prod([arr1, arr2, arr3], axis=1)
print(newarr)

newarr=np.cumsum(arr1) #cummulative sum: newarr[i] = arr1[0]+...+arr1[i]
print(newarr) #output: [1, 3, 6]
newarr=np.cumprod(arr3) #cummulative product: newarr[i] = arr3[0]*...*arr3[i]
print(newarr) #output: [2, 6, 24]