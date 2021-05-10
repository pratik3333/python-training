class Employee:
    increment=1.5
    no_of_emps=0
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first+last+"@gmail.com"

    def increase(self):
         self.salary=int(self.salary * self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

harry=Employee("Harry","Jackson",48000)
rohan=Employee("Rohan","Das",78000)

print(harry.salary)
Employee.change_increment(2)
harry.increase()
print(harry.salary)