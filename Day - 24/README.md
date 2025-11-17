# Day 24 - Notes Manager 📝

## Project Overview
Built a comprehensive command-line notes management system with file I/O operations. This project demonstrates file handling, data persistence, and modular programming principles for creating practical utility applications.

## What I Learned
- **File I/O Operations**: Reading, writing, and appending to text files
- **Data Persistence**: Storing and retrieving data between program sessions
- **Modular Programming**: Separating concerns across multiple modules
- **Error Handling**: Managing file operations and user input validation
- **Menu-Driven Interface**: Creating interactive command-line applications
- **CRUD Operations**: Create, Read, Update, Delete functionality

## Key Features
- ✅ Add new notes with automatic file creation
- ✅ View all stored notes with numbered display
- ✅ Search notes by keyword (case-insensitive)
- ✅ Delete specific notes by number
- ✅ Replace/edit existing notes
- ✅ Clear all notes with confirmation
- ✅ Persistent storage in text file
- ✅ Clean menu-driven interface

## Application Structure

### Modules Implemented
- **main.py**: Menu system and application flow control
- **file_manager.py**: File operations (create, read, write, append)
- **actions.py**: Note management functions (add, view, search, delete, replace, clear)

### Core Functions
- **File Management**: Automatic file creation and data persistence
- **Note Operations**: Full CRUD functionality for note management
- **Search System**: Keyword-based note searching
- **User Interface**: Interactive menu with input validation

## Menu Options
1. **Add Note**: Create and store new notes
2. **View Notes**: Display all notes with numbering
3. **Search Notes**: Find notes containing specific keywords
4. **Delete Note**: Remove individual notes by number
5. **Replace Note**: Edit existing notes
6. **Clear All Notes**: Delete all notes with confirmation
7. **Exit**: Close the application

## Technical Implementation
- File-based data storage using `notes.txt`
- Modular design for maintainable code
- Error handling for file operations
- Input validation and user confirmation
- Case-insensitive search functionality

## Data Flow
1. Application checks for existing notes file
2. Creates file if it doesn't exist
3. Loads existing notes for operations
4. Saves changes back to file automatically
5. Maintains data persistence between sessions

## How to Run
```bash
python main.py
```

**Concepts Mastered**: File I/O, Data Persistence, Modular Programming, CRUD Operations, Menu Systems