# customer.py

import time

class Customer:
    def __init__(self, name):
        self.name = name
        self.table_no = None
        self.tip = 0

    def choose_table(self):
        self.table_no = int(input("Choose your table (1-4): "))
        print(f"\n🪑 Table {self.table_no} reserved for you!")

    def eat_food(self):
        print("\n🍴 Eating your food...")
        time.sleep(5)
        print("That was delicious!")

    def give_tip(self):
        choice = input("Would you like to give a tip? (yes/no): ").lower()
        if choice == "yes":
            self.tip = int(input("Enter tip amount: ₹"))
        else:
            print("No worries, thank you for visiting!")
