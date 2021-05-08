class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first=None
        self.last=None

emp1=Employee('pratik','kagale')

emp1.fullname='john smith'

print(emp1.fullname)
print(emp1.email)

del emp1.fullname

