# Day 8 - Caesar Cipher

## Project Overview
A Python implementation of the Caesar Cipher encryption and decryption algorithm. This classic cryptographic technique shifts each letter in the alphabet by a specified number of positions.

## Features
- **Encrypt messages**: Convert plain text to cipher text
- **Decrypt messages**: Convert cipher text back to plain text
- **Custom shift values**: Choose any shift amount
- **Non-alphabetic character preservation**: Numbers, spaces, and symbols remain unchanged
- **Continuous operation**: Option to encrypt/decrypt multiple messages

## How to Run
```bash
python ceaser.py
```

## How It Works
1. Choose to encode or decode
2. Enter your message
3. Specify the shift number
4. View the result
5. Option to continue with another message

## Files
- `ceaser.py` - Main program with Caesar cipher logic
- `art.py` - ASCII art logo display

## Example
```
Type 'encode' to encrypt, type 'decode' to decrypt: encode
Type your message: hello world
Type the shift number: 5
Here is the encoded result: mjqqt btwqi
```

## Learning Objectives
- Function parameters and arguments
- Function with inputs
- Positional vs keyword arguments
- Import statements and modules