import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) #the original array remains unchanged

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr)) #sort an array of strings

arr=np.array([True, False, True])
print(np.sort(arr))