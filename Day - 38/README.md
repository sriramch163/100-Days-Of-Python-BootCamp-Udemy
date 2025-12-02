# Day 38 - Exercise Tracking with Natural Language Processing 🏋️

## Project Overview
Intelligent exercise tracking system that uses natural language processing to interpret workout descriptions and automatically logs them to a Google Sheet via Sheety API.

## What I Learned
- **Natural Language Processing**: Using Nutritionix API to parse exercise descriptions
- **Multi-API Integration**: Combining exercise analysis with spreadsheet automation
- **HTTP Authentication**: Different auth methods (API keys vs Basic auth)
- **Data Transformation**: Converting API responses to spreadsheet format
- **DateTime Formatting**: Custom date/time formatting for logging
- **User Input Processing**: Handling natural language exercise descriptions
- **Automated Logging**: Creating persistent workout records

## Key Features
- **Natural Language Input**: Describe exercises in plain English
- **Exercise Recognition**: AI-powered exercise identification and calorie calculation
- **Automatic Logging**: Direct integration with Google Sheets
- **Personalized Calculations**: Uses individual biometric data for accuracy
- **Real-time Tracking**: Instant workout logging with timestamps
- **Multiple Exercise Support**: Handles multiple exercises in single input
- **Calorie Estimation**: Automatic calorie burn calculation

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up APIs:
   - **Nutritionix**: Get API key and App ID from nutritionix.com
   - **Sheety**: Create Google Sheet and get Sheety endpoint
3. Update credentials in `main.py`:
   ```python
   API_KEY = "your_nutritionix_api_key"
   APP_ID = "your_nutritionix_app_id"
   USER_NAME = "your_sheety_username"
   USER_PASSWD = "your_sheety_password"
   SHEET_ENDPOINT = "your_sheety_endpoint"
   ```
4. Update personal data:
   ```python
   GENDER = "male/female"
   WEIGHT_KG = 75
   HEIGHT_CM = 183
   AGE = 21
   ```
5. Run the tracker:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 38/
├── main.py
├── requirements.txt
└── README.md
```

## APIs Used
- **Nutritionix Exercise API**: Natural language exercise processing
- **Sheety API**: Google Sheets integration for data storage

## Example Usage
```
Tell me which exercises you did: I ran 3 miles and did 20 push ups
```

**Output to Google Sheet:**
| Date | Time | Exercise | Duration | Calories |
|------|------|----------|----------|----------|
| 01/12/2025 | 14:30:25 | Running | 30 | 300 |
| 01/12/2025 | 14:30:25 | Push Ups | 5 | 25 |

## Technical Implementation
- **NLP Processing**: Nutritionix API interprets exercise descriptions
- **Biometric Integration**: Personal data for accurate calorie calculations
- **Data Mapping**: Converts API response to spreadsheet structure
- **Authentication**: API key headers + Basic auth for different services
- **Loop Processing**: Handles multiple exercises from single input

## Supported Exercise Types
- **Cardio**: Running, cycling, swimming, walking
- **Strength**: Push-ups, pull-ups, weight lifting
- **Sports**: Basketball, tennis, soccer, etc.
- **Activities**: Yoga, dancing, hiking, climbing

## Data Logged
- **Date**: Current date (DD/MM/YYYY format)
- **Time**: Current time (HH:MM:SS format)
- **Exercise**: Recognized exercise name
- **Duration**: Estimated duration in minutes
- **Calories**: Calculated calorie burn

## Automation Benefits
- No manual calorie counting
- Consistent workout logging
- Historical data tracking
- Progress monitoring
- Integration with existing spreadsheet workflows

## Practical Applications
- Personal fitness tracking
- Gym workout logging
- Diet and exercise coordination
- Fitness goal monitoring
- Health data collection

---
*Day 38 of 100 Days of Python Challenge*