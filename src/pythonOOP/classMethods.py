class Calculator:
    def add(self, a, b): return a+b
    #methods with parameters
    def multiply(self, a, b): return a*b

calc = Calculator()
print(calc.add(2, 5), calc.multiply(2, 5))
print("#####")
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    #methods that access and change class' properties
    def get_info(self):
        return f"{self.name} is {self.age} years old"
    def celebrate_birthday(self):
        self.age+=1 #modifying a class' properties
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Sang", 19)
print(p1.get_info())
p1.celebrate_birthday()
#the use of get_info() then print() is related to a special (magic) method called '__eq__'