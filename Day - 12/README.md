# Day 12 - Number Guessing Game 🎯

## Project Overview
An interactive number guessing game where players try to guess a randomly generated number between 1-100 with limited attempts based on difficulty level.

## Features
- Random number generation (1-100)
- Two difficulty levels (Easy/Hard)
- Limited attempts system
- Interactive feedback with emojis
- Visual feedback for guesses (too high/low)
- Warning system for remaining attempts
- ASCII art logo

## How to Play
1. Run the program
2. Choose difficulty: 'easy' (10 attempts) or 'hard' (5 attempts)
3. Guess numbers between 1-100
4. Follow the hints (too high/too low)
5. Win by guessing correctly before running out of attempts!

## Game Rules
- **Easy Mode**: 10 attempts
- **Hard Mode**: 5 attempts
- Number range: 1-100
- Get feedback after each guess
- Warning when 2 or fewer attempts remain

## Concepts Learned
- **Scope**: Global vs Local variables
- **Constants**: Using uppercase for constant values
- **Function parameters and returns**
- **While loops with conditions**
- **Random number generation**
- **Input validation**
- **Game state management**

## Key Programming Concepts
- Global constants (`EASY_LEVEL_TURNS`, `HARD_LEVEL_TURNS`)
- Function scope and variable accessibility
- Return values for game flow control
- Conditional logic for difficulty selection

## Files
- `Guess-The-Number.py` - Main game file
- `art.py` - ASCII art logo (required)

## Usage
```bash
python Guess-The-Number.py
```

## Sample Output
```
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100... 🤔
Choose a difficulty — Type 'easy' or 'hard': easy
🧘 Easy mode activated! You get 10 attempts.

💭 You have 10 attempt(s) remaining...
Make a guess: 50
😈 Too high! Try again...
```