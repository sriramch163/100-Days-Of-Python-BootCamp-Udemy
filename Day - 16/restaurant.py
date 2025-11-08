# restaurant.py

import time
from waiter import Waiter
from chef import Chef
from customer import Customer
from menu import Menu
from order import Order
from bill import Bill
from utils import random_waiter
from banner import show_banner

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.waiters = [Waiter("Henry"), Waiter("Simmy")]
        self.chef = Chef("Gordon")
        self.menu = Menu()

    def open_shop(self):
        show_banner()
        print("🛍️ Shop Open!")
        cmd = input("Type 'open' to enter into the restaurant: ").lower()
        if cmd != "open":
            print("Come back later!")
            return

        name = input("Enter your name: ").strip()
        customer = Customer(name)
        waiter = random_waiter(self.waiters)

        waiter.greet_customer(name)
        waiter.show_tables()
        customer.choose_table()

        order = Order()
        while True:
            self.menu.display_menu()
            item_name = input("Enter item name to order (or 'done' to finish): ").strip()
            if item_name.lower() == "done":
                break
            item = self.menu.get_item(item_name)
            if item:
                qty = int(input(f"Enter quantity for {item_name}: "))
                order.add_item(item, qty)
            else:
                print("❌ Item not found, try again.")

        waiter.take_order(customer.table_no)
        self.chef.prepare_order(customer.table_no)
        waiter.serve_order(customer.table_no)
        customer.eat_food()

        more = input("Would you like to order anything else? (yes/no): ").lower()
        if more == "yes":
            self.open_shop()
            return

        bill = Bill(customer.name, order)
        total = bill.generate_bill()
        bill.payment_process(total)
        customer.give_tip()
        print("\n💖 Thank you for dining with us!")
        time.sleep(2)
