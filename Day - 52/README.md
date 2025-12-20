# Day 52 - Instagram Follower Bot 🤖📱

## Project Overview
An automated Instagram follower bot that logs into Instagram, finds followers of a target account, and follows them automatically using Selenium WebDriver.

## Features
- Automated Instagram login
- Cookie consent handling
- Target account follower discovery
- Automated following with error handling
- Anti-bot detection measures (random delays)

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Chrome WebDriver**: Browser control
- **Python**: Core programming language

## Setup Instructions

### Prerequisites
1. Python 3.x installed
2. Chrome browser installed
3. Instagram account credentials

### Installation
1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Download ChromeDriver and ensure it's in your PATH

### Configuration
1. Update the following variables in `main.py`:
   - `SIMILAR_ACCOUNT`: Target account whose followers you want to follow
   - `USERNAME`: Your Instagram username
   - `PASSWORD`: Your Instagram password

## Usage
```bash
python main.py
```

## How It Works
1. **Login**: Automatically logs into Instagram with provided credentials
2. **Navigation**: Navigates to the target account's followers page
3. **Scrolling**: Scrolls through the followers modal to load more users
4. **Following**: Clicks follow buttons for discovered users
5. **Error Handling**: Handles already-followed users and click interceptions

## Important Notes
⚠️ **Disclaimer**: This bot is for educational purposes only. Use responsibly and in accordance with Instagram's Terms of Service.

### Best Practices
- Don't run the script too frequently to avoid detection
- Use reasonable delays between actions
- Consider Instagram's rate limits
- Respect other users' privacy

### Potential Issues
- Instagram may update their UI, requiring XPath/selector updates
- Account may get temporarily restricted for bot-like behavior
- Cookie consent dialogs may vary by region

## Key Learning Concepts
- Advanced Selenium automation
- Social media bot development
- Error handling in web automation
- Anti-detection techniques
- Modal and popup handling

## Files
- `main.py`: Main Instagram follower bot implementation
- `requirements.txt`: Required Python packages
- `README.md`: Project documentation

---
**Day 52 of 100 Days of Python** 🐍