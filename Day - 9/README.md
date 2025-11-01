# Day 9 - Secret Bidder

## Project Overview
A secret auction bidding program where multiple participants can place bids privately, and the highest bidder wins the auction.

## Features
- **Multiple bidders**: Support for unlimited number of participants
- **Private bidding**: Screen clears between bids for privacy
- **Automatic winner selection**: Finds and announces the highest bidder
- **Input validation**: Handles names and bid amounts
- **ASCII art logo**: Visual auction hammer display

## How to Run
```bash
python Secret-Bidder.py
```

## How It Works
1. Display auction logo
2. Collect bidder name and bid amount
3. Store bid in dictionary
4. Clear screen for next bidder's privacy
5. Continue until no more bidders
6. Determine and announce the winner

## Files
- `Secret-Bidder.py` - Main auction program
- `art.py` - ASCII art auction hammer logo

## Example Usage
```
Enter your name: ALICE
How much you want to bid: $150
Are there any other bidders? Type 'yes' or 'no': yes

Enter your name: BOB
How much you want to bid: $200
Are there any other bidders? Type 'yes' or 'no': no

Congratulations😊! BOB!
You have won the auction with a bid amount of $200.
```

## Learning Objectives
- Dictionaries and key-value pairs
- Functions with parameters
- While loops and user input
- Screen clearing for privacy
- Finding maximum values in dictionaries