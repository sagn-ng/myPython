x=10 #int
print(x)
y=2.5 #float
print(y)

z=x+7j #z=10+7j
print(z) #output: (10+7j)

#to assign z = x + y*j, we can use z = x + y*1j or like below
z=complex(x, y)
print(type(z)) #output: <class 'complex'>
print(z)
