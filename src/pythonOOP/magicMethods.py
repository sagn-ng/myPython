#i'll only cover '__str__', '__eq__' and '__add__'
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __str__(self):
        return f"{self.name} ({self.age})"
#The __str__() method controls what is returned when the object is printed,
#or passed to str(). The return type must be a string, otherwise, there would
#be a 'TypeError'

    def __eq__(self, other):
        return self.name==other.name and self.age==other.age
#The __eq__() method changes the behavior of the normal '==' comparison, i.e
#instead of simply comparing their address

    def __add__(self, other):
        return self.age+other.age
#The __add__() method changes the behavior of the normal '+' operator, allowing
#us to 'add' objects.

p1 = Person("Sang", 19)
print(p1) #without __str__(), this would just print the address

p2=Person("Sang", 19)
print(p1==p2) #output: True, but without __eq__(), it would be False

p3=Person("Sang", 18)
print(p1+p3) #ouput: 37, but without __add__(), there would be a type error