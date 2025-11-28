# Day 33 - ISS Overhead Notifier 🛰️

## Project Overview
Real-time ISS (International Space Station) tracker that sends email notifications when the ISS is overhead during nighttime. Combines multiple APIs for location tracking and sunrise/sunset data.

## What I Learned
- **API Integration**: Working with REST APIs and JSON responses
- **HTTP Requests**: Using requests library for API calls
- **Error Handling**: Using raise_for_status() for HTTP error checking
- **Real-time Monitoring**: Continuous loop monitoring with time delays
- **Coordinate Mathematics**: Position comparison within degree ranges
- **DateTime Processing**: Working with UTC time and local time conversion
- **Email Automation**: Combining SMTP with API data for notifications

## Key Features
- **ISS Position Tracking**: Real-time ISS location via Open Notify API
- **Sunrise/Sunset Detection**: Determines if it's nighttime at your location
- **Proximity Detection**: Checks if ISS is within ±5 degrees of your position
- **Email Notifications**: Sends alerts when ISS is visible overhead
- **Continuous Monitoring**: Runs indefinitely with 60-second intervals
- **Dual Condition Logic**: Only notifies when ISS is overhead AND it's dark

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update your coordinates and email in `main.py`:
   ```python
   MY_LAT = 51.507351  # Your latitude
   MY_LONG = -0.127758  # Your longitude
   MY_EMAIL = "your_email@gmail.com"
   MY_PASSWD = "your_app_password"
   ```
3. Run the tracker:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 33/
├── main.py
└── requirements.txt
```

## APIs Used
- **ISS Location API**: `http://api.open-notify.org/iss-now.json`
- **Sunrise-Sunset API**: `https://api.sunrise-sunset.org/json`

## Technical Implementation
- **Position Comparison**: Checks if ISS coordinates are within ±5° range
- **Time Calculation**: Extracts hour from UTC timestamps for day/night detection
- **Continuous Loop**: 60-second intervals for real-time monitoring
- **Error Handling**: HTTP status checking with raise_for_status()
- **Email Integration**: SMTP notification system for alerts

## Logic Flow
1. **Get ISS Position**: Fetch current ISS coordinates
2. **Check Proximity**: Compare ISS location with user location (±5°)
3. **Check Time**: Determine if it's nighttime at user location
4. **Send Notification**: Email alert if both conditions are met
5. **Wait & Repeat**: 60-second delay before next check

## Practical Applications
- Astronomy enthusiasts tracking ISS passes
- Educational tool for space science
- Real-time satellite monitoring
- Location-based notification systems

---
*Day 33 of 100 Days of Python Challenge*