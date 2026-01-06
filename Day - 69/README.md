# Day 69 - Flask Blog with User Authentication & Comments

## 🎯 Project Overview
A complete Flask blog application featuring user authentication, admin controls, and a commenting system. This project demonstrates advanced Flask concepts including user sessions, database relationships, and role-based access control.

## ✨ Features
- **User Authentication**: Registration, login, and logout functionality
- **Admin Controls**: Only admin users can create, edit, and delete posts
- **Commenting System**: Authenticated users can comment on blog posts
- **Rich Text Editor**: CKEditor integration for post creation and comments
- **Profile Images**: Gravatar integration for user avatars
- **Responsive Design**: Bootstrap-powered responsive UI
- **Database Relationships**: Complex SQLAlchemy relationships between users, posts, and comments

## 🛠️ Technologies Used
- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and validation
- **Flask-CKEditor**: Rich text editor
- **Flask-Bootstrap**: UI framework integration
- **Flask-Gravatar**: Profile image service
- **Werkzeug**: Password hashing
- **SQLite**: Database

## 📁 Project Structure
```
Day - 69/
├── main.py                 # Main Flask application
├── forms.py               # WTForms definitions
├── requirements.txt       # Project dependencies
├── instance/
│   └── posts.db          # SQLite database
├── static/
│   ├── assets/           # Images and favicon
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
└── templates/           # HTML templates
    ├── index.html       # Home page
    ├── post.html        # Individual post view
    ├── make-post.html   # Create/edit post form
    ├── login.html       # Login form
    ├── register.html    # Registration form
    ├── about.html       # About page
    ├── contact.html     # Contact page
    ├── header.html      # Navigation header
    └── footer.html      # Page footer
```

## 🚀 How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser and navigate to `http://localhost:5001`

## 👤 User Roles
- **Admin (User ID: 1)**: Can create, edit, and delete posts
- **Regular Users**: Can register, login, and comment on posts
- **Visitors**: Can view posts but cannot comment

## 🔑 Key Learning Concepts
- **Flask-Login**: User session management and authentication
- **Password Security**: Hashing and salting with Werkzeug
- **Database Relationships**: One-to-many relationships between users, posts, and comments
- **Decorators**: Custom admin-only decorator for route protection
- **Form Validation**: Advanced form handling with Flask-WTF
- **Rich Text Editing**: CKEditor integration for content creation
- **Flash Messages**: User feedback and error handling
- **Template Inheritance**: Modular HTML template structure

## 🎨 UI Components
- Responsive navigation with user authentication status
- Rich text editor for post creation and comments
- User profile images via Gravatar
- Bootstrap-styled forms and layouts
- Flash message notifications

## 🔒 Security Features
- Password hashing with PBKDF2-SHA256
- CSRF protection on forms
- Admin-only route protection
- User session management
- SQL injection prevention through SQLAlchemy ORM

## 📝 Database Schema
- **Users**: id, email, password, name
- **BlogPosts**: id, title, subtitle, date, body, img_url, author_id
- **Comments**: id, text, author_id, post_id

## 🎯 Next Steps
This project provides a solid foundation for:
- Adding email verification
- Implementing password reset functionality
- Adding post categories and tags
- Implementing search functionality
- Adding file upload capabilities
- Deploying to production servers

---
*Day 69 of 100 Days of Python - Advanced Flask Web Development*