a = [0,0,0]

a[0] = int(input('>'))
a[1] = int(input('>'))
a[2] = int(input('>'))
e = True
for i in range(0,3): #changing the indexes using a for loop to check all sides
    x = a[i]
    y = a[(i+1)%3]
    z = a[(i+2)%3]
    #print(x,y,z)
    if(x >= y + z): e = False
    #print(e)
if(e): pass
else: print("Traingle Invalid")

s = (a[0] + a[1] + a[2])/2 #semiperimeter
area = (s*(s-a[0])*(s-a[1])*(s-a[2]))**0.5 #area
print('The area of the triangle is %0.2f'%area)