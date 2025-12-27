# Day 59 - Flask Blog Application

## 📝 Project Overview
A dynamic blog website built with Flask that fetches blog posts from an external API and displays them in a responsive Bootstrap-styled interface.

## 🎯 Learning Objectives
- Advanced Flask routing and templating
- API integration with external data sources
- Dynamic URL routing with parameters
- Template inheritance and includes
- Bootstrap integration with Flask
- Static file management

## 🛠️ Technologies Used
- **Flask**: Web framework for Python
- **Requests**: HTTP library for API calls
- **Bootstrap 5**: Frontend framework
- **Jinja2**: Template engine
- **HTML/CSS/JavaScript**: Frontend technologies

## 📁 Project Structure
```
Day - 59/
├── main.py                 # Flask application
├── requirements.txt        # Dependencies
├── static/                 # Static assets
│   ├── css/
│   │   └── styles.css     # Custom styles
│   ├── js/
│   │   └── scripts.js     # JavaScript functionality
│   └── assets/
│       ├── img/           # Images
│       └── favicon.ico    # Site icon
└── templates/             # HTML templates
    ├── header.html        # Header component
    ├── footer.html        # Footer component
    ├── index.html         # Home page
    ├── about.html         # About page
    ├── contact.html       # Contact page
    └── post.html          # Individual post page
```

## 🚀 Features
- **Dynamic Blog Posts**: Fetches posts from external API
- **Responsive Design**: Bootstrap-powered responsive layout
- **Individual Post Pages**: Dynamic routing for each blog post
- **Template Inheritance**: Modular HTML structure
- **Static Asset Management**: Organized CSS, JS, and images
- **Navigation System**: Multi-page navigation

## 🔧 Installation & Setup

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the Application**:
```bash
python main.py
```

3. **Access the Blog**:
   - Open browser to `http://127.0.0.1:5000`

## 📊 API Integration
- **Data Source**: `https://api.npoint.io/2b1e1701b179fe512483`
- **Data Format**: JSON array of blog posts
- **Post Structure**: ID, title, subtitle, author, date, body

## 🎨 Key Features Implemented

### Flask Routes
- `/` - Home page with all posts
- `/index.html` - Alternative home route
- `/about.html` - About page
- `/contact.html` - Contact page
- `/post/<int:p_id>` - Individual post pages

### Template Features
- **Template Inheritance**: Header and footer includes
- **Dynamic Content**: Jinja2 templating for posts
- **URL Generation**: Flask's `url_for()` function
- **Bootstrap Integration**: Responsive grid system

### Static File Management
- **CSS**: Custom styling with Bootstrap
- **JavaScript**: Interactive functionality
- **Images**: Background images and assets
- **Favicon**: Site branding

## 🎓 Concepts Learned
- Flask application structure and organization
- Dynamic routing with URL parameters
- Template inheritance and component reuse
- API integration and JSON data handling
- Static file serving in Flask
- Bootstrap framework integration
- Responsive web design principles

## 🔄 How It Works
1. **Data Fetching**: Application fetches blog posts from API on startup
2. **Route Handling**: Flask routes handle different page requests
3. **Template Rendering**: Jinja2 renders HTML with dynamic data
4. **Static Serving**: Flask serves CSS, JS, and image files
5. **Dynamic URLs**: Individual posts accessible via ID-based URLs

## 🌟 Potential Enhancements
- Add database integration for persistent data
- Implement user authentication and comments
- Add search and filtering functionality
- Create admin panel for post management
- Add pagination for large post collections
- Implement contact form functionality

## 📚 Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)

---
**Day 59 of 100 Days of Python** ✅