#assuming repetiton allowed

class idk():
    def __init__(self, list1):
        self.inp = list1
        self.out = []

    def sum(self):
        #could reduce memory space here but an increase in code size.....  complete code
        for i in self.inp:
            for j in self.inp:
                for k in self.inp:
                    if (i + j + k) ==0 and sorted([i,j,k]) not in self.out : self.out.append(sorted([i,j,k]))

sum1 = idk(list(map(int,input('Enter list (using ","): ').split(','))))
#print(sum1.inp)
sum1.sum()
print(sum1.out)