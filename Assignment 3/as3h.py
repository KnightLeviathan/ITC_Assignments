#predefined sets
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#SetA = Set1.union(Set2) - Set1.intersection(Set2)
SetA = Set1^Set2
print(SetA)

#print((Set1&Set2) | (Set2&Set3) | (Set3&Set1))
#print(Set1|Set2|Set3)
SetB = (Set1|Set2|Set3) - ((Set1&Set2) | (Set2&Set3) | (Set3&Set1))
print(SetB)

SetC = (Set1&Set2) | (Set2&Set3) | (Set3&Set1)
print(SetC)

SetD = set()
for i in range (1,11) : 
    if i not in Set1:  SetD.add(i) #ascending order?
print(SetD)

SetE = set()
for i in range (1,11) : 
    if i not in Set1|Set2|Set3:  
        #print(i)
        SetE.add(i) #output decsending order? because unordered? sorts it for a specific no. of elements? after 5.....
print(SetE)

