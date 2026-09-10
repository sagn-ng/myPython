s="Sang Nguyen"

s1=s.upper() #however, s would stay the same
print(s1) #output: SANG NGUYEN

print(s.lower()) #output: sang nguyen

s1="  Sang   " #remove whitespaces
print(s1.strip()) #output: Sang

#replace(oldStr, newStr) method: replace all the substrings oldStr by another string newStr
print(s.replace("Sa", "S")) #output: Sng Nguyen