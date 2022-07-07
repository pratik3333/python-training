import csv


class Item:
    pay_rate=0.8
    all = []
    def __init__(self,name: str,price: float,quantity=0):
        assert price >= 0, f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"

        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate

    @classmethod
    def instantiat_from_csv(cls):
        with open('Item.csv','r') as f:
            reader = csv.DictReader(f)
            items=list(reader)


        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item( '{self.name}', '{self.price}', '{self.quantity}')"

Item.instantiat_from_csv()
print(Item.all)