# Day 53 - Data Entry Job Automation

## Project Overview
This project automates the process of collecting rental property data from a real estate website and filling out Google Forms with the scraped information. It demonstrates advanced web scraping and browser automation techniques.

## What I Learned
- **Web Scraping with Beautiful Soup**: Extracting structured data from HTML
- **CSS Selectors**: Targeting specific elements for data extraction
- **Data Cleaning**: Processing and formatting scraped text data
- **Selenium WebDriver**: Automating browser interactions
- **Form Automation**: Filling out web forms programmatically
- **XPath Selection**: Locating form elements precisely

## Technologies Used
- **Beautiful Soup 4**: HTML parsing and web scraping
- **Requests**: HTTP requests for web page retrieval
- **Selenium**: Browser automation and form filling
- **Chrome WebDriver**: Browser control for automation

## Project Features

### Part 1: Web Scraping
- Scrapes rental property listings from Zillow-Clone website
- Extracts property links, addresses, and prices
- Cleans and formats the scraped data
- Handles data inconsistencies and formatting issues

### Part 2: Form Automation
- Automates Google Form submission
- Fills multiple form entries with scraped data
- Uses XPath selectors for precise element targeting
- Implements delays for reliable form interaction

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Chrome WebDriver**:
   - Ensure Chrome browser is installed
   - ChromeDriver will be managed automatically by Selenium 4.x

3. **Configure Google Form**:
   - Create a Google Form with fields for address, price, and link
   - Replace `YOUR_GOOGLE_FORM_LINK_HERE` with your actual form URL
   - Update XPath selectors if your form structure differs

4. **Run the Script**:
   ```bash
   python main.py
   ```

## Code Structure

### Web Scraping Section
```python
# Scrapes property data using Beautiful Soup
- Property links extraction
- Address data cleaning
- Price formatting and normalization
```

### Browser Automation Section
```python
# Automates form filling using Selenium
- Chrome browser initialization
- Form field location and interaction
- Batch data submission
```

## Key Concepts Demonstrated

1. **CSS Selectors**: `.StyledPropertyCardDataWrapper a` for targeting specific elements
2. **List Comprehensions**: Efficient data processing and cleaning
3. **String Manipulation**: Removing unwanted characters and formatting
4. **XPath Usage**: Precise element location in complex web forms
5. **Browser Options**: Configuring Chrome for automation tasks

## Challenges Overcome
- **Data Inconsistency**: Handled varying price formats and address structures
- **Element Location**: Used robust XPath selectors for form fields
- **Timing Issues**: Implemented delays for reliable form interaction
- **Data Cleaning**: Processed raw scraped data into usable format

## Real-World Applications
- **Data Entry Automation**: Reducing manual data entry tasks
- **Real Estate Analysis**: Collecting market data for analysis
- **Form Processing**: Automating repetitive form submissions
- **Web Scraping**: Extracting structured data from websites

## Notes
- Replace the Google Form URL with your own form
- Update XPath selectors based on your form structure
- Ensure stable internet connection for reliable scraping
- Consider rate limiting for respectful web scraping

## Dependencies
See `requirements.txt` for exact package versions used in this project.

---
**Day 53 of 100 Days of Python** 🐍
*Advanced Web Scraping & Browser Automation*