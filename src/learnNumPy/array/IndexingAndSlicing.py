import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(arr1[0], arr1[2]+arr1[3]) #indexing on 1-D arrays

arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr2[0, 1]) #indexing on 2-D arrays

print("#####")
#We pass slice instead of index like this: [start:end]
#We can also define the step, like this: [start:end:step]
# *note: the result will exclude the index 'end'
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])   #slice from index 1 to 4
print(arr[2:])    #slice from index 2 to the end
print(arr[:4])    #slice from the beginning to index 3
print(arr[-3:-1]) #slice from the index 3 from the end to the last (excluded)