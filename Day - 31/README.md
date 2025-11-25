# Day 31 - Flash Card App (Flashy) 🃏

## Project Overview
Interactive language learning flashcard application with automatic card flipping, progress tracking, and spaced repetition. Learn French vocabulary with visual feedback and persistent progress saving.

## What I Learned
- **Tkinter Canvas**: Advanced canvas operations and image manipulation
- **Timer Functions**: Using window.after() for delayed operations
- **Data Persistence**: Saving learning progress to CSV files
- **Exception Handling**: Managing missing files gracefully
- **Spaced Repetition**: Removing known words from study deck
- **Image Integration**: Working with PNG images in GUI applications

## Key Features
- **Auto-flip Cards**: Cards flip from French to English after 3 seconds
- **Progress Tracking**: Removes known words from study deck
- **Data Persistence**: Saves words to learn for future sessions
- **Visual Feedback**: Different card designs for front/back
- **Interactive Buttons**: Right/wrong buttons with custom images
- **Exception Handling**: Creates learning file if it doesn't exist

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Files & Directory Structure
```
Day - 31/
├── main.py
├── requirements.txt
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv (generated)
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
```

## Game Mechanics
1. **Card Display**: Shows French word on front of card
2. **Auto-flip**: After 3 seconds, reveals English translation
3. **User Choice**: Click ✓ (known) or ✗ (unknown)
4. **Progress Saving**: Unknown words saved for future study
5. **Adaptive Learning**: Known words removed from deck

## Technical Implementation
- **Canvas Operations**: Dynamic text and image updates
- **Timer Management**: Canceling and resetting flip timers
- **Data Processing**: Converting between DataFrame and dictionary formats
- **File Handling**: Reading/writing CSV files with pandas
- **Exception Recovery**: Fallback to original dataset if progress file missing

## Learning Algorithm
- Uses spaced repetition principle
- Focuses study time on unknown words
- Tracks learning progress across sessions
- Reduces deck size as vocabulary improves

---
*Day 31 of 100 Days of Python Challenge*