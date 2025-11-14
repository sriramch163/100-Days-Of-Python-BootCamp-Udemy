# Day 22 - Pong Game 🏓

## Project Overview
Built the classic Pong arcade game with enhanced features using Python's Turtle graphics. This project demonstrates advanced game development concepts including collision detection, scoring systems, and interactive gameplay mechanics.

## What I Learned
- **Game Development**: Complete game loop implementation
- **Collision Detection**: Ball-paddle and ball-wall interactions
- **Event Handling**: Continuous key press detection system
- **Modular Design**: Organized code across multiple classes
- **Game Physics**: Ball movement, bouncing, and speed mechanics
- **User Interface**: Dynamic scoring and winner display

## Key Features
- ✅ Two-player Pong gameplay
- ✅ Customizable player names
- ✅ Adjustable winning score
- ✅ Smooth paddle movement with boundary detection
- ✅ Ball physics with acceleration after paddle hits
- ✅ Dynamic color-changing ball
- ✅ Sound effects for collisions and scoring
- ✅ Power-up system with shrinking ball effect
- ✅ Winner announcement screen

## Game Components

### Classes Implemented
- **Paddle**: Player-controlled paddles with movement constraints
- **Ball**: Game ball with physics, collision detection, and effects
- **Scoreboard**: Score tracking and winner display
- **SmallBall**: Power-up collectible with timed respawn
- **BallColor**: Random color generation system

### Controls
- **Left Paddle**: W (up), S (down)
- **Right Paddle**: Arrow Up, Arrow Down

### Power-Up System
- Gold power-up balls spawn every 5 seconds
- Collecting shrinks the main ball for 10 seconds
- Makes gameplay more challenging and strategic

## Technical Implementation
- Continuous key press detection for smooth movement
- Ball speed increases with each paddle collision
- Boundary collision detection for walls and paddles
- Modular class structure for maintainable code
- Sound integration using winsound module

## Game Flow
1. Player name input and winning score setup
2. Real-time paddle movement and ball physics
3. Collision detection and scoring
4. Power-up collection mechanics
5. Winner determination and display

## How to Run
```bash
python main.py
```

**Concepts Mastered**: Advanced OOP, Game Physics, Collision Detection, Event Systems, Modular Programming