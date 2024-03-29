class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'.'+'@gmail.com'

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount_amt=amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
emp_1=Employee('corey','schafer',500000)
emp_2=Employee('Test','User',600000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1='John-Deo-700000'
emp_str_2='Steve-smith-80000'
emp_str_3='Jane-Doe-90000'

first,last,pay = emp_str_1.split('-')

new_emp_1=Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


import datetime

my_date=datetime.date(2016,7,11)

print(Employee.is_workday(my_date))
