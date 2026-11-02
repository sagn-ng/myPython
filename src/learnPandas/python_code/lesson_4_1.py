import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'Finance', 'HR', 'Finance', 'IT'],

    'Gender': ['M', 'M', 'F', 'F', 'M'],

    'Salary': [2500, 1200, 1800, 2000, 1000],

    'Job review': ['great', 'mid', 'mid', 'great', 'low'],

    'Score': [100, 85, 80, 90, 84]
})

"""Grouping"""
eg_0=df.groupby('Department').Department.count() #equivalent to value_counts()
print(eg_0)

print()
#view the highest salary in different salary values of each department
eg_1=df.groupby('Department').Salary.max()
print(eg_1)

print()
#selecting the name of the first department to give each kind of review
eg_2=df.groupby('Job review').apply(lambda p: p.Department.iloc[0])
print(eg_2)

print()
#a simple statistical summary of the salary of each department
eg_3=df.groupby('Department').Salary.agg([len, min, max, sum])
print(eg_3)

"""Multi-indexes"""
print()
#average salary by job and gender
eg_4=df.groupby(['Department', 'Gender'])['Salary'].mean()
print(type(eg_4))
print(eg_4)

print()
#converting back to a regular index
eg_5=eg_4.reset_index()
print(type(eg_5)) #DataFrame
print(eg_5)