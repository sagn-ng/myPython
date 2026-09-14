f=open("D:\\myPython\\src\\basic_knowl\\fileHandling\\demoFile.txt", "w") #open in write-only mode
#rewrite the file if it already exists, otherwise, create a new one

f.write("25, 10")
f.write("\nSang")
f.close() #must close to push all the content from the buffer to the file
#or if we don't want to close immediately, use flush()

f=open("D:\\myPython\\src\\basic_knowl\\fileHandling\\demoFile.txt", "a") #open in append mode
f.write("\nHello") #append "Hello" to the end
f.close()

f1=open("D:\\myPython\\src\\basic_knowl\\fileHandling\\demoFile.txt")
print(f1.read()) #confirm the changes
f1.close()

#to avoid forgetting the close() line, there is "with open(...) as ...", e.g:
with open("D:\\myPython\\src\\basic_knowl\\fileHandling\\demoFile.txt") as f:
    print(f.readline(), end="")