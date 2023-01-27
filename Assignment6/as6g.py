#to be modified


class Student():
    pass #empty class
    '''
    year = 1

    def __init__(self, name, branch, sid, age):
        self.name = name
        self.branch = branch
        self.sid = sid
        self.age = age
    '''
class Marks(): pass
a = Student()#'A', 'ece', '2210xxxx', '18')
if isinstance(a, Student):print('Is instance.')
else: print('No')
if isinstance(a, Marks):print('Is instance.')
else: print('No')

b = Marks()
print(isinstance(b,Student))
print(isinstance(b,Marks))

if issubclass(Student, object):print('Is sub.')
else: print('No')
if issubclass(Marks, object):print('Is sub.')
else: print('No')