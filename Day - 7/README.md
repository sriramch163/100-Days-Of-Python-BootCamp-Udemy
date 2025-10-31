# Day 7 - Hangman Game

## Project Overview
A classic Hangman word guessing game implemented in Python. Players try to guess a randomly selected word letter by letter before running out of lives.

## Features
- **Random word selection**: 100 game titles to guess from
- **Visual hangman stages**: ASCII art showing game progress
- **Lives system**: 6 attempts before game over
- **Duplicate guess detection**: Prevents repeated letter guesses
- **Win/lose conditions**: Clear feedback on game outcome

## How to Run
```bash
python hangman.py
```

## How It Works
1. A random word is selected from the word list
2. Player sees blanks representing each letter
3. Guess letters one at a time
4. Correct guesses reveal letters in the word
5. Wrong guesses reduce lives and advance hangman drawing
6. Win by guessing all letters or lose when lives reach zero

## Files
- `hangman.py` - Main game logic
- `hangman_art.py` - ASCII art for logo and hangman stages
- `hangman_words.py` - List of 100 game titles to guess

## Example Gameplay
```
****************************6/6 LIVES LEFT****************************
Word to guess: _ _ _ _ _ _ _ _ _
Guess a letter: e
Word to guess: _ _ _ e _ _ _ _ _
```

## Learning Objectives
- While loops and flow control
- Lists and random selection
- String manipulation
- Modular programming with imports
- Game state management