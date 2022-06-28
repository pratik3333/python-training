
class car:
    def __init__(self,price:str,milage:float,discount=str,quantity=str):

        assert price >= 0, f"price {price} is not greater than or equaal to zero"
        assert milage >=10, f"milage {milage} is not greater than or equal to ten"
        self.price = price
        self.milage = milage
        self.discount = discount
        self.quantity = quantity

    def calulate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.discount

car1=car(1000,13,0.8,5)

print(car1.price)
print(car1.calulate_total_price())
car1.apply_discount()
print(car1.calulate_total_price())