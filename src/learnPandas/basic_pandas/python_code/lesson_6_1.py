import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Gender': ['M', 'M', 'F', 'F', 'M'],
    'Salary': [2500, 1200, 1800, 2000, 1000],
    'Job review': ['great', 'mid', 'mid', 'great', 'low'],
    'Score': [100, 85, 80, 90, 84]
})
"""I. Renaming"""
"""I.1. Renaming columns"""
eg_0=df.rename(columns={'Score': 'points'}) #change the 'Score' column to 'points'
print(eg_0)

print()
"""I.2. Renaming rows"""
#rename the 0_th and 1_th indexed rows as 'firstEntry' and 'secondEntry'
eg_1=df.rename(index={0: 'firstEntry', 1: 'secondEntry'})
print(eg_1)

print()
"""I.3. Renaming the axis"""
#rename the index column as 'numbers' and add the name 'fields' for columns' names:
eg_2=df.rename_axis('numbers', axis='index').rename_axis('fields', axis='columns')
print(eg_2)

print()
"""II. Combining"""
"""II.1. concat()"""
temp1 = pd.DataFrame({'Name': ['A', 'B']})
temp2 = pd.DataFrame({'Name': ['C', 'D']})

eg_3 = pd.concat([temp1, temp2]) #axis=0
print(eg_3)

print()
"""II.2. join()"""
temp1 = pd.DataFrame({
    'Fruits': ['Apple', 'Banana', 'Blueberry', 'Orange'],
    'Score': [9.0, 8.0, 9.5, 9.25],
})
temp2 = pd.DataFrame({
    'Price': [10000, 7000, 12000, 11000],
    'Sold out': [True, False, False, True]
})

eg_4=pd.concat([temp1, temp2], axis=1) #or axis='columns'
print(eg_4)