sec = int(input("Enter no. of seconds : "))
minutes = sec//60
seconds = sec%60

if(sec//60 != 0):
    toprint = "minutes"
    if(sec//60 <= 1): toprint = 'minute'
    print(minutes, toprint, end = ' ')
if(sec%60 != 0): 
    toprint = "seconds"
    if(sec%60 <= 1): toprint = 'second'
    print(seconds, toprint)


