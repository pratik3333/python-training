class Dad:
    basketball = 1

class Son(Dad):
    Dance=1
    def isdance(self):
        return f"Yes i dance {self.Dance} number of times."
class Grandson(Son):
    Dance=6
    basketball = 78

    def isdance(self):
        return f"Jackson yeah! yes i dance very awesomely {self.Dance} number of times"

darry=Dad
larry=Son
harry=Grandson
print(harry.basketball)