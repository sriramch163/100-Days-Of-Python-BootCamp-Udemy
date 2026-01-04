# Day 67 - RESTful Blog with Flask

## Project Overview
A full-featured blog application built with Flask that demonstrates RESTful routing, database operations, and rich text editing capabilities.

## Features
- Create, read, update, and delete blog posts (CRUD operations)
- Rich text editor using CKEditor
- SQLAlchemy database integration
- Bootstrap styling
- Form validation with WTForms
- Responsive design

## Technologies Used
- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-WTF**: Form handling and validation
- **CKEditor**: Rich text editor
- **Bootstrap**: Frontend styling
- **SQLite**: Database

## Installation & Setup

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser and navigate to `http://localhost:5002`

## Project Structure
```
Day - 67/
├── instance/
│   └── posts.db          # SQLite database
├── static/
│   ├── assets/           # Images and favicon
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
├── templates/           # HTML templates
├── main.py             # Main application file
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## Key Learning Concepts
- RESTful API design principles
- Database relationships and migrations
- Form handling and validation
- Template inheritance
- Static file management
- CRUD operations with SQLAlchemy
- Rich text editing integration

## Routes
- `GET /` - Display all blog posts
- `GET /post/<id>` - Display individual post
- `GET /new-post` - Show create post form
- `POST /new-post` - Create new post
- `GET /edit-post/<id>` - Show edit form
- `POST /edit-post/<id>` - Update existing post
- `GET /delete/<id>` - Delete post
- `GET /about` - About page
- `GET /contact` - Contact page

## Database Schema
**BlogPost Model:**
- id (Primary Key)
- title (String, 250 chars)
- subtitle (String, 250 chars)
- date (String, 250 chars)
- body (Text)
- author (String, 250 chars)
- img_url (String, 250 chars)