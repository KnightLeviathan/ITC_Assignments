a = 56 #111000
b = 10 #1010
#print(bin(a), bin(b))
print(a&b, a|b, a^b)

a = a << 2
b = b << 2
print(a,b)

a = a >> 2
b = b >> 4

print(a,b) #a remains same