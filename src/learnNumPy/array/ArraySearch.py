#search for a certain value, then return the indexes that have a match,
#we use the method where() which returns a tuple of indexes
import numpy as np

arr = np.array([2, 5, 1, 4, 5, 4, 4, 0])

x=np.where(arr==4) #find all the appearances of 4
y=np.where(arr%2==1) #find all the appearances of odd numbers
print(type(x))
print(x) #output: (array([3, 5, 6]),)
print(y) #output: (array([1, 2, 4]),)

print("#####")

arr=np.array([0, 1, 2, 5, 5, 7, 10, 25, 250])
#the method searchsorted(), which is assumed to be used in sorted arrays, performs
#a binary search to find the first index that inserting that number still maintains
#the order
x=np.searchsorted(arr, 5)
print(x) #output: 3

y=np.searchsorted(arr, 5, side='right') #search from the right side
print(y) #output: 5

#for multiple values:
z=np.searchsorted(arr, [3, 6, 9]) #z is an array
print(type(z))
print(z) #output: [3 5 6]