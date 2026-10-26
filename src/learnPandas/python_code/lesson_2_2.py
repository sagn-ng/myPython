import pandas as pd

new_df=pd.DataFrame({
    'price': [15, 10, 20, 25],
    'name': ['Apple', 'Banana', 'Orange', 'Blueberry'],
    'discount (%)': [10, 7, 10, 25],
    'remaining quantity': [1200, 1000, 2500, 1000]
})


"""Manipulate the index"""
print("After set the 'name' field to be the label:")
print(new_df.set_index('name'))

print()
"""Conditional selection"""
print("check if each fruit's price is bigger than 12:")
x=(new_df.price>12) #x is a Series
print(type(x))
print(x)

print()
eg_2_0=new_df.loc[x] #or: new_df.loc[new_df.price > 12]
print(type(eg_2_0))
print(eg_2_0) #eg_2_0is a DataFrame

print("\nExtract fruits whose prices are >12 and discounts are >10%:")
eg_2_1=new_df.loc[(new_df.price>12) & (new_df['discount (%)']>10)]
print(eg_2_1)

print("\nSelect only 'Apple' and 'Orange':")
eg_2_3=new_df.loc[new_df.name.isin(['Apple', 'Orange'])]
print(eg_2_3)

"""Assigning data"""
print()
new_df['sold out']=False #it's like adding a new column
new_df['rank']=[1, 3, 2, 4]
print(new_df)