#the __init__() method is a 'constructor' for objects. Only the newest declared _init_() method can exist.
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    #the first parameter 'self' (or this, obj...) is compulsory in instance methods

    def sayHello(self):
        print(f"Hello, my name is {self.name}. I'm {self.age}")
#'self' doesn't have to be named 'self', but that variable shows python which object's properties
#that we want to access
p1=Person("Sang", 19)
p1.sayHello()