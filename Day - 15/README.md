# Day 15 - Coffee Machine ☕

## 🎯 Project Overview
**BrewBox Coffee Machine** - A comprehensive coffee vending machine simulator that demonstrates procedural programming concepts and modular code organization.

## 📚 Concepts Learned
- **Local Development Environment Setup**
- **Code Organization & Modular Programming**
- **File Imports & Module Management**
- **Data Structures (Dictionaries & Lists)**
- **Control Flow & Error Handling**
- **User Interface Design (CLI)**
- **Resource Management**
- **Payment Processing Logic**

## 🚀 Features
- **5 Coffee Varieties**: Espresso, Latte, Cappuccino, Mocha, Cold Brew
- **Resource Management**: Automatic refilling when ingredients run low
- **Payment System**: Bill calculation and change processing
- **Admin Mode**: Resource checking and profit tracking (login: "host")
- **Interactive UI**: ASCII art, loading animations, and coffee quotes
- **Order Summary**: Receipt generation with timestamps
- **Multiple Orders**: Add multiple items before payment

## 🛠️ Project Structure
```
Day - 15/
├── Coffee-Machine.py    # Main program logic
├── coffee_data.py       # Menu items, resources, and quotes
├── art.py              # ASCII art and animations
└── README.md           # Project documentation
```

## 💻 How to Run
```bash
cd "Day - 15"
python Coffee-Machine.py
```

## 🎮 Usage Instructions

### Customer Mode
1. Type `start` to begin
2. Enter your name
3. Select drinks from the menu
4. Add multiple items if desired
5. Complete payment
6. Receive receipt
7. Type `off` to shutdown

### Admin Mode
1. Type `start` to begin
2. Enter `host` as username
3. Available commands:
   - `resource` - Check ingredient levels
   - `profit` - View total earnings
   - `back` - Return to customer mode

## 📋 Menu & Pricing
| Drink | Price | Ingredients |
|-------|-------|-------------|
| Espresso | ₹120 | Water, Coffee |
| Latte | ₹200 | Water, Milk, Coffee |
| Cappuccino | ₹250 | Water, Milk, Coffee |
| Mocha | ₹280 | Water, Milk, Coffee, Chocolate |
| Cold Brew | ₹220 | Water, Coffee, Ice |

## 🔧 Key Functions
- `coffee_machine()` - Main program controller
- `make_coffee()` - Handles drink preparation
- `process_final_payment()` - Payment processing
- `check_and_refill()` - Resource management
- `summarize_order()` - Order consolidation

## 🎨 Special Features
- **ASCII Art**: Custom drink illustrations
- **Loading Animation**: Brewing simulation
- **Random Quotes**: Coffee-themed inspiration
- **Auto-Refill**: Seamless resource management
- **Receipt System**: Professional order summary

## 🧠 Programming Concepts Applied
- **Modular Design**: Separated data, art, and logic
- **Global Variables**: Profit and resource tracking
- **Dictionary Operations**: Menu and resource management
- **List Comprehensions**: Order summarization
- **Error Handling**: Input validation and resource checks
- **Time Module**: Animations and delays
- **String Formatting**: Receipt and display formatting

## 🎯 Learning Outcomes
- Understanding of local development environment
- Code organization best practices
- Module import and management
- Complex program flow control
- User experience design in CLI applications
- Data persistence concepts
- Resource management algorithms

---
**Day 15 Complete** ✅ | **Next**: Day 16 - Object-Oriented Programming