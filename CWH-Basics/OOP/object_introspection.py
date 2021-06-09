class Employee:
    no_of_leaves=4
    no_of_emps=0
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first+last+'123@gmail.com'
        Employee.no_of_emps+=1

    def info(self):
        print(f"The Employee name is{self.first} {self.last}.\nSalary is {self.salary}.")

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

    @classmethod
    def from_dash(cls,string):
    #     param=string.split('-')
    #     return cls(param[0],param[1],param[2])
        return cls(*string.split('-'))

emp1=Employee('pratik','kagale',9434)
emp2=Employee.from_dash('corey-schafer-4365')

import inspect
print(inspect.getmembers(emp1))
print(inspect.getmembers(emp2))
