day = int(input("day: "))
mon = int(input("month(integer): "))
year = int(input("year: "))

#dictionary with months to days in them
dates = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}

#if year not in range(1800,2025) or mon not in range(0,13) or day>dates[mon]: raise ValueError("Please enter a valid date")
#using if elif for conditions
if year not in range(1800,2025): raise ValueError("Please enter a valid date")
elif mon not in range(0,13): raise ValueError("Please enter a valid date")
elif day>dates[mon]: raise ValueError("Please enter a valid date")

if year % 4 == 0 and (year % 100 != 0 or year%400 == 0): dates[2] = 29
#print(dates[2])

if day == dates[mon]:
    day = 1
    if mon == 12: 
        mon = 1 
        year += 1
    else : mon += 1
else:
    day += 1

if day < 10 : day = '0' + str(day)
if mon < 10 : mon = '0' + str(mon)
print('Next Date is ' + str(day) + '/' + str(mon) + '/' + str(year))