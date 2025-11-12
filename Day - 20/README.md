# Day 20 - Snake Game (Part 1) 🐍

## Project Overview
Built the foundation of the classic Snake game using Python's Turtle graphics module. This project focuses on creating the snake body, implementing movement mechanics, and handling user input for directional control.

## What I Learned
- **Class-based Programming**: Created a Snake class to manage game objects
- **Turtle Graphics**: Advanced turtle module usage for game development
- **Event Handling**: Keyboard input detection and response
- **Game Logic**: Snake movement mechanics and direction control
- **List Manipulation**: Managing snake segments as a collection

## Key Features
- ✅ Snake body creation with multiple segments
- ✅ Smooth snake movement animation
- ✅ Keyboard controls (WASD keys)
- ✅ Direction change restrictions (can't reverse into itself)
- ✅ Object-oriented game structure

## Code Structure

### Snake Class
- `__init__()`: Initialize snake with starting segments
- `create_snake()`: Generate initial snake body
- `move_snake()`: Handle snake movement mechanics
- `control_snake()`: Set up keyboard event listeners
- Direction methods: `up()`, `down()`, `left()`, `right()`

### Controls
- **W**: Move Up
- **S**: Move Down  
- **A**: Move Left
- **D**: Move Right

## Technical Implementation
- Snake segments follow each other in sequence
- Head movement drives the entire body
- Direction changes are restricted to prevent self-collision
- Turtle graphics provide smooth animation

## Next Steps (Day 21)
- Add food generation and collision detection
- Implement score tracking
- Add game over conditions
- Complete the full Snake game experience

## How to Run
```bash
python snake.py
```

**Concepts Mastered**: OOP, Turtle Graphics, Event Handling, Game Development Basics