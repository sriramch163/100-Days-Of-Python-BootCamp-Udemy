from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def sqr():
    return n1 ** 2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "**": sqr
}

def calci():
    while True:
        first_number = float(input("Enter you first number? : "))
        
        while True:
            for symbol in operations:
                print(symbol)
            operator = input("Which operation did you choose?\n")
            if operator == "**":
                result = first_number ** 2
                print(f"{first_number} {operator} 2 = {result}")
                choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation, or type 'e' for exit the calculator: ")
                if choice == "y":
                    first_number = result
                elif choice == "n":
                    print("\n" * 100)
                    print(logo)
                    break
                elif choice == "e":
                    print("THANK YOU FOR USING OUR CALCULATOR❤️")
                    return
                else:
                    break
            else:
                second_number = float(input("Enter your second number? : "))

                result = operations[operator](first_number, second_number)
                print(f"{first_number} {operator} {second_number} = {result}")

                choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation, or type 'e' for exit the calculator: ")

                if choice == "y":
                    first_number = result
                elif choice == "n":
                    print("\n" * 100)
                    print(logo)
                    break
                elif choice == "e":
                    print("THANK YOU FOR USING OUR CALCULATOR😁")
                    return
                else:
                    break

calci()