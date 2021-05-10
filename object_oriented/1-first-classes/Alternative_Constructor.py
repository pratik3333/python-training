class Employee:
    increment=1.5
    no_of_emps=0
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first+last+"@email.com"

    no_of_emps+=1
    def increase(self):
        self.salary=int(self.salary * self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

    @classmethod
    def from_string(cls,emp_string):
        first,last,salary=emp_string.split("-")
        return cls(first,last,salary)

harry=Employee("Harry","jackson",44000)
lovish=Employee.from_string("Lovish-Shaha-48615")
print(lovish.first)
print(lovish.salary)