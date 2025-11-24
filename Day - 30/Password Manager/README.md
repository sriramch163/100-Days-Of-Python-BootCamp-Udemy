# Password Manager - Enhanced with JSON & Search 🔐

## Project Overview
Advanced password manager with JSON storage, search functionality, and comprehensive exception handling. Features secure password generation, data persistence, and credential lookup.

## What I Learned
- **JSON Handling**: Reading, writing, and updating JSON files
- **Exception Handling**: FileNotFoundError and data validation
- **Search Functionality**: Credential lookup and retrieval
- **Pyperclip Integration**: Automatic password copying to clipboard
- **Advanced Error Management**: Try/except/else/finally blocks

## Key Features
- **JSON Storage**: Structured data storage instead of plain text
- **Search Function**: Find saved credentials by website
- **Auto-copy**: Generated passwords copied to clipboard
- **Exception Handling**: Graceful error management
- **Data Validation**: Prevents empty field submissions
- **File Management**: Creates JSON file if not exists

## How to Run
```bash
python main.py
```

## Files
- `main.py` - Enhanced application with JSON and search
- `logo.png` - Application logo
- `data.json` - Generated JSON file for password storage

## New Features Added
- Search button for credential lookup
- JSON file format for better data structure
- Pyperclip integration for password copying
- Comprehensive exception handling
- Automatic file creation

## Exception Handling Implementation
```python
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
else:
    data.update(new_data)
finally:
    # Cleanup operations
```

---
*Day 30 - Exception Handling Enhancement*