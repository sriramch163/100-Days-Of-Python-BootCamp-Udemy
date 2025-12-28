# Day 60 - Flask Contact Form with Email Integration

## 📋 Project Overview
A Flask web application that implements a contact form with email functionality. Users can submit contact information through a web form, and the application sends the data via email using SMTP.

## 🎯 Learning Objectives
- Advanced Flask form handling with POST requests
- Email integration using Python's smtplib
- Template rendering with conditional logic
- Form data processing and validation
- SMTP configuration and email automation

## 🛠️ Technologies Used
- **Flask**: Web framework for Python
- **smtplib**: Built-in Python library for sending emails
- **requests**: HTTP library for API calls
- **HTML/CSS**: Frontend templates
- **Bootstrap**: CSS framework for styling

## 📁 Project Structure
```
Day - 60/
├── main.py              # Main Flask application
├── templates/
│   ├── contact.html     # Contact form template
│   └── index.html       # Home page template
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## 🚀 Features
- **Contact Form**: Multi-field form with name, email, phone, and message
- **Email Integration**: Automatic email sending via SMTP
- **Form Validation**: Required field validation
- **Success Feedback**: Dynamic template rendering based on form submission
- **API Integration**: Fetches blog posts from external API

## 💻 How to Run

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Configure Email Settings**:
   - Update `OWN_EMAIL` and `OWN_PASSWORD` in main.py
   - Use app-specific password for Gmail

3. **Run the Application**:
```bash
python main.py
```

4. **Access the Application**:
   - Open browser and go to `http://localhost:5000`
   - Navigate to `/contact` to test the form

## 🔧 Configuration
- **SMTP Server**: Gmail (smtp.gmail.com)
- **Port**: 587 (TLS)
- **Authentication**: Email and app password required

## 📝 Key Concepts Learned
- **Flask POST Requests**: Handling form submissions
- **Email Automation**: SMTP configuration and message formatting
- **Template Logic**: Conditional rendering with Jinja2
- **Form Data Processing**: Extracting and validating user input
- **Error Handling**: Managing email sending failures

## 🔒 Security Notes
- Store email credentials securely (use environment variables)
- Implement proper form validation
- Consider rate limiting for form submissions
- Use app-specific passwords for email accounts

## 🎨 Styling
- Bootstrap CSS framework
- Responsive design
- Clean contact form layout
- Success/error message display

## 📈 Potential Enhancements
- Add form validation on frontend
- Implement CAPTCHA for spam protection
- Store form submissions in database
- Add email templates for better formatting
- Implement file upload functionality

---
**Day 60 of 100 Days of Python** 🐍