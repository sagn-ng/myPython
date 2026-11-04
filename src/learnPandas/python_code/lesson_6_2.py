import pandas as pd

temp1 = pd.DataFrame({
    'City': ['Hanoi', 'HCM']
}, index=['A', 'B'])

temp2 = pd.DataFrame({
    'Population': [8, 9]
}, index=['A', 'B'])

eg_5=temp1.join(temp2) #'temp1' and 'temp2' remain unchanged
print(eg_5)

print()
"""II.3. merge()"""
temp1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Fruits': ['Apple', 'Banana', 'Blueberry', 'Orange'],
    'Score': [9.0, 8.0, 9.5, 9.25],
})
temp2 = pd.DataFrame({
    'id':[1, 2, 5],
    'Sold out': [True, False, True]
})

eg_6=pd.merge(temp1, temp2) #by default: how='inner'
print(eg_6)

print()
eg_7=pd.merge(temp1, temp2, on='id', how='left') #left join
print(eg_7)

print()
eg_9=pd.merge(temp1, temp2, how='outer') #outer join
print(eg_9)