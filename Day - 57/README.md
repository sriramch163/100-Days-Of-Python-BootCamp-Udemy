# Day 57 - Flask Blog Application

## 🎯 Project Overview
A dynamic blog application built with Flask that fetches blog posts from an external API and displays them with a clean, responsive design.

## 🚀 Features
- **Dynamic Content**: Fetches blog posts from external API
- **Flask Routing**: Multiple routes for home and individual posts
- **Template Engine**: Jinja2 templating with dynamic data
- **OOP Design**: Post class for data modeling
- **Responsive UI**: Clean CSS styling with Google Fonts
- **URL Parameters**: Dynamic post viewing with URL routing

## 🛠️ Technologies Used
- **Backend**: Flask (Python web framework)
- **HTTP Client**: Requests library for API calls
- **Frontend**: HTML5, CSS3, Jinja2 templates
- **API**: External JSON API (npoint.io)
- **Fonts**: Google Fonts (Raleway)

## 📁 Project Structure
```
Day - 57/
├── main.py               # Main Flask application
├── post.py              # Post class model
├── requirements.txt     # Python dependencies
├── templates/
│   ├── index.html      # Blog home page
│   └── post.html       # Individual post page
└── static/
    └── css/
        └── styles.css  # Custom styling
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

3. **Access the Blog**:
   - Home page: `http://127.0.0.1:5000`
   - Individual posts: `http://127.0.0.1:5000/post/<post_id>`

## 💡 Key Concepts Learned
- **Flask Routing**: URL routing with parameters
- **API Integration**: HTTP requests with external APIs
- **Template Rendering**: Dynamic content with Jinja2
- **Object-Oriented Design**: Data modeling with classes
- **URL Building**: Dynamic URL generation with url_for()
- **Static Files**: CSS and asset management

## 🌐 API Integration
- **Data Source**: https://api.npoint.io/5abcca6f4e39b4955965
- **Data Format**: JSON array of blog posts
- **Fields**: id, title, subtitle, body

## 🎨 Design Features
- Clean, modern blog layout
- Card-based post display
- Responsive design
- Professional color scheme
- Google Fonts integration

## 📝 Code Highlights
- **Post Class**: Object-oriented data modeling
- **Dynamic Routing**: URL parameters for post viewing
- **Template Inheritance**: Reusable HTML structure
- **API Data Processing**: JSON to Python object conversion

## 🔄 Application Flow
1. Fetch blog posts from external API
2. Convert JSON data to Post objects
3. Render home page with all posts
4. Handle individual post requests via URL routing
5. Display specific post content dynamically

Perfect foundation for building more complex blog applications with user authentication, CRUD operations, and database integration!