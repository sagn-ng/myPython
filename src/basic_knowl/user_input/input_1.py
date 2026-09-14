#take an input:
x=input()
print(type(x)) #python stores whatever you type as strings
print("You typed:", x)

y=input("Type something (a string, a number,...): ") # take an input with prompt
print(y)

x=int(input("Type an integer: ")) #typecasting to get specific types of inputs
print("You typed: ", x)

#the input() func. only stops when it meets the character '\n' (i.e Enter)
x=input("Try typing more than 1 words: ")
print("You typed: ", x)
wordList=x.split() #split the input x into a list of single words
print(wordList)

#split a string of numbers separated by spaces into a list of numbers:
numbers=list(int(x) for x in input().split())
print(numbers)