import numpy as np
def myadd(x, y):
    return x+y
func = np.frompyfunc(myadd, 2, 1) #without this line, the result below would be [1, 2,..., 8]

#the 3 lines above are equivalent to np.add(), which is also a ufunc

print(func([1, 2, 3, 4], [5, 6, 7, 8])) #ufuncs perform element-wise operations, i.e in this case
#addition on single elements
#*note: 2 arrays must have the same size and the same data type

print(type(func)==np.ufunc) #check if a function is a ufunc
print(type(np.add)==np.ufunc)