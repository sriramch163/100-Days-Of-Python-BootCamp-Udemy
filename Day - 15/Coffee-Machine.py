# main.py
import time
import random
import sys
import os
from datetime import datetime
from collections import Counter
from coffee_data import MENU, resources, quotes
from art import (
    coffee_machine_logo,
    loading_ascii,
    drink_ascii_map,
    start_screen,
    off_screen,
)

profit = 0


# ---------------------- Utility Functions ---------------------- #
def clear_screen():
    """Clears the console screen on Windows, macOS, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    print("\n📋 Menu:")
    for drink, info in MENU.items():
        print(f"- {drink.title():<12} ₹{info['cost']}")
    print()


def show_random_quote():
    """Displays a random coffee quote while order is being prepared."""
    quote, author = random.choice(quotes)
    print("\n💭 While we prepare your drink, here's a coffee thought:")
    print(f"   {quote}")
    print(f"   — {author}\n")
    time.sleep(2)


def show_ascii_loading(drink_name="your drink"):
    """Simulates brewing animation with clean output."""
    for frame in loading_ascii:
        sys.stdout.write("\r" + f"{frame} ({drink_name.title()})".ljust(60))
        sys.stdout.flush()
        time.sleep(0.7)
    sys.stdout.write("\r" + f"[==========] Done! ☕ {drink_name.title()} Ready!".ljust(60))
    sys.stdout.flush()
    time.sleep(1)
    print("\n")


def check_and_refill(order_ingredients):
    """Checks resources and refills automatically if low."""
    global resources
    for item in order_ingredients:
        if item not in resources or order_ingredients[item] > resources[item]:
            print("\n⚠️ Not enough resources. Refilling...")
            time.sleep(2)
            for i in range(3):
                print(f"Refilling {'.' * (i+1)}", end="\r")
                time.sleep(1)
            resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
                "chocolate": 50,
                "ice": 100,
            }
            print("✅ Refill Complete!\n")
            return


def make_coffee(drink_name, order_ingredients):
    """Prepares the coffee."""
    check_and_refill(order_ingredients)
    print(f"\n☕ Now Serving: {drink_name.title()} ☕")
    show_random_quote()
    show_ascii_loading(drink_name)
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\nYour {drink_name.title()} is ready!\n")
    print(drink_ascii_map.get(drink_name, ""))


def process_final_payment(total_bill):
    """Handles payment at end of order."""
    print(f"\n💰 Your total bill is ₹{total_bill}")
    amount = float(input("Enter payment amount: ₹"))
    print("Processing payment", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(1)

    if amount >= total_bill:
        print("\n✅ Payment received successfully!")
        change = round(amount - total_bill, 2)
        if change > 0:
            print(f"Here is your change: ₹{change}")
        return amount
    else:
        print("\n❌ Insufficient payment. Money refunded.")
        return 0


def summarize_order(order_list):
    """Summarize repeated orders (Latte × 2)."""
    counter = Counter(order_list)
    summary = [f"{item.title()} × {count}" for item, count in counter.items()]
    return summary


# ---------------------- Coffee Machine Core ---------------------- #
def coffee_machine():
    global profit
    print("☕ Welcome to BrewBox Coffee Machine! ☕")

    user = input("Enter your name : ").lower()

    # 🧑‍💼 Host Admin Mode
    if user == "host":
        while True:
            cmd = input(
                "\nType 'resource' to check stock, 'profit' to view earnings, or 'back' to return: "
            ).lower()
            if cmd == "resource":
                print("\n📦 Current Resources:")
                for item, qty in resources.items():
                    print(f"- {item.title():<10}: {qty}")
            elif cmd == "profit":
                print(f"\n💰 Total Profit Earned: ₹{profit}")
            elif cmd == "back":
                print("\nReturning to Coffee Machine...")
                time.sleep(1)
                clear_screen()                      # ✅ Clear screen before showing menu again
                print(start_screen)
                time.sleep(1)
                print(coffee_machine_logo)
                coffee_machine()                    # ✅ Restart as normal coffee machine
                return
            else:
                print("Invalid command. Try again.")

    print_menu()

    customer = user.title()
    orders = []
    total_bill = 0

    while True:
        choice = input(f"\n{customer}, what would you like? ").lower()
        if choice not in MENU:
            print("❌ Invalid choice. Try again.")
            continue

        drink = MENU[choice]
        make_coffee(choice, drink["ingredients"])
        orders.append(choice)
        total_bill += drink["cost"]

        more = input("\nWould you like to order more? (yes/no): ").lower()
        if more == "yes":
            print_menu()
            continue
        else:
            break

    # Payment section
    paid = process_final_payment(total_bill)
    if paid >= total_bill:
        profit += total_bill

    # Receipt section
    now = datetime.now().strftime("%I:%M %p")
    print("\n🧾 Receipt")
    print("=" * 45)
    print(f"Customer: {customer}")
    print(f"🕒 Order Time: {now}")
    print("\nItems Ordered:")
    for item in summarize_order(orders):
        print(f"  - {item}")
    print(f"\nTotal Bill : ₹{total_bill}")
    print("=" * 45)
    print("Thank you for your visit! ☕💖")

    # Shutdown prompt
    shut = input("\nPlease shut down the coffee machine by typing 'off': ").lower()
    if shut == "off":
        print(off_screen)
        time.sleep(1)
        print("Thanks for using our Coffee Machine! 🙏☕")
        restart = input("\nType 'yes' to start again or 'no' to exit: ").lower()
        if restart == "yes":
            clear_screen()
            print(start_screen)
            time.sleep(1)
            print(coffee_machine_logo)
            coffee_machine()
        else:
            print("Goodbye! Have a great day! 🌟")
            exit()


# ---------------------- MAIN CONTROLLER ---------------------- #
if __name__ == "__main__":
    while True:
        cmd = input("\nType 'start' to start the coffee machine: ").lower()
        if cmd == "start":
            print(start_screen)
            time.sleep(1)
            print(coffee_machine_logo)
            coffee_machine()
        elif cmd == "off":
            print(off_screen)
            time.sleep(1)
            print("Thanks for using BrewBox Coffee Machine! 🙏☕")
            break
        else:
            print("Invalid command. Please type 'start'.")
