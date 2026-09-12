#we only consider special cases: default paramter values; keyword arguments
print("1) default parameter values:")
def sayHello(name="Sang"): print("Hello", name)

sayHello("S") #call the function with an argument
sayHello() #the function use the default parameter values

print("\n2) keyword arguments:")
def my_function(name, age):
  print("My name is", name)
  print("I am", age)

my_function(name="Sang", age = 19)
#with keyword arguments, the order of arguments doesn't matter:
my_function(age=19, name="Sang")

print("\n3) myFunc(*args, **kwargs):")
print("3.1: *args") #used to accept any number of positional arguments as a dictionary
def printSum(*args):
  print(type(args)) #output: <class 'tuple'>
  sum=0
  for x in args: sum+=x
  print(sum)

printSum(1,2,3,4,5,6,7)

print("\n3.2: **kwargs") #used to accept any number of keyword arguments as a list
def my_function(**myvar):
  print("Type:", type(myvar)) #ouput: <class 'dict'>
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Sang", age = 19, city = "Hanoi")