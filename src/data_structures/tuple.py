fruits = ("apple", "banana", "cherry") #create a tuple
print(fruits, "; length of the tuple:", len(fruits))
print("#####")
#access to items in a tuple (works the same as in list):
print(fruits[1], fruits[-1], fruits[1:3])

print("#####")
#"unpack" a tuple:
(green, yellow, red) = fruits
print(green, yellow, red)
#note: The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.

print("#####")
#asterisk: each one not having receive only 1 value, the one that has it takes the rest
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #assign the rest as a list called "red"
print(green, yellow)
print(red) #    red=['cherry', 'strawberry', 'raspberry']

print("#####")
#join tuples;
tuple1, tuple2 = ("a", "b" , "c"), (1, 2, 3)
tuple3 = tuple1 + tuple2 #join tuple1 and tuple2
print(tuple3)

mytuple = fruits*2  #multiply the content in a tuple a number of times
print(mytuple)