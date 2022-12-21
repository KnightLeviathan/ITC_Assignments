'''trial file of assignment 3'''


import re

str1 = input(">")
'''
for a in range(0,len(str1)):
    for b in range(a+1,len(str1) + 2):
        str_to_find = str1[a:b]
        if(str1 != ' '):
            all_occ = [i.start() for i in re.finditer(str_to_find, str1)]
            if (len(all_occ) > 0): 
                print(str_to_find, "occurs", len(all_occ), "times")
                print(all_occ)
'''
str1 = " ".join(str1.split())
print (str1)
str1 += ' ' 
spaces = [i.start() for i in re.finditer(' ', str1)]


if (len(spaces) > 1):
    spaces2 = [0] + spaces
    print(spaces2)
    
    #can do the same using split(' ') and list.count()
    #print(str1.count()
    for a in range(0,len(spaces2)):
        str_to_find = str1[spaces[a]:spaces[a+1]]
        all_occ = [i.start() for i in re.finditer(str_to_find, str1)]
        if (len(all_occ) > 0 and str_to_find != ' ' and str_to_find != ''): 
                print(str_to_find, "occurs", len(all_occ), "times")
                print(all_occ)

else:
    for a in range(0,len(str1)):
        str_to_find = str1[a:a+1]
        all_occ = [i.start() for i in re.finditer(str_to_find, str1)]
        if (len(all_occ) > 0 and str_to_find != ' ' and str_to_find != ''): 
                print(str_to_find, "occurs", len(all_occ), "times")
                print(all_occ)



