s="hello world"
#s[i : j]   get the substring from index i to j-1
print(s[2:5]) #output: llo

#s[i :] get the substring from index i to the end
print(s[2:]) #output: llo world

#s[: j] get the substring from the start to index j-1
print(s[:5]) #output: hello

"""negative indexing: s[i : j] (i, j<0) get the slice from the
#end of the array"""
print(s[-5:-2]) #output: wor