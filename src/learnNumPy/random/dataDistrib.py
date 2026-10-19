#We can generate random numbers based on defined probabilities using
#the choice() method of the random module.

#The choice() method also allows specifying the probability for each value.
from numpy import random
import numpy as np

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10)) #return an array of 10 numbers
#the corresponding probabilities of 3, 5, 7, 9 are 0.1, 0.3, 0.6
print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)) #return a 2-D array
print(x)

print("#####")
# - shuffle() re-arranges the original array
# - permutation() returns a re-arranged array while leaving the original one unchanged
arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
print(random.permutation(arr)) #return a random permutation of 'arr'