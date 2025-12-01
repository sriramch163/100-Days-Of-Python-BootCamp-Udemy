# Day 37 - Habit Tracker with Pixela API 📊

## Project Overview
Habit tracking application using Pixela API to create visual graphs for daily activities. Demonstrates full CRUD operations (Create, Read, Update, Delete) with a habit tracking service.

## What I Learned
- **RESTful API Operations**: Complete CRUD implementation with HTTP methods
- **API Authentication**: Using custom headers for token-based authentication
- **DateTime Formatting**: Converting dates to API-required format (YYYYMMDD)
- **HTTP Methods**: POST, PUT, DELETE operations for different functionalities
- **JSON Data Handling**: Sending structured data to external APIs
- **Habit Tracking**: Building systems for personal productivity monitoring
- **API Endpoints**: Working with multiple related endpoints for different operations

## Key Features
- **User Account Creation**: Register new users with Pixela service
- **Graph Creation**: Set up custom habit tracking graphs
- **Daily Logging**: Record daily habit completion (commits/activities)
- **Data Updates**: Modify existing entries with new values
- **Data Deletion**: Remove incorrect or unwanted entries
- **Visual Tracking**: Generate web-based habit tracking graphs
- **Token Authentication**: Secure API access with user tokens

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update your credentials in `main.py`:
   ```python
   TOKEN = "your_unique_token"
   USER = "your_username"
   GRAPH_ID = "your_graph_id"
   ```
3. Uncomment desired operations and run:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 37/
├── main.py
├── requirements.txt
└── README.md
```

## API Operations Implemented

### 1. User Creation
```python
POST https://pixe.la/v1/users
# Creates new user account with terms agreement
```

### 2. Graph Creation
```python
POST https://pixe.la/v1/users/{username}/graphs
# Creates habit tracking graph with custom parameters
```

### 3. Pixel Creation (Daily Entry)
```python
POST https://pixe.la/v1/users/{username}/graphs/{graph_id}
# Logs daily habit completion
```

### 4. Pixel Update
```python
PUT https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}
# Updates existing daily entry
```

### 5. Pixel Deletion
```python
DELETE https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}
# Removes daily entry
```

## Graph Configuration
- **Unit**: "commit" (customizable to steps, hours, etc.)
- **Type**: "int" (integer values)
- **Color**: "ajisai" (purple theme)
- **Date Format**: YYYYMMDD (e.g., 20251130)

## Authentication
Uses custom header authentication:
```python
headers = {"X-USER-TOKEN": "your_token"}
```

## Practical Applications
- **Coding Practice**: Track daily commits or coding hours
- **Exercise Habits**: Log workouts, steps, or gym sessions
- **Learning Goals**: Monitor study time or lessons completed
- **Health Tracking**: Record water intake, meditation, sleep
- **Productivity**: Track tasks completed or goals achieved

## Visual Output
Creates web-accessible graphs at:
```
https://pixe.la/v1/users/{username}/graphs/{graph_id}.html
```

## Best Practices Demonstrated
- Modular endpoint construction
- Proper HTTP method usage for different operations
- Token-based authentication
- Date formatting for API compatibility
- Commented code sections for selective execution

---
*Day 37 of 100 Days of Python Challenge*