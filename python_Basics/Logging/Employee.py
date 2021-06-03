
import logging

logging.basicConfig(filename='employee.log',level=logging.INFO)

class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

        logging.info(f'created Employee: {self.fullname} {self.email}')

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}{self.last}@email.com'

emp_1=Employee('Pratik','Kagale')
emp_2=Employee('Corey','Schafer')


