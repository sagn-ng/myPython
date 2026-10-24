import pandas as pd

"""DataFrame"""
data = {
  'Bob': ['I liked it.', 'It was awful.'],
  'Sue': ['Pretty good.', 'Bland.']
}

df = pd.DataFrame(data) #load data into a DataFrame object:
print(type(df))
print(df)

print("-"*50)
#Assign values for row labels
df_1=pd.DataFrame(data, index=['Product A', 'Product B'])
print(df_1)

print("-"*50)
"""Series"""
sr=pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(type(sr))
print(sr)

print("-"*50)
"""Reading data files"""
csv_path='src\\learnPandas\\data.csv'
eg=pd.read_csv(csv_path)
print(eg.shape) #table size
print("\nThe first 5 rows:")
print(eg.head())

print("\nThe last 5 rows:")
print(eg.tail())