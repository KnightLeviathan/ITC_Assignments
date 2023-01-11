inp = input('Enter range in format(x y) : ').split()  
ran = list(map(int,inp))


for num in range(ran[0], ran[1] + 1): 
    prime = True
    if num == 1:
        prime = False
    elif num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                break
    if(prime):print(num)