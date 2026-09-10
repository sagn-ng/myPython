#walrus operator: assigns values to variables
#as part of a larger expressions
print(x:=25)

#chaining comparisons:
print(5<x<10) #x is 25 as assigned from above

#logical operators:
print(x>20 and x<30, end=" ") #output: True
print(x<5 or x<10, end=" ") #output: False
print(not(x>20)) #output: False