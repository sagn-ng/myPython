set1, set2 = {"a", "b", "c"}, {1, 2, 3, "a"}

set3 = set1.intersection(set2) #intersections of 2 sets, or '&' instead
#intersection_update() also take the intersection, but doesn't return anything
print(set3)

print("#####")
set3 = set1.difference(set2) #difference of set1 and set2: elements in set1 that are not in set2
#difference_update() also take the difference, but doesn't return anything
print(set3)
#we also have symmetric_difference() and symmetric_difference_update()

print("#####")
set3=set1.copy() #copy a set
print(set3)