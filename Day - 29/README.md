# Day 29 - Password Manager 🔐

## Project Overview
Secure password manager application with GUI that generates strong passwords and stores login credentials. Features password generation, data validation, and file storage.

## What I Learned
- **Advanced Tkinter**: Canvas widgets, PhotoImage, and complex layouts
- **File I/O**: Writing and appending data to text files
- **Data Validation**: Input checking and error handling
- **Message Boxes**: User confirmation and error dialogs
- **List Comprehensions**: Efficient password generation
- **Random Module**: Secure password creation with shuffling

## Key Features
- **Password Generator**: Creates strong 12-16 character passwords
- **Data Storage**: Saves credentials to local text file
- **Input Validation**: Prevents empty field submissions
- **User Confirmation**: Asks before saving credentials
- **Auto-focus**: Cursor starts in website field
- **Visual Interface**: Logo display with canvas widget

## How to Run
```bash
python main.py
```

## Files
- `main.py` - Main application logic
- `logo.png` - Application logo image
- `data.txt` - Generated file storing saved passwords

## Directory Structure
```
Day - 29/
├── main.py
├── logo.png
└── data.txt (generated)
```

## Security Features
- Strong password generation (letters, numbers, symbols)
- Random shuffling for unpredictable patterns
- Local file storage (no cloud dependency)
- Input validation to prevent incomplete entries

## Technical Concepts
- Canvas widget for image display
- MessageBox for user interactions
- File handling with context managers
- List comprehensions for password generation
- Grid layout management
- Event-driven programming

---
*Day 29 of 100 Days of Python Challenge*