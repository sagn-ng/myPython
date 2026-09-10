list1=["apple", "banana"]

list1.append("orange") #append an item to the end
list1.insert(2,"lemon") #insert "lemon" at index 2
print(list1)

list2=["McLaren", "Porsche", "Volvo"]
list1.extend(list2) #append elements from another list (or any iterable object)
print(list1)

print("#####")
#remove elements:
list1.remove("lemon") #remove a specified element (if there are duplicates, remove the first one)
print(list1)
list1.pop(4) #remove an element by index (the last one if not set)
print(list1)

print("#####")
list1.clear() #clear the list
print(list1)