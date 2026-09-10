list1 = ["apple", "banana", "mango"]
#general syntax:    listName = [<expression> for <item> in <iterable> if <condition>]
newList=[x for x in list1 if x!="apple"] #only accepts values that are not "apple"
print(newList)

print("#####")
list1.sort() #sort a list in ascending order - by default
print(list1) #output: apple, banana, cherry, mango
#sort in descending order: use the argument:    reverse=True

print("#####")
def myfunc(n):
  return abs(n - 50)
list2 = [100, 50, 65, 82, 23]
list2.sort(key=myfunc) #custom sort: key=myFunc argument
print(list2)

print("#####")
list1.reverse() #reverse a list
print(list1)

list2=list1.copy() #make a copy of list1

list3=["cherry", "orange"] #join 2 lists:

list4=list2+list3
print(list4)
#we can use the extend() method, or the constructor: list(list1),
#or assign: list2=list1[:]