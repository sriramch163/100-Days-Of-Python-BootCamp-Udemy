# Day 55 - Flask Number Guessing Game

## Project Overview
A web-based number guessing game built with Flask where users try to guess a random number between 0 and 9.

## Features
- Random number generation (0-9)
- Web interface with animated GIFs
- Dynamic feedback based on user guesses
- Color-coded responses (purple for too high, red for too low, green for correct)

## Concepts Learned
- Flask web framework basics
- URL routing with parameters
- Dynamic content generation
- HTML integration in Flask
- Web application structure

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser and navigate to `http://127.0.0.1:5000`

4. Try guessing by adding a number to the URL (e.g., `http://127.0.0.1:5000/5`)

## Game Rules
- Guess a number between 0 and 9
- Navigate to `/<your_guess>` to make a guess
- Get visual feedback with animated GIFs
- Keep trying until you find the correct number!

## Technologies Used
- Python 3.x
- Flask 2.3.3
- HTML (inline)
- Giphy GIFs for visual feedback