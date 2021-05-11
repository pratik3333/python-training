class Employee:
    increment=1.5
    no_of_emps=0
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first+last+"123@gmail.com"

    no_of_emps += 1
    def increase(self):
        self.salary=int(self.salary*self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

    @classmethod
    def new_emp(cls,string):
        first,last,salary=string.split("-")
        return cls(first,last,salary)

    @staticmethod
    def is_open(day):
        if day=="Sunday":
            return False
        else:
            return True

    def __add__(self, other):
        return self.salary+other.salary

    def __mul__(self, other):
        return self.salary*other.salary

    def __repr__(self):
        return "Employee ({} {} {})".format(self.first,self.last,self.salary)

    def __str__(self):
        return "The employee's email id is {}".format(self.email)

harry=Employee('Harry','Jackson',78000)
rohan=Employee('Rohan','Das',78000)

#print(harry.salary)
#Employee.change_increment(2)
#harry.increase()
#print(harry.salary)

#print(harry*rohan)
print(harry.__repr__())
print(harry.__str__())