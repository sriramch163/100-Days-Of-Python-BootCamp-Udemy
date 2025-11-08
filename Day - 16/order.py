# order.py

class Order:
    def __init__(self):
        self.items = []  # list of (MenuItem, quantity)

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def calculate_total(self):
        return sum(item.price * qty for item, qty in self.items)

    def show_order(self):
        print("\nYour Current Order:")
        for item, qty in self.items:
            print(f"- {item.name} x{qty} = ₹{item.price * qty}")
        print(f"Total Bill: ₹{self.calculate_total()}")
