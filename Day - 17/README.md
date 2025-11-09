# Day 17 - Ultimate Quiz Challenge 🎯

## Project Overview
Interactive quiz game with multiple categories, featuring Object-Oriented Programming concepts and enhanced user experience with ASCII art and emojis.

## Features
- 🎨 ASCII art logo
- 🎉 Welcome interface with emojis
- 📚 5 quiz categories to choose from
- 🎲 Random question generation (10 questions per quiz)
- 🏆 Score tracking and performance feedback

## Quiz Categories
1. 🧠 **General Knowledge** - Fun facts and trivia
2. 🔢 **Mathematics** - Basic math concepts
3. 😄 **Funny Riddles** - Brain teasers and riddles
4. 📱 **Mobile Games** - Gaming trivia
5. ⚙️ **DevOps** - Technical concepts

## How to Run
```bash
python main.py
```

## File Structure
- `main.py` - Main game logic and user interface
- `quiz_brain.py` - QuizBrain class for managing quiz flow
- `question_model.py` - Question class model
- `data.py` - Question datasets for all categories
- `art.py` - ASCII art logo

## Concepts Learned
- Object-Oriented Programming (Classes and Objects)
- Class initialization and methods
- Data organization and management
- Random selection from datasets
- User input validation
- Enhanced UI with emojis

## Sample Output
```
 ██████╗ ██╗   ██╗██╗███████╗
██╔═══██╗██║   ██║██║╚══███╔╝
██║   ██║██║   ██║██║  ███╔╝ 
██║▄▄ ██║██║   ██║██║ ███╔╝  
╚██████╔╝╚██████╔╝██║███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝

🎉 Welcome to the Ultimate Quiz Challenge! 🎉

📚 Choose your quiz category:
1. 🧠 General Knowledge
2. 🔢 Mathematics
3. 😄 Funny Riddles
4. 📱 Mobile Games
5. ⚙️ DevOps
```

## Performance Feedback
- 8-10 correct: 🎉 Excellent! You're a quiz master!
- 6-7 correct: 😊 Great job! Well done!
- 4-5 correct: 😐 Not bad! Keep practicing!
- 0-3 correct: 😔 Better luck next time!