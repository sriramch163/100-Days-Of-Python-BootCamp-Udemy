# Day 23 - Crossroads Game Enhanced 🚗🐢

## Project Overview
Built an enhanced version of the classic Frogger-style crossing game with advanced features including traffic lights, multiplayer support, and dynamic car generation. This project demonstrates complex game mechanics and multi-object interaction systems.

## What I Learned
- **Multi-Object Management**: Handling multiple game entities simultaneously
- **Game State Management**: Traffic light system affecting gameplay
- **Multiplayer Implementation**: Supporting 1-2 player modes
- **Dynamic Object Creation**: Random car generation with varied properties
- **Collision Detection**: Player-car interaction systems
- **Progressive Difficulty**: Level-based speed increases

## Key Features
- ✅ 1-2 player support with different colored turtles
- ✅ Traffic light system controlling car movement
- ✅ Dynamic car generation with random sizes and colors
- ✅ Progressive difficulty with increasing car speeds
- ✅ Multiple movement options (walk, jump, lateral movement)
- ✅ Level progression and scoring system
- ✅ Collision detection and game over mechanics
- ✅ Modular code structure across multiple files

## Game Components

### Classes Implemented
- **Player**: Turtle character with movement and collision detection
- **CarManager**: Handles car creation, movement, and speed management
- **Scoreboard**: Level tracking and game over display
- **TrafficLight**: Timed traffic control system
- **Controls**: Centralized input handling for multiple players

### Controls
- **Player 1**: Arrow Keys (Up/Down/Left/Right)
- **Player 2**: WASD Keys (W/A/S/D)
- **Special**: Down Arrow / S Key for jump movement

### Traffic Light System
- Alternates between green (4 seconds) and red (4 seconds)
- Cars only move during green light phases
- Adds strategic timing element to gameplay

## Technical Implementation
- Random car generation with varied sizes and colors
- Time-based traffic light switching mechanism
- Multi-player collision detection system
- Progressive difficulty scaling with level increases
- Modular architecture for maintainable code

## Game Mechanics
1. Players start at bottom of screen
2. Cars spawn randomly from right side during green lights
3. Players must cross to top without hitting cars
4. Reaching finish line increases level and car speed
5. Game ends on collision with any car

## How to Run
```bash
python main.py
```

**Concepts Mastered**: Multi-Object Management, Game State Systems, Multiplayer Design, Dynamic Content Generation