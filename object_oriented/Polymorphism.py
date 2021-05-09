class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am Dog. my name is {self.name}.I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am Cat. my name is {self.name}.I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

dog1=Dog("Sam",2)
cat1=Cat("Lucy",2.5)

for animal in (dog1,cat1):
    animal.make_sound()
    animal.info()