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


class player:
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetail(self):
        return f"The name is {self.name} and game is {self.game}"

class coolprogrammer(Employee,player):
    language = "python"
    def printlanguage(self):
        print(self.language)

pratik=Employee("Pratik",50000,"Student")
jack=Employee("Jack",60000,"super visor")
shubham=player("Shubham",["Cricket"])
karan=coolprogrammer("karan",8785,"coolprogrammer")

karan.printlanguage()
det=karan.printdetail()

print(det)