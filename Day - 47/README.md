# Day 47 - Amazon Price Tracker 💰

## Project Overview
Automated Amazon price monitoring system that tracks product prices and sends email alerts when items drop below target thresholds. Demonstrates advanced web scraping with anti-detection techniques.

## What I Learned
- **Advanced Web Scraping**: Bypassing anti-bot measures with proper headers
- **Price Monitoring**: Automated price tracking and comparison logic
- **Email Automation**: SMTP integration for price alert notifications
- **Environment Variables**: Secure credential management with .env files
- **HTML Element Selection**: Targeting specific price and title elements
- **Data Processing**: String manipulation and type conversion for prices
- **Anti-Detection Techniques**: Using realistic browser headers

## Key Features
- **Amazon Price Scraping**: Extracts current product prices from Amazon
- **Price Threshold Monitoring**: Configurable buy price alerts
- **Email Notifications**: Automated alerts when prices drop
- **Product Title Extraction**: Includes product names in alerts
- **Environment Security**: Credentials stored in .env file
- **Header Spoofing**: Mimics real browser requests to avoid blocking

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create `.env` file with credentials:
   ```env
   SMTP_ADDRESS=smtp.gmail.com
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```
3. Update target price and product URL in `main.py`
4. Run the price tracker:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 47/
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## Technical Implementation

### 1. Anti-Detection Headers
```python
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
```

### 2. Price Extraction
```python
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
```

### 3. Product Title Extraction
```python
title = soup.find(id="productTitle").get_text().strip()
```

### 4. Email Alert System
```python
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    # Send email notification
```

## Web Scraping Challenges
- **Anti-Bot Protection**: Amazon blocks requests without proper headers
- **Dynamic Content**: Prices may be loaded via JavaScript
- **Rate Limiting**: Need delays between requests for multiple products
- **Element Changes**: HTML structure may change over time

## Security Features
- **Environment Variables**: Sensitive data stored in .env file
- **Email Authentication**: Secure SMTP login with app passwords
- **UTF-8 Encoding**: Proper character encoding for international products
- **No Hardcoded Credentials**: All secrets externalized

## Automation Potential
- **Scheduled Monitoring**: Run via cron jobs for continuous tracking
- **Multiple Products**: Monitor entire wishlist or category
- **Price History**: Store historical price data for trend analysis
- **Multiple Notifications**: SMS, Slack, or Discord integration

## Legal Considerations
- **Terms of Service**: Respect website terms and conditions
- **Rate Limiting**: Avoid overwhelming servers with requests
- **Personal Use**: Intended for personal price monitoring only
- **Robots.txt**: Check and respect site crawling policies

## Practical Applications
- Deal hunting and bargain finding
- Investment timing for expensive purchases
- Market research and price analysis
- Inventory management for resellers

---
*Day 47 of 100 Days of Python Challenge - Advanced Web Scraping*