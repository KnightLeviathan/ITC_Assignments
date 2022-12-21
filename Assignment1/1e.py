import math
'''
angle = float(input("Enter angle(in degrees): "))
rads = (angle/360)*2*math.pi
anglec = str(round(math.cos(rads), 4))
angles = str(round(math.sin(rads), 4))
print(str(angle), end = ' --- ')
print(angles + ' ' + anglec)
'''
'''angle = 0
#start_angle = 0
end_angle = 345
for x in range(angle, int(end_angle/15) + 1):
    rads = angle/360 * 2 * math.pi
    print(str(angle) + ' --- ' + str(round(math.sin(rads), 4)) + ' ' + str(round(math.cos(rads), 4)))
    angle += 15
'''

start_angle = 0
end_angle = 345
for x in range(start_angle, end_angle + 1 ,15):
    rads = math.radians(x)
    print(x, ' --- ',round(math.sin(rads), 4), round(math.cos(rads), 4))