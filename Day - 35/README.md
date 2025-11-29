# Day 35 - Rain Alert SMS Notifier ☔

## Project Overview
Automated weather monitoring system that sends SMS alerts when rain is predicted. Combines OpenWeatherMap API for weather data with Twilio SMS service for notifications.

## What I Learned
- **Weather API Integration**: Working with OpenWeatherMap forecast API
- **SMS Services**: Using Twilio API for programmatic SMS sending
- **API Parameters**: Handling latitude/longitude coordinates and API keys
- **Data Filtering**: Processing weather forecast data for specific conditions
- **Conditional Logic**: Weather condition code analysis for rain detection
- **Third-party Services**: Integrating multiple external APIs in one application
- **Environment Variables**: Secure handling of API keys and credentials

## Key Features
- **Weather Forecast Analysis**: Checks next 12 hours of weather data
- **Rain Detection**: Identifies rain conditions using weather codes (<700)
- **SMS Notifications**: Sends umbrella reminders via Twilio SMS
- **Location-based**: Uses GPS coordinates for accurate local weather
- **Automated Monitoring**: Can be scheduled for daily execution
- **Error Handling**: HTTP status checking for API reliability

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Get API credentials:
   - **OpenWeatherMap**: Sign up at openweathermap.org for API key
   - **Twilio**: Create account at twilio.com for Account SID and Auth Token
3. Update credentials in `main.py`:
   ```python
   account_sid = "your_twilio_account_sid"
   auth_token = "your_twilio_auth_token"
   api_key = "your_openweathermap_api_key"
   ```
4. Update location coordinates and phone numbers
5. Run the script:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 35/
├── main.py
└── requirements.txt
```

## APIs Used
- **OpenWeatherMap Forecast API**: `http://api.openweathermap.org/data/2.5/forecast`
- **Twilio SMS API**: For sending text message notifications

## Technical Implementation
- **Weather Code Analysis**: Codes <700 indicate precipitation (rain/snow)
- **Forecast Loop**: Checks next 4 time periods (12 hours)
- **Boolean Flag**: Tracks if rain is detected in any forecast period
- **SMS Trigger**: Sends notification only when rain is predicted
- **Error Handling**: API response validation with raise_for_status()

## Weather Condition Codes
- **200-299**: Thunderstorm ⛈️
- **300-399**: Drizzle 🌦️
- **500-599**: Rain 🌧️
- **600-699**: Snow ❄️
- **700+**: Atmosphere conditions (fog, mist, etc.)

## Automation Potential
- **Cron Jobs**: Schedule for daily morning execution
- **Cloud Deployment**: Run on AWS Lambda or similar services
- **Multiple Locations**: Monitor weather for different cities
- **Custom Conditions**: Alert for other weather conditions (snow, storms)
- **Multiple Recipients**: Send alerts to family/friends

## Security Best Practices
- Store API keys in environment variables
- Use Twilio's verified phone numbers for testing
- Implement rate limiting for API calls
- Monitor API usage and costs

---
*Day 35 of 100 Days of Python Challenge*