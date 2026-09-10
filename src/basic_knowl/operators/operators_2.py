#identity operators:
x, y=["apple", "banana"], ["apple", "banana"]
z=x
print(x is z, x is y, x==y) #ouput: True False True

#membership operators:
print("apple" in x, "orange" not in x) #output: True True
print ("s" in "apple") #output: False

#arithmetic operators: division and exponentation
x, y=2.5, 3
print(f"{x/y:.6f}") #returns a float
print(x//y) #returns an integer that is rounded down
print(x**y)