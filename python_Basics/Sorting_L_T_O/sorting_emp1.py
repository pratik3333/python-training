

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return f'{self.name} {self.age} ${self.salary}'


e1=Employee('pratik',21,70000)
e2=Employee('corey',25,80000)
e3=Employee('peter',30,90000)

employee=[e1,e2,e3]
#Using lambda function
s_employee=sorted(employee,key=lambda e: e.salary)
print(s_employee)