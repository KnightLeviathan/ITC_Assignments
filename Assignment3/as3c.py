str_input = input("Enter numbers (using ',' or ' 'as separators) : ")
if (' ' in str_input) : numbers = list(map(int, str_input.split()))
elif(',' in str_input) :numbers = list(map(int, str_input.split(',')))
elif(len(str_input) == 1): numbers = [int(str_input)]
else: raise ValueError("Please enter a valid input")

#print(numbers)
#numbers2 = []
#for i in numbers: numbers2.append(int(i))

list_final = []
for i in numbers:
    list_final.append((i,i**2))

print(list_final)