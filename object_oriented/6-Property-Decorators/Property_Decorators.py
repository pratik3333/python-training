class Employee:
    increment=1.5
    no_of_emps=0
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        Employee.no_of_emps +=1




    def increase(self):
        self.salary=int(self.salary*self.increment)

    @classmethod
    def emp_string(self,string):
        first,last,salary=emp_string.split("-")
        return cls(first,last,salary)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

    @property
    def email(self):
        if self.first==None:
            return 'Email not set'
        else:
            return self.first+'.'+self.last+'123@email.com'

    @email.setter
    def given_email(self,given_email):
        name_list=given_email.split('@')[0].split('.')
        self.first=name_list[0]
        self.last=name_list[1]


    @email.deleter
    def email(self):
        self.first=None
        self.last=None

    @staticmethod
    def is_open(day):
        if day=="Sunday":
            print("Closed")

        else:
            print("Open")


if __name__ == '__main__':
    harry = Employee('Harry', 'Jackson', 78000)
    rohan = Employee('Rohan', 'Das', 78000)



    print(rohan.email,harry.email)
    harry.last='patil'
    print(harry.email)
    del harry.email
    print(harry.email)