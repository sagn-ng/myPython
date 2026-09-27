import time

#The epoch is the point where the time starts and is platform-dependent.
#On Windows and most Unix systems, the epoch is January 1, 1970, 00:00:00 (UTC)
print(time.gmtime(0)) #get the epoch

cur=time.time() #get the current time in secs (float type) since epoch
print(type(cur))
print("Current time in seconds since epoch:", cur)

convTime=time.ctime(cur) #convert a specified timestamp into a readable format
print(type(convTime)) # <class 'str'>
print(convTime)

#halt the program execution:
for i in range(4):
    time.sleep(1)
    print(i)

obj = time.localtime(1790494600.6317906) #the number of secs since epoch
print(obj) #returns the struct_time object in local time

#convert a struct_time object back to secs since epoch:
x=time.mktime(obj)
print("Local time in secs:", x)

#the method time.strftime() converts a tuple (struct_time representing)
#to a string as specified by the format argument
s=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(1790494600.6317906))
print(s)