class Dates:
    def __init__(self,date):
        self.date=date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/","-")

class DatewithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date=Dates("8-5-2021")
dateFromDB = DatewithSlashes("8/5/2021")

if (date.getDate()==dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")

