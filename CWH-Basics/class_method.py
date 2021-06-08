

class Employee:
    no_of_leaves=5

    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first+last+'123@gmail.com'

    def info(self):
        print(f"The Employee name is {self.first} {self.last}.\nsalary is {self.salary}.")


    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves


emp1=Employee('pratik','kagale',9940)
emp2=Employee('Kunal','Deshmukh',9343)

print(emp1.no_of_leaves)
Employee.change_leaves(45)
print(emp1.no_of_leaves)