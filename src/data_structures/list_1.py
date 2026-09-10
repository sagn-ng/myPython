#create a list:
myList=["apple", "banana", "cherry"]
print(myList) #print a list
print(type(myList)) #check the type, output: <class 'list'>

print(len(myList)) #get the length (number of items) of a list

#a list can contain different data types:
myList=["apple", 25, True]
print(myList)

#the list() constructor is also available
myList=list(("apple", 25, True))
print(myList)
#####

#access, change list items: it works the same as in string
print(myList[1]) #get the element whose index is 2, i.e the second one
print(myList[1:3]) #this returns a list from index 1 -> 2
print(myList[-1]) #get the last element

myList[1:3]="orange" #"orange" will be treated as a list of 6 characters
print(myList)

myList=["apple", "banana", 25, "cherry", True]
myList[1:3]=["orange"] #change a range of item values
print(myList)