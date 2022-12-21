str1 = input('>')
answer = False
'''for i in range (0, len(str1) - 4):
    a = str1[i:i+4]
    print(a)
    if(a == 'name'): answer = True
'''
ans = str1.find('name')
if(ans != -1): answer = True

if(answer == True): print("Yes")
else: print("No")     
