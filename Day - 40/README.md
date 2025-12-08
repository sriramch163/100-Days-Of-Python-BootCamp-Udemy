# Day 40 - Flight Club with Email Notifications ✈️

## Project Overview
Enhanced flight deal finder with customer email list management and multi-channel notifications. Searches for both direct and indirect flights, sending personalized alerts to subscribers via email, SMS, and WhatsApp.

## What I Learned
- **Email Automation**: SMTP integration for bulk email notifications
- **Customer Management**: Managing subscriber lists via Google Sheets
- **Indirect Flight Search**: Handling stopover flights when direct routes unavailable
- **Multi-channel Notifications**: Email, SMS, and WhatsApp integration
- **Advanced Error Handling**: Fallback mechanisms for flight searches
- **Data Enrichment**: Enhanced flight data with stopover information
- **Scalable Architecture**: Supporting multiple recipients efficiently

## Key Features
- **Customer Email Management**: Retrieves subscriber list from Google Sheets
- **Direct & Indirect Flights**: Searches both direct and stopover options
- **Smart Fallback**: Automatically searches indirect flights if no direct routes
- **Multi-channel Alerts**: Email, SMS, and WhatsApp notifications
- **Bulk Email Sending**: Sends alerts to all subscribers simultaneously
- **Stopover Information**: Includes number of stops in notifications
- **Price Comparison**: Alerts only when prices below target thresholds

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create `.env` file with credentials:
   ```env
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_SECRET=your_amadeus_secret
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   SHEETY_PRICES_ENDPOINT=your_prices_endpoint
   SHEETY_USERS_ENDPOINT=your_users_endpoint
   TWILIO_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_VIRTUAL_NUMBER=your_twilio_phone
   TWILIO_VERIFIED_NUMBER=your_verified_phone
   TWILIO_WHATSAPP_NUMBER=your_whatsapp_number
   EMAIL_PROVIDER_SMTP_ADDRESS=smtp.gmail.com
   MY_EMAIL=your_email@gmail.com
   MY_EMAIL_PASSWORD=your_app_password
   ```
3. Set up Google Sheets with two tabs:
   - **prices**: Destination cities and target prices
   - **users**: Customer email addresses
4. Run the flight club:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 40/
├── main.py                    # Main orchestrator with email integration
├── data_manager.py           # Google Sheets management (prices + users)
├── flight_search.py          # Amadeus API with direct/indirect search
├── flight_data.py            # Flight data model with stopover support
├── notification_manager.py   # Email, SMS, WhatsApp notifications
├── .env                      # Environment variables
├── requirements.txt
└── README.md
```

## New Features (vs Day 39)

### 1. Customer Email Management
- Retrieves subscriber emails from Google Sheets
- Supports bulk email notifications
- Separate sheet tab for user management

### 2. Indirect Flight Search
- Searches for stopover flights when direct unavailable
- Includes stop count in notifications
- Fallback mechanism for better deal finding

### 3. Email Notifications
- SMTP integration for email alerts
- Bulk sending to all subscribers
- UTF-8 encoding for special characters

### 4. Enhanced Messaging
- Different messages for direct vs indirect flights
- Includes stopover information
- Professional email formatting

## Google Sheets Structure

### Prices Sheet
| city | iataCode | lowestPrice |
|------|----------|-------------|
| Paris | PAR | 54 |
| Tokyo | TYO | 485 |

### Users Sheet
| firstName | lastName | whatIsYourEmail? |
|-----------|----------|------------------|
| John | Doe | john@example.com |
| Jane | Smith | jane@example.com |

## Notification Examples

### Direct Flight
```
Low price alert! Only GBP 299 to fly direct
from LON to PAR, on 2025-01-15 until 2025-01-22.
```

### Indirect Flight
```
Low price alert! Only GBP 450 to fly
from LON to TYO, with 1 stop(s)
departing on 2025-02-10 and returning on 2025-02-20.
```

## Technical Enhancements
- **Rate Limiting**: 2-second delays between API calls
- **Error Recovery**: Indirect search fallback
- **Bulk Operations**: Efficient multi-recipient email sending
- **Data Validation**: Checks for valid flight data before processing
- **Environment Management**: Centralized credential handling

## Automation Workflow
1. Retrieve destination data from Google Sheets
2. Update IATA codes if missing
3. Retrieve customer email list
4. Search for direct flights to each destination
5. If no direct flights, search for indirect options
6. Compare prices with target thresholds
7. Send notifications via email, SMS, and WhatsApp

## Security Best Practices
- Environment variables for all credentials
- SMTP authentication with app passwords
- OAuth2 for API access
- No hardcoded sensitive data

---
*Day 40 of 100 Days of Python Challenge*