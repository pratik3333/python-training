class Employee:
    no_of_leaves=4
    no_of_emps=0
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

    @staticmethod
    def print_good(string):
        print("This is good " + string)

class Programmmer(Employee):
    #
    # def info(self):
    #      print(f"The name is {self.first} {self.last}.\nsalary is {self.salary}.")

    def __init__(self,first,last,salary,role):
        super(Programmmer, self).__init__(first,last,salary)
        self.role=role


    def info(self):
         print(f"The name is {self.first} {self.last}.\nsalary is {self.salary}.\nRole is {self.role}")


emp1=Programmmer('pratik','kagale',9434,'Programmer')
emp2=Employee.from_dash('corey-schafer-4365')
emp3=Programmmer.from_dash('Amit-Mane-3425-programmer')

# emp1.info()
# emp2.info()
emp3.info()