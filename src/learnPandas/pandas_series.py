import pandas as pd
"""A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type."""

a = [1, 7, 2]

myvar = pd.Series(a)
print(type(myvar)) #<class 'pandas.Series'>
print(myvar)
print()
#If nothing else is specified, the values are labeled with their index number: 0, 1, 2,..
#use the 'index' argument to name our own labels
x1, x2, x3=2, 5, 10
myvar=pd.Series(a, index=[x1, x2, x3])
print(myvar)
print()
#access an item by its label:
print(myvar[x1]) #output: 1
print()

#we can also use a key/value object (like a dict) - the keys become the labels
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print()
#to select only some items, list them in the 'index' argument:
var2=pd.Series(calories, index=["day1", "day2"])
print(var2)