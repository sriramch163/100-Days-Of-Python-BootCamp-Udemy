# bill.py

import time

class Bill:
    def __init__(self, customer_name, order):
        self.customer_name = customer_name
        self.order = order

    def generate_bill(self):
        print("\n------ BILL ------")
        print(f"Customer: {self.customer_name}")
        total = 0
        for item, qty in self.order.items:
            print(f"- {item.name} x{qty} = ₹{item.price * qty}")
            total += item.price * qty
        print("------------------")
        print(f"Total Amount: ₹{total}")
        return total

    def payment_process(self, total):
        amount = int(input("Enter payment amount: ₹"))
        change = amount - total
        print("\nProcessing transaction...")
        time.sleep(3)
        print(f"✅ Payment successful! You paid ₹{amount}, change ₹{change}.")
