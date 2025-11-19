# Day 26 - NATO Phonetic Alphabet Converter 📡

## Project Overview
Built a NATO phonetic alphabet converter using pandas for CSV data processing and list comprehensions for efficient data transformation. This project demonstrates data analysis fundamentals and advanced Python syntax.

## What I Learned
- **Pandas Library**: CSV file reading and DataFrame operations
- **List Comprehensions**: Efficient data transformation and filtering
- **Dictionary Comprehensions**: Creating dictionaries from iterables
- **Data Processing**: Working with structured data from external files
- **DataFrame Iteration**: Using iterrows() for row-by-row processing
- **Advanced Python Syntax**: Concise and readable code patterns

## Key Features
- ✅ CSV data loading with pandas
- ✅ Dictionary creation from DataFrame using comprehension
- ✅ Word-to-phonetic conversion using list comprehension
- ✅ Case-insensitive input handling
- ✅ Clean, efficient code structure
- ✅ External data file integration

## Technical Implementation

### Data Processing Flow
1. **CSV Loading**: Read NATO phonetic alphabet from CSV file
2. **Dictionary Creation**: Transform DataFrame to dictionary using comprehension
3. **User Input**: Accept word input with case conversion
4. **Conversion**: Map each letter to phonetic code using list comprehension
5. **Output**: Display phonetic alphabet list

### Code Structure
```
Day - 26/
├── main.py                    # Main application logic
├── nato_phonetic_alphabet.csv # NATO phonetic data
└── README.md                  # Project documentation
```

### Key Code Concepts
- **Dictionary Comprehension**: `{row.letter:row.code for (index, row) in data.iterrows()}`
- **List Comprehension**: `[phonetic_dict[letter] for letter in word]`
- **Pandas Integration**: `pandas.read_csv()` for data loading
- **DataFrame Iteration**: `data.iterrows()` for row processing

## Example Usage
```
Input: "HELLO"
Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

Input: "python"
Output: ['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

## Data Source
- **NATO Phonetic Alphabet**: Complete A-Z mapping from CSV file
- **Format**: Two columns (letter, code) with 26 entries
- **Standards**: Official NATO/ICAO phonetic alphabet codes

## Libraries Used
- **pandas**: For CSV data processing and DataFrame operations
- **Built-in modules**: For basic input/output operations

## How to Run
```bash
python main.py
```

**Concepts Mastered**: Pandas Library, List Comprehensions, Dictionary Comprehensions, CSV Processing, Data Analysis