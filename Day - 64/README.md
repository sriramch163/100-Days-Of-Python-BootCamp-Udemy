# Day 64 - My Top 10 Movies Website

## 🎬 Project Overview
A Flask web application that allows users to create and manage their personal top 10 movies list. Users can search for movies using The Movie Database (TMDb) API, add them to their collection, rate them, write reviews, and manage their rankings.

## ✨ Features
- **Movie Search**: Search for movies using TMDb API
- **Add Movies**: Add movies to your personal collection
- **Rate & Review**: Rate movies out of 10 and write personal reviews
- **Dynamic Ranking**: Movies are automatically ranked based on ratings
- **Edit & Delete**: Update ratings/reviews or remove movies
- **Responsive Design**: Bootstrap-powered responsive UI
- **Database Persistence**: SQLite database for data storage

## 🛠️ Technologies Used
- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite
- **Forms**: WTForms, Flask-WTF
- **API**: The Movie Database (TMDb) API
- **HTTP Requests**: Requests library

## 📁 Project Structure
```
Day - 64/
├── instance/
│   └── movies.db          # SQLite database
├── static/
│   └── css/
│       └── styles.css     # Custom CSS styles
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Home page (movie list)
│   ├── add.html           # Add movie form
│   ├── select.html        # Movie selection from search
│   └── edit.html          # Edit rating/review
├── main.py                # Main Flask application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🚀 How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Get TMDb API Key**:
   - Sign up at [The Movie Database](https://www.themoviedb.org/)
   - Get your API key
   - Replace `USE_YOUR_OWN_CODE` in `main.py` with your API key

3. **Run the Application**:
   ```bash
   python main.py
   ```

4. **Access the App**:
   - Open your browser and go to `http://127.0.0.1:5000`

## 🎯 Key Learning Objectives
- **Flask Web Development**: Building complete web applications
- **SQLAlchemy ORM**: Database modeling and operations
- **API Integration**: Working with external APIs (TMDb)
- **Form Handling**: WTForms for secure form processing
- **Template Inheritance**: Jinja2 templating system
- **Bootstrap Integration**: Responsive web design
- **CRUD Operations**: Create, Read, Update, Delete functionality

## 🔧 Core Concepts Demonstrated

### Database Operations
- SQLAlchemy ORM with Flask-SQLAlchemy
- Database model creation and relationships
- CRUD operations with proper error handling

### Web Development
- Flask routing and view functions
- Template rendering with Jinja2
- Form validation and processing
- Static file serving

### API Integration
- HTTP requests to external APIs
- JSON data processing
- Error handling for API calls

## 🎨 User Interface
- Clean, modern design with Bootstrap 5
- Card-based layout for movie display
- Responsive design for mobile compatibility
- Interactive forms with validation

## 📊 Database Schema
```sql
Movie Table:
- id (Primary Key)
- title (String, Unique)
- year (Integer)
- description (String)
- rating (Float)
- ranking (Integer)
- review (String)
- img_url (String)
```

## 🔄 Application Flow
1. **Home Page**: Display ranked movies
2. **Add Movie**: Search and select from TMDb
3. **Rate Movie**: Add personal rating and review
4. **Update**: Modify existing ratings/reviews
5. **Delete**: Remove movies from collection

## 🎓 Skills Developed
- Full-stack web development
- Database design and management
- API integration and data processing
- Form handling and validation
- Template-based UI development
- Error handling and user experience

## 🌟 Possible Enhancements
- User authentication system
- Movie recommendations
- Social sharing features
- Advanced search filters
- Movie watchlist functionality
- Export/import movie lists

---
**Day 64 of 100 Days of Python** 🐍