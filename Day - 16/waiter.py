# waiter.py

import time

class Waiter:
    def __init__(self, name):
        self.name = name

    def greet_customer(self, customer_name):
        print(f"\n👨‍🍳 {self.name}: Hello {customer_name}! Welcome to Python Bistro!")

    def show_tables(self):
        print("\nAvailable Tables: 1, 2, 3, 4")

    def take_order(self, table_number):
        print(f"\n🧾 {self.name}: Taking order from table {table_number}...")
        time.sleep(3)
        print("Order taken successfully!")

    def serve_order(self, table_number):
        print(f"\n🍽️ {self.name}: Serving order to table {table_number}...")
