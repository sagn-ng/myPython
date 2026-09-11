s = {10, 50, 20} #create a set, or we can use the set() constructor
print(s) #there is no specific order for elements to be printed
print(type(s)) #check the type

#sets don't allow modifying values, but you can add and remove, combine:
s.add(25) #add()
s.add(25) #duplicates will be ignored
print(s)

s.remove(20) #remove(), but it will cause an error if "20" doesn't exist
#discard() can fix that
print(s)

print("#####")
set1, set2 = {"a", "b", "c"}, {1, 2, 3, "a"}
s = set1.union(set2) #union of n (in this case n=2) sets, or also '|': set3 = set1 | set2
print(s)
#union() can take tuples, lists,.. as arguments

s.update(set1) #also joins sets, but only changes the original, doesn't return a new set
print(s)