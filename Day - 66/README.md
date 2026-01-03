# Day 66 - Cafe & WiFi REST API 🏪☕

## Project Overview
A comprehensive REST API built with Flask and SQLAlchemy for managing a database of cafes with WiFi information. This project demonstrates RESTful API design principles, database operations, and HTTP methods.

## Features
- **GET** random cafe information
- **GET** all cafes in the database
- **GET** cafes by location search
- **POST** new cafe entries
- **PATCH** update cafe prices
- **DELETE** remove cafes (with API key authentication)

## Technologies Used
- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **SQLite** - Database
- **HTML** - Basic frontend template

## API Endpoints

### 1. Home Page
- **URL**: `/`
- **Method**: GET
- **Description**: Displays welcome page with API documentation link

### 2. Random Cafe
- **URL**: `/random`
- **Method**: GET
- **Description**: Returns a random cafe from the database
- **Response**: JSON object with cafe details

### 3. All Cafes
- **URL**: `/all`
- **Method**: GET
- **Description**: Returns all cafes ordered by name
- **Response**: JSON array of all cafes

### 4. Search Cafes
- **URL**: `/search?loc=<location>`
- **Method**: GET
- **Description**: Find cafes by location
- **Parameters**: `loc` - location to search for
- **Response**: JSON array of matching cafes or 404 error

### 5. Add New Cafe
- **URL**: `/add`
- **Method**: POST
- **Description**: Add a new cafe to the database
- **Body Parameters**:
  - `name` - Cafe name
  - `map_url` - Google Maps URL
  - `img_url` - Image URL
  - `loc` - Location
  - `sockets` - Has power sockets (boolean)
  - `toilet` - Has toilet facilities (boolean)
  - `wifi` - Has WiFi (boolean)
  - `calls` - Can take calls (boolean)
  - `seats` - Number of seats
  - `coffee_price` - Price of coffee

### 6. Update Price
- **URL**: `/update-price/<cafe_id>?new_price=<price>`
- **Method**: PATCH
- **Description**: Update coffee price for a specific cafe
- **Parameters**: 
  - `cafe_id` - ID of the cafe
  - `new_price` - New price value

### 7. Delete Cafe
- **URL**: `/report-closed/<cafe_id>?api-key=<key>`
- **Method**: DELETE
- **Description**: Remove a cafe from the database
- **Parameters**:
  - `cafe_id` - ID of the cafe to delete
  - `api-key` - Authentication key (TopSecretAPIKey)

## Database Schema

### Cafe Model
- `id` - Primary key (Integer)
- `name` - Cafe name (String, unique)
- `map_url` - Google Maps URL (String)
- `img_url` - Image URL (String)
- `location` - Location (String)
- `seats` - Number of seats (String)
- `has_toilet` - Toilet availability (Boolean)
- `has_wifi` - WiFi availability (Boolean)
- `has_sockets` - Power sockets availability (Boolean)
- `can_take_calls` - Call-friendly environment (Boolean)
- `coffee_price` - Coffee price (String)

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Access the API**:
   - Base URL: `http://127.0.0.1:5000`
   - Documentation: Available on home page

## Testing with Postman

### GET Requests
- Test `/random`, `/all`, and `/search` endpoints directly in browser or Postman

### POST Request (Add Cafe)
- Method: POST
- URL: `http://127.0.0.1:5000/add`
- Body: x-www-form-urlencoded
- Include all required form parameters

### PATCH Request (Update Price)
- Method: PATCH
- URL: `http://127.0.0.1:5000/update-price/1?new_price=£5.50`

### DELETE Request (Remove Cafe)
- Method: DELETE
- URL: `http://127.0.0.1:5000/report-closed/1?api-key=TopSecretAPIKey`

## Key Learning Concepts

### REST API Principles
- **GET** - Retrieve data
- **POST** - Create new resources
- **PATCH** - Update existing resources
- **DELETE** - Remove resources

### HTTP Status Codes
- `200` - Success
- `404` - Not Found
- `403` - Forbidden

### Database Operations
- SQLAlchemy ORM usage
- Database model creation
- CRUD operations
- Query filtering and ordering

### Security Features
- API key authentication for delete operations
- Input validation and error handling

## Project Structure
```
Day - 66/
├── instance/
│   └── cafes.db          # SQLite database
├── templates/
│   └── index.html        # Home page template
├── main.py               # Main Flask application
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Error Handling
- 404 errors for non-existent cafes
- 403 errors for unauthorized delete attempts
- Proper JSON error responses with descriptive messages

## Future Enhancements
- User authentication system
- Rate limiting
- Data validation
- API versioning
- Comprehensive error logging

---

**Day 66 Complete!** ✅  
*REST API Development with Flask & SQLAlchemy*