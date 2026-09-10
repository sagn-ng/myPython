#normal boolean values:
print(10>9) #output: True

#evaluate values with True or False in return:
print(bool(10), end=" ")
print(bool("hello"))

#exceptions: all of these expressions below return False:
print(bool(0), end=" ")
print(bool(""), end=" ")
print(bool(()), end=" ")
print(bool([]), end=" ")
print(bool({}), end=" ")
print(bool(None))

#isinstance() function:
x=25
print(isinstance(x, int)) #output: True