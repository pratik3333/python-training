
import logging
#
# loger=logging.getLogger(__name__)
logging.basicConfig(filename='employee.log',level=logging.INFO)

class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

        logging.info(f'created Employee: {self.fullname} {self.email}')
        #loger.info(f'created Employee: {self.fullname} {self.email}')

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}{self.last}@email.com'





emp_1=Employee('Pranit','Kagale')
emp_2=Employee('Test','Schafer')
