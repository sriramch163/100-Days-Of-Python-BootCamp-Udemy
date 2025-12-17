# Day 49 - Automated Gym Class Booking Bot

## Project Overview
An automated gym class booking system using Selenium WebDriver that books Tuesday and Thursday 6 PM classes with network resilience and verification features.

## Features
- **Automated Login**: Secure login with credentials
- **Smart Class Selection**: Automatically finds and books Tuesday/Thursday 6 PM classes
- **Network Resilience**: Retry mechanism for handling network issues
- **Booking Verification**: Confirms bookings on "My Bookings" page
- **Status Tracking**: Tracks booked, waitlisted, and already booked classes
- **Chrome Profile**: Persistent browser session

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Chrome Options**: Custom browser configuration
- **WebDriverWait**: Explicit waits for elements
- **Exception Handling**: Robust error management

## Key Concepts Learned
- Advanced Selenium automation
- Network resilience patterns
- Browser profile management
- Element interaction strategies
- Retry mechanisms
- Web scraping with dynamic content

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Update credentials in main.py:
```python
ACCOUNT_EMAIL = "your_email@example.com"
ACCOUNT_PASSWORD = "your_password"
```

3. Run the script:
```bash
python main.py
```

## How It Works

1. **Setup**: Configures Chrome with persistent profile
2. **Login**: Automated login with retry mechanism
3. **Class Search**: Finds Tuesday/Thursday 6 PM classes
4. **Booking**: Books available classes or joins waitlists
5. **Verification**: Confirms all bookings on My Bookings page

## Error Handling
- TimeoutException handling for slow page loads
- NoSuchElementException for missing elements
- Retry wrapper for network resilience
- Verification system to ensure booking success

## Output
The script provides detailed feedback including:
- Booking attempts and results
- Already booked/waitlisted classes
- Verification of all bookings
- Success/failure summary

## Notes
- Requires manual Chrome profile setup initially
- Remember to quit Chrome before re-running if detach=True
- Handles both booking and waitlist scenarios
- Includes comprehensive error handling and retry logic