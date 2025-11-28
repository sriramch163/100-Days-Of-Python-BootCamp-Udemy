# Day 34 - Ultimate Quiz Challenge 🧠

## Project Overview
Advanced GUI quiz application with multiple categories, player customization, and interactive interface. Features modular design with separate classes for different functionalities.

## What I Learned
- **Advanced OOP**: Multiple class interactions and modular design
- **Tkinter Styling**: TTK widgets, custom styles, and advanced layouts
- **Data Organization**: Structured quiz data with multiple categories
- **GUI State Management**: Button states and dynamic content updates
- **Error Handling**: Graceful fallbacks for missing image files
- **Random Sampling**: Dynamic question selection from larger datasets
- **Visual Feedback**: Color-coded responses and interactive elements

## Key Features
- **Multiple Categories**: 5 quiz categories (General Knowledge, Math, Riddles, Mobile Games, DevOps)
- **Player Personalization**: Name input and personalized results
- **Random Questions**: 10 randomly selected questions per quiz
- **Visual Feedback**: Green/red canvas feedback for correct/incorrect answers
- **Score Tracking**: Real-time score updates and final results
- **Professional UI**: Dark theme with custom styling and ASCII art logo
- **Image Integration**: Custom True/False button images with text fallbacks

## How to Run
```bash
python main.py
```

## Files & Directory Structure
```
Day - 34/
├── main.py          # Main application and category selection
├── ui.py            # Quiz interface and GUI logic
├── quiz_brain.py    # Quiz logic and question management
├── question_model.py # Question class definition
├── data.py          # Quiz questions and categories
├── art.py           # ASCII art logo
├── test_gui.py      # Testing file
├── true.png         # True button image
└── false.png        # False button image
```

## Quiz Categories
1. **🧠 General Knowledge** - Interesting facts and trivia
2. **🔢 Mathematics** - Math concepts and calculations
3. **😄 Funny Riddles** - Brain teasers and logic puzzles
4. **📱 Mobile Games** - Gaming industry knowledge
5. **⚙️ DevOps** - Development and operations concepts

## Technical Architecture
- **Question Model**: Simple class for question data structure
- **Quiz Brain**: Logic for question management and scoring
- **UI Interface**: Tkinter-based GUI with visual feedback
- **Main Controller**: Category selection and application flow
- **Data Module**: Structured question database

## Advanced Features
- **Modular Design**: Separate files for different responsibilities
- **Error Recovery**: Text buttons if images are missing
- **Dynamic Sampling**: Random question selection from larger pools
- **State Management**: Disabled buttons after quiz completion
- **Custom Styling**: TTK styles for professional appearance

## User Experience Flow
1. **Welcome Screen**: Logo display and name input
2. **Category Selection**: Radio buttons for quiz topics
3. **Quiz Interface**: Question display with True/False buttons
4. **Visual Feedback**: Color changes for answer feedback
5. **Results Display**: Final score and completion message

---
*Day 34 of 100 Days of Python Challenge*