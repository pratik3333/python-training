import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity=0):
        #Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"


        #Assign to self object
        self.name = name
        self.price=price
        self.quantity=quantity

        #Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('Item.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity}')"

# for instance in Item.all:
#     print(instance.name)
Item.instantiate_from_csv()
