# Day 39 - Flight Deal Finder 🛫

## Project Overview
Comprehensive flight deal monitoring system that tracks flight prices across multiple destinations and sends notifications when deals are found. Uses Amadeus API for flight data and integrates with Google Sheets for destination management.

## What I Learned
- **Complex API Integration**: Working with Amadeus flight search API and OAuth2 authentication
- **Environment Variables**: Secure credential management using .env files
- **Object-Oriented Design**: Multiple classes with specific responsibilities
- **Data Processing**: Parsing complex JSON flight data structures
- **Rate Limiting**: Handling API rate limits with time delays
- **Multi-channel Notifications**: SMS and WhatsApp integration via Twilio
- **Automated Monitoring**: Continuous price tracking and alert systems

## Key Features
- **Flight Price Monitoring**: Tracks prices for multiple destinations over 6-month periods
- **IATA Code Management**: Automatically retrieves and updates airport codes
- **Deal Detection**: Compares current prices with target thresholds
- **Multi-notification Support**: SMS and WhatsApp alerts via Twilio
- **Google Sheets Integration**: Manages destination data and price targets
- **OAuth2 Authentication**: Secure API access with token management
- **Error Handling**: Comprehensive error management for API failures

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up APIs:
   - **Amadeus**: Get API key and secret from developers.amadeus.com
   - **Sheety**: Create Google Sheet integration at sheety.co
   - **Twilio**: Set up SMS/WhatsApp service at twilio.com
3. Create `.env` file with credentials:
   ```env
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_SECRET=your_amadeus_secret
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   TWILIO_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_VIRTUAL_NUMBER=your_twilio_phone_number
   TWILIO_VERIFIED_NUMBER=your_verified_phone_number
   TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
   ```
4. Update endpoints in respective files
5. Run the flight finder:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 39/
├── main.py                    # Main application orchestrator
├── data_manager.py           # Google Sheets data management
├── flight_search.py          # Amadeus API flight search
├── flight_data.py            # Flight data model and processing
├── notification_manager.py   # SMS/WhatsApp notifications
├── .env                      # Environment variables (not in repo)
├── requirements.txt
└── README.md
```

## Class Architecture

### DataManager
- Manages Google Sheets integration via Sheety API
- Retrieves and updates destination data
- Handles IATA code updates

### FlightSearch
- Handles Amadeus API authentication and requests
- Retrieves IATA codes for cities
- Searches for flight deals with specified parameters

### FlightData
- Data model for flight information
- Processes complex API responses
- Finds cheapest flights from multiple options

### NotificationManager
- Sends SMS notifications via Twilio
- Supports WhatsApp messaging
- Handles message formatting and delivery

## APIs Used
- **Amadeus Flight API**: Flight search and IATA code lookup
- **Sheety API**: Google Sheets integration for data management
- **Twilio API**: SMS and WhatsApp notifications

## Technical Implementation
- **OAuth2 Flow**: Automatic token generation and management
- **Rate Limiting**: 2-second delays between API calls
- **Error Handling**: Try-catch blocks for API failures
- **Data Validation**: Checks for valid flight data before processing
- **Price Comparison**: Compares current prices with target thresholds

## Notification Format
```
Low price alert! Only £299 to fly from LON to PAR,
on 2025-01-15 until 2025-01-22.
```

## Automation Potential
- **Scheduled Execution**: Run daily via cron jobs or cloud functions
- **Multiple Origins**: Monitor from different departure cities
- **Dynamic Pricing**: Adjust target prices based on historical data
- **Email Integration**: Additional notification channels
- **Database Storage**: Historical price tracking and analytics

## Security Features
- Environment variable management for sensitive data
- OAuth2 token-based authentication
- Secure API credential handling
- No hardcoded secrets in source code

---
*Day 39 of 100 Days of Python Challenge*