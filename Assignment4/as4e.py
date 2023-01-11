inp = input("Enter string: ")
list1 = []
for i in range(len(inp)):list1.append(inp[-(i+1)])
print(''.join(list1))
