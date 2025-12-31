# Day 63 - Virtual Bookshelf with SQLAlchemy

## 🎯 Project Overview
A comprehensive library management web application built with Flask and SQLAlchemy. This project demonstrates database integration, CRUD operations, and advanced Flask concepts for managing a personal book collection.

## 🚀 Features
- **Book Management**: Add, edit, delete, and view books
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Rating System**: Rate books from 1-10
- **Responsive Interface**: Clean HTML interface for book management
- **Data Persistence**: Books stored permanently in SQLite database

## 🛠️ Technologies Used
- **Flask**: Web framework for Python
- **SQLAlchemy**: Object-Relational Mapping (ORM) library
- **Flask-SQLAlchemy**: Flask extension for SQLAlchemy
- **SQLite**: Lightweight database for data storage
- **Jinja2**: Template engine for dynamic HTML rendering

## 📋 Requirements
```
Flask==3.0.0
flask_sqlalchemy==3.1.1
SQLAlchemy==2.0.25
```

## 🔧 Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Access the Application**:
   - Open your browser and navigate to `http://localhost:5000`

## 🎮 How to Use

1. **View Library**: Home page displays all books in your collection
2. **Add Books**: Click "Add New Book" to add title, author, and rating
3. **Edit Ratings**: Click "Edit Rating" next to any book to update its rating
4. **Delete Books**: Click "Delete" to remove books from your library
5. **Empty Library**: Shows "Library is empty" message when no books exist

## 📁 Project Structure
```
Day - 63/
├── instance/
│   └── books.db           # SQLite database file
├── templates/
│   ├── index.html         # Main library view
│   ├── add.html          # Add new book form
│   └── edit_rating.html  # Edit book rating form
├── main.py               # Main Flask application
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🔍 Key Concepts Learned

### SQLAlchemy ORM
- **Database Models**: Creating Book model with mapped columns
- **Database Operations**: CRUD operations using SQLAlchemy
- **Query Building**: Using `db.select()` and `db.session.execute()`
- **Database Relationships**: Understanding primary keys and constraints

### Flask-SQLAlchemy Integration
- **Database Configuration**: Setting up SQLite database URI
- **Application Context**: Creating tables within app context
- **Session Management**: Adding, committing, and deleting records

### Advanced Flask Concepts
- **Route Parameters**: Using `request.args.get()` for URL parameters
- **Form Handling**: Processing POST requests with form data
- **Error Handling**: Using `db.get_or_404()` for safe record retrieval
- **URL Generation**: Dynamic URL creation with `url_for()`

## 🗄️ Database Schema

### Book Model
```python
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
```

## 🔧 API Endpoints

- **GET /**: Display all books in library
- **GET/POST /add**: Add new book form and processing
- **GET/POST /edit**: Edit book rating form and processing
- **GET /delete**: Delete book by ID

## 🚀 Potential Enhancements
- User authentication and multiple libraries
- Book categories and genres
- Search and filter functionality
- Book cover image uploads
- Reading progress tracking
- Book recommendations
- Export library to CSV/PDF
- Advanced sorting options

## 📚 Learning Outcomes
- SQLAlchemy ORM fundamentals
- Database design and relationships
- CRUD operations in web applications
- Flask-SQLAlchemy integration
- Form handling and validation
- Database migration concepts
- Web application architecture

---

**Day 63 Complete!** ✅  
*Database-driven web applications with Flask and SQLAlchemy*