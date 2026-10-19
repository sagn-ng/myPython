import numpy as np

arr1 = np.array([1, 2, 3]) #1-D array

for x in arr1: print(x) #go through each element one by one
print("#####")
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) #2-D array
for x in arr2: print(x) #go through each row (1-D) one by one
#note: by this way, if we iterate through a n-D array, it'll go through (n-1)-dimension one by one

print("#####")
for x in arr2:
    for y in x: print(y) #return actual values (the scalars) by iterating in each dimension

print("#####")
#iterating on each scalar of a n-D array requires n for loop, making it difficult.
#we use nditer() instead:
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr2):
    print(x)

print("#####")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]): #iterate with step size (in this case, the step is 2)
    print(x) #output: 1 3 5 7 (each number sits in a line)