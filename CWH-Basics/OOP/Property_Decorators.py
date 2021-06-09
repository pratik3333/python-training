class Employee:
    no_of_leaves=8
    No_of_emps=0
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        Employee.No_of_emps +=1

    def details(self):
        print(f"The Employee name is {self.fname}{self.lname}.")

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. please set it useing setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting now....")
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


emp1=Employee('Corey','Schafer')
emp2=Employee('Nikhil','Pandey')
emp3=Employee.from_dash('Raj-Pandey')


# print(emp1.email)
# emp1.fname='Rahul'
# print(emp1.email,'\n')

emp1.email='This.That@gmail.com'
print(emp1.email)

del emp1.email
print(emp1.email)
print(emp1.no_of_leaves)
print(emp1.fname)