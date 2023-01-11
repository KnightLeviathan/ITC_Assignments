inp = input('Enter range in format(x y) : ').split()  
ran = list(map(int,inp))
num = int(input('Enter number : '))
for i in range(ran[0], ran[1] + 1): 
    if(i%num == 0):print(i, end=' ')

