f=open("D:\\myPython\\src\\basic_knowl\\fileHandling\\demoFile.txt") # 'r' (for read-only) is the default value
#if f is in read mode but the file doesn't exist, there will be an I/O error
print(type(f))

print(f.read()) #read all the content from the pointing file
#after that, f reaches end of file

print("#####")
f.seek(0) #make f point to the start of the file again

line=f.readline() #get the first line as a string
print(line)
#after a use of the method readline(), f will point to the next line, until it reaches the end

f.close() #close