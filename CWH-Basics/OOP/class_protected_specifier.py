class Employee:

    no_of_leaves=4
    no_of_emps=0
    _protect=10
    __private=30
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first+last+'123@gmail.com'

        Employee.no_of_emps +=1

    def info(self):
        print(f"The name is {self.first} {self.last}.\nsalary is {self.salary}.")

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))

class Programmer(Employee):
    pass

emp1=Employee('Corey','Schafer',425)
print(emp1.no_of_leaves)
print(emp1._protect)
print(emp1._Employee__private)