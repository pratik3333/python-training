class Employee:
    raise_amount=1.04
    number_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'123@gmail.com'

        Employee.number_of_emps +=1

    def fullname(self):
        return f'{self.first} {self.last}'
        # return '{} {}'.format(self.first,self.last)

    @classmethod
    def from_string(cls,emp_string):
        first,last,pay=emp_string.split('-')
        return cls(first,last,pay)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True



emp1=Employee('Corey','Schafer',78000)
emp2=Employee('Pratik','Kagale',78000)
emp3='John-Smith-98000'

new_emp3=Employee.from_string(emp3)
print(Employee.number_of_emps)
print(emp2.fullname())


import datetime
my_date = datetime.date(2021,5,18)

print(Employee.is_workday(my_date))