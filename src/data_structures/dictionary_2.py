thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red" #add an item to the dictionary
thisdict["year"]=2007 #overwrite an existing key's value
print(thisdict)

print("#####")
thisdict.pop("year") #remove an item by its key
thisdict.popitem() #remove the last inserted item
print(thisdict)