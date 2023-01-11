Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alphabet1 = list(map(str,Alphabet))
#print(Alphabet1)

ran = int(input("Enter rows:"))
a = 0
b = 1
letters = ((ran)*(ran + 1))//2
if letters > 26:
    Alphabet *= (letters//26) + 1
    Alphabet1 = list(map(str,Alphabet))
for i in range(ran):
    b = a + i+ 1
    print(Alphabet[a:b])
    a += i + 1


    