# Day 16 - Restaurant Management System 🍽️

## 🎯 Project Overview
**Python Bistro** - A comprehensive restaurant management system demonstrating Object-Oriented Programming (OOP) principles through a multi-class interactive dining experience.

## 📚 Concepts Learned
- **Object-Oriented Programming (OOP)**
- **Classes and Objects**
- **Instance Variables and Methods**
- **Class Initialization (__init__)**
- **Multi-file Project Structure**
- **Import Statements and Modules**
- **Encapsulation and Data Organization**
- **Object Interaction and Communication**

## 🏗️ Class Architecture
```
Restaurant (Main Controller)
├── Customer (Dining experience)
├── Waiter (Service management)
├── Chef (Food preparation)
├── Menu & MenuItem (Food catalog)
├── Order (Order tracking)
└── Bill (Payment processing)
```

## 🚀 Features
- **Multi-Class Design**: 8 interconnected classes
- **Interactive Dining**: Table selection, ordering, eating
- **Dynamic Menu**: Object-based menu items
- **Order Management**: Add multiple items with quantities
- **Bill Generation**: Automated billing with itemized receipt
- **Staff Interaction**: Random waiter assignment
- **Payment System**: Transaction processing with change calculation
- **Tip System**: Optional gratuity feature

## 🛠️ Project Structure
```
Day - 16/
├── main.py          # Entry point
├── restaurant.py    # Main Restaurant class
├── customer.py      # Customer class
├── waiter.py        # Waiter class
├── chef.py          # Chef class
├── menu.py          # Menu and MenuItem classes
├── order.py         # Order management class
├── bill.py          # Bill generation class
├── utils.py         # Utility functions
├── banner.py        # Welcome banner
└── README.md        # Project documentation
```

## 💻 How to Run
```bash
cd "Day - 16"
python main.py
```

## 🎮 User Experience Flow
1. **Welcome** - Restaurant banner display
2. **Entry** - Type 'open' to enter
3. **Registration** - Provide customer name
4. **Seating** - Choose table (1-4)
5. **Ordering** - Select items from menu
6. **Service** - Waiter takes order, chef prepares
7. **Dining** - Enjoy your meal
8. **Payment** - Bill generation and payment
9. **Tip** - Optional gratuity
10. **Farewell** - Thank you message

## 📋 Menu Items
| Item | Price |
|------|-------|
| Pasta | ₹250 |
| Burger | ₹180 |
| Coke | ₹60 |
| Ice Cream | ₹90 |
| Pizza | ₹300 |

## 🔧 Key Classes & Methods

### Restaurant Class
- `__init__(name)` - Initialize restaurant with staff
- `open_shop()` - Main restaurant operation flow

### Customer Class
- `choose_table()` - Table selection
- `eat_food()` - Dining simulation
- `give_tip()` - Tip processing

### Menu Classes
- `MenuItem(name, price)` - Individual menu item
- `Menu.display_menu()` - Show available items
- `Menu.get_item(name)` - Retrieve specific item

### Order Class
- `add_item(item, quantity)` - Add items to order
- `calculate_total()` - Compute total cost
- `show_order()` - Display current order

### Bill Class
- `generate_bill()` - Create itemized bill
- `payment_process(total)` - Handle payment transaction

## 🧠 OOP Concepts Applied
- **Classes**: 8 distinct classes with specific responsibilities
- **Objects**: Multiple instances (waiters, menu items)
- **Encapsulation**: Data and methods bundled in classes
- **Abstraction**: Complex operations simplified through methods
- **Composition**: Restaurant composed of other objects
- **Instance Variables**: Object-specific data storage
- **Method Interaction**: Objects communicating through methods

## 🎯 Learning Outcomes
- Understanding of OOP fundamentals
- Class design and object creation
- Multi-file project organization
- Object interaction patterns
- Real-world application of OOP concepts
- Code reusability and maintainability
- Separation of concerns principle

## 🔄 Program Flow
```
main.py → Restaurant.open_shop() → Customer creation → 
Waiter assignment → Table selection → Menu display → 
Order creation → Chef preparation → Bill generation → 
Payment processing → Tip handling → Exit
```

---
**Day 16 Complete** ✅ | **Next**: Day 17 - Advanced OOP Concepts