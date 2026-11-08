import pandas as pd

df=pd.DataFrame({
    'name': ['Apple', 'Banana', 'Orange', 'Blueberry'],
    'price': [15, 10, 20, 25],
    'discount (%)': [10, 7, 10, 25],
    'remaining quantity': [1200, 1000, 2500, 1000],
    'rank': [1, 3, 2, 4]
})
print(df)

print('\nSummary functions')
print('#####')
print(df.price.describe())

print(f'\nThe average price: {df.price.mean()}')

print('\nMaps')
print('#####')
"""map()"""
mean_price=df.price.mean()
eg_1=df.price.map(lambda x: x-mean_price)
print(type(eg_1)) #Series
print(eg_1)
#i.e: replace all values X in 'price' with X - avg(price), leaving 'df' unchanged.

print()
"""apply()"""
eg_4=df.apply(
    lambda row: row['price']-row['price']*row['discount (%)']/100,
    axis=1)
print(eg_4)

print()
eg_5=df.copy()
eg_5['price after discount']=eg_4
print(eg_5)