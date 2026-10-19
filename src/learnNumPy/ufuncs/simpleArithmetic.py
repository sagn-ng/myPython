import numpy as np
arr1 = np.array([25, 11, 12, 13, 14, 15])
arr2 = np.array([2, 2, 4, 1, 3, 2])

newarr = np.add(arr1, arr2) #sum the content of 2 arrays, return the results in a new array
print(newarr)

print(np.subtract(arr1, arr2)) #subtraction: newarr[i] = arr1[i] - arr2[i]

print(np.multiply(arr1, arr2)) #multiplication: multiply the content of 2 arrays

#division (return float results), if we want integers, use floor_divide
print(np.floor_divide(arr1, arr2)) #newarr[i] = arr1[i] / arr2[i]

print(np.power(arr1, arr2)) #rise the values in the arr1 to the power of values in arr2

newarr=np.mod(arr1, arr2) #or remainder()
print(newarr) #newarr[i] = arr1[i] % arr2[i]

#the divmod() function returns both the quotients and the remainders in 2 arrays:
#the first one is for quotients, the second one is for remainders.
print(np.divmod(arr1, arr2))

print(np.absolute([-2, -5, -1, 0, 7, 10])) #return the absolute values