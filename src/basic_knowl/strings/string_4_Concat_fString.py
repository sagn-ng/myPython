a,b="Sang", "Nguyen"
c=a+b
print(c) #output: SangNguyen

c=a+" "+b
print(c) #output: Sang Nguyen

#However, concatenation doesn't work when we try adding another type,
#such as c = a + 25. To do this and other expressions on strings, we have to learn about f-strings



#create an f-strings:
x=19
txt=f"Hello, i'm Sang. I'm {x}"
#add curly brackets as placeholders for variables and operations, modifiers
print(txt)

#example for operations and modifiers:
discout=0.25
price=250010.0
print(f"You have to pay {price*(discout+1):.1f}")