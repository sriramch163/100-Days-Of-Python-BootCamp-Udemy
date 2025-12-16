# Day 48 - Cookie Clicker Bot with Selenium 🍪🤖

## Project Overview
An automated Cookie Clicker bot using Selenium WebDriver that plays the popular incremental game by automatically clicking cookies and purchasing upgrades to maximize cookie production.

## What I Learned
- **Selenium WebDriver**: Browser automation and control
- **Web Element Interaction**: Finding and clicking elements by ID, class, and CSS selectors
- **Exception Handling**: Managing NoSuchElementException for robust automation
- **Timing and Delays**: Using sleep() and time-based logic for game automation
- **Game Strategy**: Implementing purchasing logic for optimal upgrade selection
- **Chrome Options**: Configuring browser settings for automation

## Key Features
- Automated cookie clicking for continuous cookie generation
- Smart upgrade purchasing system that buys the most expensive affordable item
- Language selection handling for international game versions
- Timer-based purchasing strategy (checks every 5 seconds)
- 5-minute runtime with final score reporting
- Error handling for missing elements and parsing issues

## How It Works
1. **Setup**: Launches Chrome browser with Selenium WebDriver
2. **Navigation**: Opens the Cookie Clicker game website
3. **Initialization**: Handles language selection and page loading
4. **Main Loop**: 
   - Continuously clicks the big cookie
   - Every 5 seconds, checks available upgrades
   - Purchases the most expensive affordable upgrade
   - Continues for 5 minutes total
5. **Results**: Reports final cookie count

## Technical Implementation
- Uses CSS selectors to find store products (product0-product17)
- Parses cookie count from game display text
- Implements reverse iteration to prioritize expensive upgrades
- Uses class attribute checking to identify affordable items

## Requirements
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver (managed automatically by Selenium 4.x)

## Installation & Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the bot:
```bash
python main.py
```

3. Watch the automation in action for 5 minutes!

## Game Strategy
The bot implements a greedy algorithm:
- Continuously generates cookies through clicking
- Prioritizes the most expensive upgrades for better cookie-per-second rates
- Balances clicking frequency with upgrade checking

## Learning Outcomes
- Browser automation fundamentals
- Web scraping with dynamic content
- Game automation strategies
- Error handling in web automation
- Timer-based event systems

## Future Enhancements
- Golden cookie detection and clicking
- Achievement tracking
- Multiple strategy implementations
- Performance optimization
- Headless browser mode

---
*Part of the 100 Days of Python Challenge - Day 48*