from math import sum


def Perfect(num):
	divs = []
	for i in range(num,0,-1):
		if num%i==0: divs.append(i)
	if num*2==sum(divs): return True
	else: return False
		
a = input('Enter a number: ')
if(Perfect(a)):print('Perfect')
else: print('Not Perfect')