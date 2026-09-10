x=25
x="sang" #change the type and value of x
print(x) #output: sang

x=float(25) #casting: x will be 25.0
print(type(x)) #output: <class 'float'>

#assign multiple values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry" 
print(x, y, z) #print with a space separating words

#assign the same value for many variables
a=b=c="Apple"
print(a, b, c)

#concatenation in a single print() line:
print(x+y+z) #output: OrangeBananaCherry