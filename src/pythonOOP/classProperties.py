class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    #'brand' & 'model' are called 'instance properties'

car1 = Car("Toyota", "Corolla")

print(car1.brand, car1.model) #access properties

#modifying properties
car1.brand, car1.model="Nissan", "GT-R" #modifying an object's properties
print(car1.brand, car1.model)

print("#####")
class Dog:
  birthYear=2022 #this is called a 'class property'
  def __init__(self, name, type):
    self.name, self.type = name, type

dog1=Dog("luke", "shiba")
print(dog1.birthYear) #output: 2022
Dog.birthYear=2025 #modifying the property of a whole class
print(dog1.birthYear) #output: 2025

dog1.color="white" #add a new property to an object (not the whole class)
print(dog1.color)