
q1 = int(input("If the candy is divided evenly among 5 people, how many pieces would be left over?"))
q2 = int(input("If the candy is divided evenly among 6 people, how many pieces would be left over?"))
q3 = int(input("If the candy is divided evenly among 7 people, how many pieces would be left over?"))

if q1 > 5 or q2 > 6 or q3>7: raise ValueError('Dont trick me!!')

candy_found=False
for i in range(1,201):
    if i%5 == q1 and i%6==q2 and i%7==q3: 
        print(i)
        candy_found = True
if(not candy_found):print("No such number less than 200 exists")