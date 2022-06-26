class Item:
    def __init__(self,name: str,price: float,quantity=0):
        #Run validation to the received arguments
        assert price >= 0
        assert quantity >= 0

        #Assign to self object
        self.name = name
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone",100,1)

item2=Item("Laptop",1000,3)

