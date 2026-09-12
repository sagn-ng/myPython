print("3.3: Combining normal (positional) arguments and *args, **kwargs:")
#the order must be: normal -> *args -> **kwargs
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("User Info", "Sang", "S", age = 25, city = "Hanoi")

print("\n4. Unpacking arguments:")
print("4.1: Unpacking lists with *") #unpack items store in a list to use them as arguments
def my_function(a, b, c):   return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

print("\n4.2: Unpacking Dictionaries with **")
def my_function(fname, lname):  print("Hello", fname, lname)

person = {"fname": "Sang", "lname": "Nguyen"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
#note: the keys in the unpacked dict must be in "str" type