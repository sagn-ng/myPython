import os
if os.path.exists("D:\\myText.txt"): #if the file doesn't exist, there will be an error
    os.remove("D:\\myText.txt")
else:
    print("The file doesn't exist!")