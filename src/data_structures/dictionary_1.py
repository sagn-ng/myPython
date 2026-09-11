#create a dictionary with curly brackets, consisting key-value pairs:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
print(type(thisdict))

#access items by keys:
x=thisdict["brand"] #or use the get() method
print(x) #output: Ford

#extract the key set as a list:
keySet=thisdict.keys()
print(keySet)

#extract the value set as a list:
valueSet=thisdict.values()
print(valueSet)

#extract all items as a list of tuples
x=thisdict.items()
print(x)
print(type(x))