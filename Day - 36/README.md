# Day 36 - Stock News Alert System 📈

## Project Overview
Automated stock monitoring system that tracks Tesla stock price changes and sends SMS alerts with relevant news when significant price movements occur (>5% change).

## What I Learned
- **Stock Market APIs**: Working with Alpha Vantage for real-time stock data
- **News APIs**: Integrating NewsAPI for relevant financial news
- **Data Processing**: Analyzing time series stock data and calculating percentage changes
- **List Comprehensions**: Processing JSON data and creating formatted messages
- **Multi-API Integration**: Combining three different APIs in one application
- **Financial Calculations**: Computing stock price differences and percentage changes
- **Conditional Logic**: Triggering alerts based on threshold conditions

## Key Features
- **Stock Price Monitoring**: Tracks Tesla (TSLA) daily closing prices
- **Percentage Change Calculation**: Compares yesterday vs day before yesterday
- **Threshold-based Alerts**: Only sends notifications for >5% price changes
- **News Integration**: Fetches top 3 relevant news articles
- **SMS Notifications**: Sends formatted alerts via Twilio
- **Visual Indicators**: Uses 🔺/🔻 emojis for price direction
- **Error Handling**: HTTP status validation for all API calls

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Get API credentials:
   - **Alpha Vantage**: Free stock API key from alphavantage.co
   - **NewsAPI**: Free news API key from newsapi.org
   - **Twilio**: Account SID, Auth Token, and phone number from twilio.com
3. Update credentials in `main.py`:
   ```python
   STOCK_API_KEY = "your_alpha_vantage_api_key"
   NEWS_API_KEY = "your_news_api_key"
   TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
   TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
   TWILIO_PHONE = "your_twilio_phone_number"
   YOUR_PHONE = "your_phone_number"
   ```
4. Run the monitor:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 36/
├── main.py
├── requirements.txt
└── README.md
```

## APIs Used
- **Alpha Vantage**: `https://www.alphavantage.co/query` - Stock market data
- **NewsAPI**: `https://newsapi.org/v2/everything` - Financial news articles
- **Twilio SMS**: SMS notification service

## Technical Implementation
- **Time Series Analysis**: Processes daily stock data chronologically
- **Percentage Calculation**: `(current - previous) / current * 100`
- **Threshold Logic**: Only triggers when `abs(percentage) > 5`
- **Data Slicing**: Extracts first 3 articles using `[:3]`
- **Message Formatting**: Combines stock data with news headlines
- **Batch SMS**: Sends separate message for each news article

## Alert Message Format
```
TSLA: 🔺7%
Headline: Tesla Reports Record Quarterly Earnings
Brief: Tesla Inc. announced record-breaking quarterly results...
```

## Automation Potential
- **Scheduled Execution**: Run daily after market close
- **Multiple Stocks**: Monitor portfolio of different stocks
- **Custom Thresholds**: Different alert levels for different stocks
- **Email Integration**: Additional notification channels
- **Database Logging**: Track historical alerts and performance

## Financial Use Cases
- Day trading alerts for significant price movements
- Investment portfolio monitoring
- News-driven trading decisions
- Risk management notifications

---
*Day 36 of 100 Days of Python Challenge*