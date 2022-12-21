a = int(input("1st No. \n>"))
b = int(input("2nd No. \n>"))
c = int(input("3rd No. \n>"))
d = 0
e = True
#print(a,b,c)
if(a>b):
    d = a
    if(c>a):
        d = c   
    elif(a==c):
        e = False
        print(a,c," are greatest")
elif(b>a):
    d = b
    if(c>b):
        d = c
    elif(b==c):
        e = False
        print(b,c,"2nd and 3rd Nos. are greatest") 
elif (a==b & a>c):
    e = False
    print(a,b,"1st and 2nd are greatest")
elif(a==b==c):
    print("All equal")
    e = False

if(e):
    print(d,"is the greatest")
    