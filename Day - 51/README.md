# Day 51 - Internet Speed Twitter Bot 🤖📡

## Project Overview
An automated bot that tests your internet speed and tweets at your ISP if the speeds are below what you're paying for.

## What I Learned
- Advanced Selenium WebDriver automation
- Web element interaction and timing
- Social media automation
- Speed testing automation
- Error handling in web automation

## Features
- Automated speed testing using Speedtest.net
- Twitter login and posting automation
- Speed comparison with promised speeds
- Automated complaint generation

## How It Works
1. Opens Speedtest.net and runs a speed test
2. Captures download and upload speeds
3. Compares with promised speeds
4. If speeds are below promised, logs into Twitter
5. Posts a complaint tweet to the ISP

## Setup Instructions

### Prerequisites
- Python 3.x
- Chrome browser
- ChromeDriver (automatically managed by Selenium 4.x)
- Twitter account

### Installation
1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Update credentials in main.py:
```python
TWITTER_EMAIL = "your_email@example.com"
TWITTER_PASSWORD = "your_password"
```

3. Set your promised speeds:
```python
PROMISED_DOWN = 150  # Your promised download speed
PROMISED_UP = 10     # Your promised upload speed
```

### Running the Bot
```bash
python main.py
```

## Important Notes
- **Security**: Never commit real credentials to version control
- **Rate Limits**: Be aware of Twitter's posting limits
- **Legal**: Ensure compliance with terms of service
- **Timing**: The bot includes delays for page loading

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Chrome**: Web browser for automation
- **XPath/CSS Selectors**: Element location
- **Time module**: Delays and timing

## Potential Improvements
- Add error handling for network issues
- Implement headless browser mode
- Add logging for debugging
- Store credentials securely
- Add retry mechanisms
- Support multiple ISPs

## Disclaimer
This project is for educational purposes. Always respect website terms of service and rate limits when automating interactions.