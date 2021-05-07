class Employee:
    number_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetail(self):
        return f"The name is {self.name}.\nsalary is {self.salary}.\nrole is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.number_of_leaves=newleaves


    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

class programmer(Employee):

    def __init__(self,name,salary,role,languages):
        self.name=name
        self.salary=salary
        self.role=role
        self.languages=languages


    def printprog(self):
        return f"The programmer's name is {self.name}.\nsalary is {self.salary}.\nrole is {self.role}.\nlanguages are {self.languages}"



pratik=Employee("Pratik",50000,"Student")
jack=Employee("Jack",60000,"super visor")
john=programmer("john",795,"programmer",["python"])
karan=programmer("karan",365,"programmer",["python","Cpp"])


print(karan.printprog())