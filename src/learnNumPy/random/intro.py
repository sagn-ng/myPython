from numpy import random as rd

x=rd.randint(100) #generate a random number from 0 to 100
print(x)

x=rd.rand() #generate a random float between 0 and 1
print(x)

y=rd.randint(100, size=(5)) #generate a 1-D array of 5 random integers from 0 to 100
print(type(y)) #output: <class 'numpy.ndarray'>
print(y)

y=rd.randint(100, size=(2, 3)) #generate a 2x3 array containing 15 random integers from 0 to 100
print(y)

y=rd.rand(5) #generate a 1-D array of random floats between 0 and 1
print(y)

y = rd.choice([3, 5, 7, 9]) #generate a random number from a given list of values
print(y)