#shorthand if:
a, b = 10, 20
bigger = a if a > b else b
print("Bigger is", bigger)

print("#####")
print("A") if a > b else print("=") if a == b else print("B")

print("#####")
for i in range(11):
    if (i%2!=0): pass #pass = continue in C, C++, Java
    else: print(i, end=" ")