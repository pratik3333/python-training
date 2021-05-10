class Employee:
    increment=1.5
    no_of_emps=0
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary

    no_of_emps +=1
    def increase(self):
        self.salary=int(self.salary*self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

    @classmethod
    def from_string(cls,emp_string):
        first,last,salary=emp_string.split("-")
        return cls(first,last,salary)

    @staticmethod
    def isopen(day):
        if day=="Sunday":
            return False
        else:
            return True

class Programmer(Employee):
    def __init__(self,first,last,salary,proglang,exp):
        super().__init__(first,last,salary)
        self.proglang=proglang
        self.exp=exp

    def increase(self):
        self.salary=int(self.salary*(self.increment+0.2))

pratik=Programmer('Pratik','Kagale',78000,'python','5yrs')
kunal=Employee('Kunal','Deshmukh',78000)

print(pratik.salary)
Employee.change_increment(1)
pratik.increase()
print(pratik.salary)

