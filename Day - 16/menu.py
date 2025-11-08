# menu.py

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Menu:
    def __init__(self):
        self.items = [
            MenuItem("Pasta", 250),
            MenuItem("Burger", 180),
            MenuItem("Coke", 60),
            MenuItem("Ice Cream", 90),
            MenuItem("Pizza", 300),
        ]

    def display_menu(self):
        print("\n------ MENU ------")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print("------------------")

    def get_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
