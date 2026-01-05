# Day 68 - Flask Authentication & User Management 🔐

## Project Overview
A complete Flask web application demonstrating user authentication, registration, login/logout functionality, and protected routes with file downloads.

## 🎯 Learning Objectives
- **Flask-Login Integration**: User session management and authentication
- **Password Security**: Hashing and salting with Werkzeug
- **SQLAlchemy ORM**: Advanced database operations with Flask-SQLAlchemy
- **Protected Routes**: Login-required decorators and access control
- **User Experience**: Flash messages and form validation
- **File Serving**: Secure file downloads for authenticated users

## 🚀 Features
- ✅ User Registration with email validation
- ✅ Secure Password Hashing (PBKDF2 + SHA256)
- ✅ User Login/Logout System
- ✅ Session Management with Flask-Login
- ✅ Protected Routes (@login_required)
- ✅ Flash Messages for User Feedback
- ✅ SQLite Database with SQLAlchemy ORM
- ✅ File Download for Authenticated Users
- ✅ Responsive Bootstrap UI

## 🛠️ Technologies Used
- **Flask 3.0.0**: Web framework
- **Flask-Login 0.6.3**: User session management
- **Flask-SQLAlchemy 3.1.1**: Database ORM
- **SQLAlchemy 2.0.25**: Database toolkit
- **Werkzeug 3.0.0**: Password hashing and security
- **Bootstrap**: Frontend styling
- **SQLite**: Database storage

## 📁 Project Structure
```
Day - 68/
├── instance/
│   └── users.db              # SQLite database
├── static/
│   ├── css/
│   │   └── styles.css        # Custom styles
│   └── files/
│       └── cheat_sheet.pdf   # Protected download file
├── templates/
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   ├── login.html           # Login form
│   ├── register.html        # Registration form
│   └── secrets.html         # Protected content
├── main.py                  # Main Flask application
├── requirements.txt         # Dependencies
└── README.md               # This file
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
   - Open browser to `http://localhost:5000`

## 🎮 How to Use

### Registration Process
1. Navigate to the home page
2. Click "Register" button
3. Fill in your name, email, and password
4. Submit the form to create your account
5. You'll be automatically logged in and redirected to secrets page

### Login Process
1. Click "Login" button from home page
2. Enter your registered email and password
3. Access the protected content upon successful login

### Protected Features
- **Secrets Page**: Only accessible to logged-in users
- **File Download**: Download the cheat sheet PDF (login required)
- **Automatic Redirects**: Seamless navigation between protected/public areas

## 🔒 Security Features

### Password Security
- **PBKDF2 Hashing**: Industry-standard password hashing
- **SHA256 Algorithm**: Cryptographic hash function
- **Salt Length**: 8-character random salt for each password
- **No Plain Text**: Passwords never stored in readable format

### Session Management
- **Flask-Login**: Secure user session handling
- **User Loader**: Automatic user retrieval from database
- **Login Required**: Decorator-based route protection
- **Automatic Logout**: Session cleanup on logout

### Database Security
- **SQLAlchemy ORM**: SQL injection prevention
- **Unique Constraints**: Email uniqueness enforcement
- **Proper Validation**: Input sanitization and validation

## 🎨 User Interface

### Pages & Features
- **Home Page**: Welcome screen with login/register options
- **Registration**: Clean form with validation feedback
- **Login**: Simple authentication interface
- **Secrets**: Protected content area with personalized greeting
- **Flash Messages**: User-friendly error and success notifications

### Responsive Design
- Bootstrap-based responsive layout
- Mobile-friendly interface
- Clean, professional styling

## 🧪 Key Code Concepts

### User Model with SQLAlchemy 2.0
```python
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
```

### Password Hashing
```python
hash_and_salted_password = generate_password_hash(
    password,
    method='pbkdf2:sha256',
    salt_length=8
)
```

### Protected Routes
```python
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)
```

## 🔍 Learning Outcomes

### Authentication Concepts
- User registration and login workflows
- Password security best practices
- Session management and user state
- Protected route implementation

### Flask Advanced Features
- Flask-Login integration and configuration
- SQLAlchemy 2.0 modern syntax and type hints
- Flash messaging system
- File serving with security considerations

### Security Best Practices
- Never store plain text passwords
- Implement proper user validation
- Use secure session management
- Validate user input and prevent common attacks

## 🚀 Potential Enhancements
- Email verification for registration
- Password reset functionality
- User profile management
- Role-based access control
- OAuth integration (Google, GitHub)
- Password strength requirements
- Account lockout after failed attempts

## 📚 Resources & References
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [Werkzeug Security](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security)
- [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/3.0.x/security/)

---

**Day 68 Complete!** ✅  
*Mastered Flask authentication, user management, and security best practices.*