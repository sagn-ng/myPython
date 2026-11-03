import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'Finance', 'HR', 'Finance', 'IT'],

    'Gender': ['M', 'M', 'F', 'F', 'M'],

    'Salary': [2500, 1200, 1800, 2000, 1000],

    'Job review': ['great', 'mid', 'mid', 'great', 'low'],

    'Score': [100, 85, 80, 90, 84]
})

"""Dtype"""
print("dtype of the 'Score' column:", end=" ")
print(df.Score.dtype)

print()

print("dtype of every column in 'df':")
print(df.dtypes)


print("\nconvert a column of one type into another wherever such a conversion makes sense:")
eg_0=df.Score.astype('float64')
print(eg_0)

print("\nA DataFrame or Series also has its own dtype:")
print(df.index.dtype)
print(df['Job review'].dtype)

"""Missing data"""
#add an extra column for visualization:
df['Description']=['intelligent', 'hardworking', None, 'caring', None]

print()
eg_1=df[pd.isnull(df['Description'])] #show the rows that have 'NaN' value at the 'Description' attribute
print(type(eg_1))
print(eg_1)

print()
eg_2=df['Description'].fillna("Unknown") #replace 'NaN's in the 'Description' column with 'Unknown'
print(type(eg_2)) #eg_2 is a Series
print(eg_2)

print()
#replace all 'low's in the 'Job reviews' column with 'mid's
eg_3=df['Job review'].replace('low', 'mid') #eg_3 is a Series
print(eg_3)

print(df.shape[0])
