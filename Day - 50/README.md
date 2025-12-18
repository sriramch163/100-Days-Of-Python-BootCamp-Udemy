# Day 50 - Tinder Auto Swiper Bot 🤖💕

## Project Overview
An automated Tinder swiping bot using Selenium WebDriver that logs in through Facebook and automatically likes profiles.

## Features
- Facebook login integration
- Automated profile swiping (100 likes per day)
- Handle pop-ups and notifications
- Match detection and handling
- Error handling for various scenarios

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Chrome WebDriver**: Browser control
- **Facebook OAuth**: Authentication
- **XPath Selectors**: Element targeting

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download ChromeDriver and ensure it's in your PATH

3. Update credentials in main.py:
```python
FB_EMAIL = "your_facebook_email@example.com"
FB_PASSWORD = "your_facebook_password"
```

## How It Works

1. **Login Process**: Opens Tinder, clicks login, authenticates via Facebook
2. **Permission Handling**: Accepts location and notification permissions
3. **Auto Swiping**: Automatically likes 100 profiles with 1-second delays
4. **Error Handling**: Manages match pop-ups and loading delays

## Key Concepts Learned
- Advanced Selenium automation
- Multi-window handling
- Exception handling for web automation
- Social media API integration
- Browser profile management

## Security Notes
- Never commit real credentials to version control
- Use environment variables for sensitive data
- Be aware of platform terms of service

## Disclaimer
This project is for educational purposes only. Always respect platform terms of service and user privacy.

---
**Day 50 of 100 Days of Python Challenge**