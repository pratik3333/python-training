class Employee:
    increment=1.5
    no_of_emps=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_emps+=1

    def increase(self):
        self.salary=int(self.salary * Employee.increment)


harry=Employee("Harry","jackson",440000)
rohan=Employee("Rohan","Das",440000)


print(Employee.no_of_emps)
print(harry.salary)
harry.increase()
print(harry.salary)
print(harry.__dict__)