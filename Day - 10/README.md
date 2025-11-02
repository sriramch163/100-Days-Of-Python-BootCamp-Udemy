# Day 10 - Calculator

A simple calculator program that performs basic arithmetic operations with a user-friendly interface.

## Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Square Operation**: Calculate square of a number (**)
- **Continuous Calculation**: Continue calculating with previous result
- **New Calculation**: Start fresh calculation
- **ASCII Art Logo**: Displays calculator logo on startup

## How to Use

1. Run the program
2. Enter your first number
3. Choose an operation from the displayed symbols
4. For square operation (**), only first number is needed
5. For other operations, enter second number
6. View the result
7. Choose what to do next:
   - **'y'**: Continue with the result
   - **'n'**: Start new calculation
   - **'e'**: Exit the calculator

## Requirements

- Python 3.x
- `art` module for logo display

## Installation

```bash
pip install art
```

## Usage Example

```
Enter you first number? : 10
+
-
*
/
**
Which operation did you choose?
+
Enter your second number? : 5
10 + 5 = 15
Type 'y' to continue calculating with 15, or type 'n' to start new calculation, or type 'e' for exit the calculator: y
```