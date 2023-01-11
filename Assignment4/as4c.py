import random

list1 = []
for i in range(0, 10):list1.append(i)

for i in range(0,10):
    a1 = random.choice(list1)
    b1 = random.choice(list1)
    print("Question ",i+1,": ", a1, 'x', b1, ' = ', end = '')
    ans = int(input(''))
    if ans == round(a1*b1): print('Right!')
    else: print('Wrong. The answer is ', round(a1*b1))