class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    #
    # def fullname(self):
    #     return 'my first name is {}.\nmy last name is {}'.format(self.first,self.last)
    def fullname(self):
        return f'my first name is {self.first}.\nmy last name is {self.last}.'

emp_1=Employee('Corey','schafer',50000)
emp_2=Employee('Test','User',60000)

print(emp_1.fullname())