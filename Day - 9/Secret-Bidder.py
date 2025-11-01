from art import logo
print(logo)


def high_bid(biding_history):
    winner = ""
    highest_bid = 0
    #max(biding_history)
    for bidder in biding_history:
        bid_amount = biding_history[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Congratulations😊! {winner}!\nYou have won the auction with a bid amount of ${highest_bid}.")


bid = {}
continue1 = True
while continue1:
    name = input("Enter your name: ").upper()
    price = int(input("How much you want to bid: $"))
    bid[name] = price
    choice = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    if choice == "no":
        continue1 = False
        high_bid(bid)
    elif choice == "yes":
        print("\n" * 100)









