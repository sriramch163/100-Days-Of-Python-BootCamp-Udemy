# NATO Phonetic Alphabet - Enhanced with Exception Handling 📻

## Project Overview
Enhanced NATO phonetic alphabet converter with robust error handling. Converts words to NATO phonetic codes while gracefully handling invalid input.

## What I Learned
- **Exception Handling**: Try/except/else blocks for error management
- **Recursion**: Function calling itself for retry logic
- **KeyError Handling**: Managing dictionary key lookup failures
- **User Input Validation**: Ensuring only valid characters are processed

## Key Features
- Converts any word to NATO phonetic alphabet
- Handles invalid characters gracefully
- Recursive retry mechanism for invalid input
- Clear error messages for user guidance

## How to Run
```bash
python main.py
```

## Files
- `main.py` - Enhanced main logic with exception handling
- `nato_phonetic_alphabet.csv` - NATO alphabet data

## Exception Handling Implementation
```python
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
    generate_phonetic()  # Recursive retry
else:
    print(output_list)
```

## Technical Concepts
- Try/except/else control flow
- KeyError exception handling
- Recursive function calls
- Input validation and sanitization

---
*Day 30 - Exception Handling Enhancement*