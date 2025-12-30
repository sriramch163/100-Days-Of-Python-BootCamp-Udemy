# Day 62 - Cafe and WiFi Website 🏪☕

## Project Overview
A Flask web application that allows users to discover and add cafes with WiFi information. Users can view existing cafes and contribute new ones with ratings for coffee quality, WiFi strength, and power socket availability.

## Features
- **Home Page**: Welcome page with navigation
- **View Cafes**: Display all cafes in a table format with ratings
- **Add Cafe**: Form to submit new cafe information
- **Responsive Design**: Bootstrap-powered responsive UI
- **Data Persistence**: CSV file storage for cafe data

## Technologies Used
- **Flask**: Web framework
- **Flask-Bootstrap**: UI styling and components
- **Flask-WTF**: Form handling and validation
- **WTForms**: Form creation and validation
- **CSV**: Data storage
- **HTML/CSS**: Frontend structure and styling

## Project Structure
```
Day - 62/
├── static/
│   └── css/
│       └── styles.css          # Custom CSS styles
├── templates/
│   ├── base.html              # Base template with Bootstrap
│   ├── index.html             # Home page
│   ├── cafes.html             # Display all cafes
│   └── add.html               # Add new cafe form
├── cafe-data.csv              # CSV database
├── main.py                    # Main Flask application
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Access the Website**:
   - Open browser and go to `http://localhost:5002`

## Usage

### Viewing Cafes
- Navigate to the "Show Me!" page to see all registered cafes
- View cafe details including location, hours, and ratings

### Adding a New Cafe
1. Click "Add a New Cafe"
2. Fill out the form with:
   - Cafe name
   - Google Maps location URL
   - Opening and closing times
   - Coffee quality rating (☕ scale)
   - WiFi strength rating (💪 scale)
   - Power socket availability (🔌 scale)
3. Submit the form to add to the database

## Key Learning Concepts

### Flask Web Development
- **Routing**: Multiple routes with GET/POST methods
- **Templates**: Jinja2 templating with inheritance
- **Static Files**: CSS and asset management
- **Form Handling**: Processing user input securely

### Form Validation
- **WTForms Integration**: Form classes with validation
- **Field Types**: StringField, SelectField with choices
- **Validators**: DataRequired, URL validation
- **CSRF Protection**: Built-in security features

### Data Management
- **CSV Operations**: Reading and writing data
- **File Handling**: Proper encoding and error handling
- **Data Persistence**: Maintaining state between requests

### Bootstrap Integration
- **Flask-Bootstrap**: Seamless Bootstrap integration
- **Responsive Design**: Mobile-friendly layouts
- **Form Styling**: Professional form appearance

## Code Highlights

### Form Class Definition
```python
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", 
                          validators=[DataRequired(), URL()])
    coffee_rating = SelectField("Coffee Rating", 
                               choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
```

### CSV Data Handling
```python
with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
    csv_file.write(f"\n{form.cafe.data},{form.location.data}...")
```

## Possible Enhancements
- Database integration (SQLite/PostgreSQL)
- User authentication and profiles
- Image upload for cafes
- Search and filter functionality
- Rating system with user reviews
- Map integration for location display

## Dependencies
- Bootstrap_Flask==2.2.0
- Flask==2.3.2
- WTForms==3.0.1
- Flask_WTF==1.2.1
- Werkzeug==3.0.0

---

**Day 62 of 100 Days of Python** 🐍  
*Focus: Advanced Flask Web Development with Forms and Data Persistence*