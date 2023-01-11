array = [ #upperlimits:grade
[0, 'Start'],
[25,'F'],
[45,'E'],
[50,'D'],
[60,'C'],
[80,'B'],
[101,'A'] 
]


marks = int(float((input('Enter marks: '))))
if marks not in range(0, 101): print("Marks not in range")
else:
    for i in range(0, 6):
        if marks in range(array[i][0], array[i+1][0]): print("Grade : " + array[i+1][1])
