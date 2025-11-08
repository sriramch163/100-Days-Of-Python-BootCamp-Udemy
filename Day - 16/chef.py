# chef.py

import time
from utils import random_quote

class Chef:
    def __init__(self, name):
        self.name = name

    def prepare_order(self, table_number):
        print(f"\n👩‍🍳 Chef {self.name}: Preparing order for table {table_number}...")
        for _ in range(3):
            print(random_quote())
            time.sleep(2)
        print(f"\n👩‍🍳 Chef {self.name}: Table {table_number} order completed!")
