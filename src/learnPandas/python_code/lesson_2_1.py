import pandas as pd

data = {
  "calories": [420, 380, 390, 250],
  "duration": [50, 40, 45, 10]
}

reviews = pd.DataFrame(data)
print()

"""Native accessors"""
print("access a column:")
eg_0=reviews.calories #eg_0 is a Series, or we can use reviews['calories']
print(type(eg_0))
print(eg_0)

print("\ndrill down to a specific cell:")
print(reviews['calories'][2]) #row number 2 of the 'calories' column

print()
"""Indexing in pandas"""
print("\nIndex-based selection (iloc)")
#select the first row
eg_1=reviews.iloc[0] #eg_1 is also a Series
print(type(eg_1))
print(eg_1)

print()
#select row 0 and 3, column 0 and 1
eg_2=reviews.iloc[[0, 3], [0, 1]] #eg_2 is a DataFrame
print(type(eg_2))
print(eg_2)

print()
print("\nLabel-based selection (loc):")
eg_3=reviews.loc[[0, 3], ['calories', 'duration']] #it yields the same result as iloc[[0,3], [0,1]]
print(eg_3)