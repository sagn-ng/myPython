s="hello world" #either "" or ''
print(s)

#multiline string (three quotes):
s="""Sang Nguyen
25 10"""
print(s)

s="Sang Nguyen"
print(s[2]) #strings as arrays: also 0-indexed

for c in s: print(c, end=" ") #loop through characters in a string
print()

print(len(s)) #string length

#check if a character or phrase exists in a string:
print('S' in s)
print("s" in s)