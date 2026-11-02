import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Gender': ['M', 'M', 'F', 'F', 'M'],
    'Salary': [2500, 1200, 1800, 2000, 1000],
    'Job review': ['great', 'mid', 'mid', 'great', 'low'],
    'Score': [100, 85, 80, 90, 84]
})

eg_0=df.groupby(['Department', 'Job review'])['Score'].agg([len, min, max])
eg_0=eg_0.reset_index()
print(eg_0) #the sample DataFrame created with groupby()

"""Sorting"""
print()
#sort the data by a specific column
#to apply a descending sort, add the argument: ascending=False
eg_1=eg_0.sort_values(by='max')
print(eg_1)

#to sort by index values, use sort_index()
print()