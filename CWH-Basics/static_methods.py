class Employee:
    no_of_leaves=4
    no_of_emps=0
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first+last+'123@gmail.com'

        Employee.no_of_emps +=1

    def fullname(self):
        print(f"{self.first} {self.last}.")

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))

    @staticmethod
    def print_good(string):
        print("This is good " + string)

emp1=Employee('pratik','kagale',9434)
emp2=Employee.from_dash('corey-schafer-4365')

emp2.print_good('Harry')