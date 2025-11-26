# Day 32 - Automated Birthday Wisher 🎂

## Project Overview
Automated email system that sends personalized birthday wishes using SMTP. Checks daily for birthdays and sends customized emails with random letter templates.

## What I Learned
- **SMTP Protocol**: Sending emails programmatically using smtplib
- **Email Authentication**: Secure login with Gmail SMTP servers
- **DateTime Module**: Working with dates and time comparisons
- **File Template System**: Dynamic content replacement in text files
- **Pandas Data Processing**: Reading and processing CSV birthday data
- **Automation Logic**: Daily birthday checking and notification system

## Key Features
- **Automated Birthday Detection**: Checks current date against birthday database
- **Personalized Messages**: Random letter templates with name replacement
- **SMTP Email Sending**: Secure email delivery via Gmail
- **CSV Data Management**: Stores birthday information in structured format
- **Template Randomization**: 10 different letter templates for variety
- **Secure Authentication**: Email credentials for SMTP connection

## How to Run
1. Update email credentials in `main.py`:
   ```python
   MY_EMAIL = "your_email@gmail.com"
   MY_PASSWD = "your_app_password"
   FROM_NAME = "Your Name"
   ```
2. Run the script:
   ```bash
   python main.py
   ```

## Files & Directory Structure
```
Day - 32/
├── main.py
├── birthdays.csv
└── letter_templates/
    ├── letter-1.txt
    ├── letter-2.txt
    ├── letter-3.txt
    ├── letter-4.txt
    ├── letter-5.txt
    ├── letter-6.txt
    ├── letter-7.txt
    ├── letter-8.txt
    ├── letter-9.txt
    └── letter-10.txt
```

## Technical Implementation
- **Date Matching**: Compares current month/day with birthday records
- **Template Processing**: Replaces `[NAME]` and `[FROM]` placeholders
- **SMTP Connection**: Establishes secure connection with Gmail servers
- **Email Formatting**: Proper subject and body formatting for emails
- **Data Structure**: Dictionary mapping for efficient birthday lookup

## Security Considerations
- Use App Passwords instead of regular Gmail passwords
- Enable 2-factor authentication on Gmail account
- Store credentials securely (consider environment variables)
- Use STARTTLS for encrypted email transmission

## Automation Potential
- Schedule with cron jobs for daily execution
- Deploy on cloud platforms for 24/7 operation
- Add multiple email providers for redundancy
- Implement logging for sent email tracking

---
*Day 32 of 100 Days of Python Challenge*