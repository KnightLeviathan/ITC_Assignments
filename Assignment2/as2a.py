str1 = "Python is a case sensitive language" #predefined string
length = len(str1)
print("Length is : ", length)

str2 = str1[::-1]
print(str2)

#str3 = str1[10::]
str3 = slice(10,35)
print(str1[str3])

str4 = str1.replace("a case sensitive language", "object oriented")
print(str4)

print(str1.index('a'))

str1 = str1.replace(' ', '')
print(str1)#no spaces