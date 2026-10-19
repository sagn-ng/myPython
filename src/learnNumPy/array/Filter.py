import numpy as np

arr = np.array([41, 42, 43, 44])
#If the value at an index is True that element is contained in the filtered array,
#if the value at that index is False that element is excluded from the filtered array.
x = arr[[True, False, True, False]]
print(x) #output: [41 43]

print("#####")
#create the filter array
arr=np.array([0, 1, 2, 5, 5, 7, 10, 25, 250])
filter_arr=[]
for x in arr:
    if x>5: filter_arr.append(True)
    else: filter_arr.append(False)

newarr=arr[filter_arr]
print(len(newarr))
print(filter_arr)
print(newarr)

print("#####")
#create directly from the original array:
filter_arr=arr>5
newarr=arr[filter_arr]
print(newarr)