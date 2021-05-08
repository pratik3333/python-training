from datetime import date

#random person
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def frombirthyear(cls,name,birthyear):
        return cls(name,date.today().year-birthyear)


    def display(self):
        print(self.name+"'s age is: ",str(self.age))

pratik=Person('pratik',20)
pratik.display()

rahul=Person.frombirthyear('Rahul',1999)
rahul.display()