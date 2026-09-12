print("1. Basic exception handling")
try:
    x, y = 25, "Sang"
    print(x+y) #this will cause an error, and we'll catch it:
except: #must-have
    print("An error occurred.")
else: #in case there is no error (optional):
    print("No error occured until now.")
finally: #optional
    print("Task finished.")

print("\n2. Raise an exception")
x="Sang"
#i will perform a try-except block to avoid auto-generated red lines
try:
    if type(x) is not int:
        raise TypeError("Only integers are allowed")
except TypeError:
    print("Exception catched!")
else:
    print("No problem occured until now.")
finally:
    print("Task finished.")