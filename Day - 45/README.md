# Day 45 - Web Scraping with Beautiful Soup 🕷️

## Project Overview
Web scraping application that extracts the top 100 movies list from Empire Online website using Beautiful Soup. Demonstrates HTML parsing, data extraction, and file output with proper encoding.

## What I Learned
- **Web Scraping Fundamentals**: Extracting data from websites programmatically
- **Beautiful Soup Library**: HTML/XML parsing and navigation
- **HTTP Requests**: Fetching web page content using requests library
- **HTML Parsing**: Finding specific elements using tags and CSS classes
- **List Comprehensions**: Efficient data extraction from HTML elements
- **File I/O with Encoding**: Writing scraped data to files with UTF-8 encoding
- **Data Manipulation**: Reversing lists to correct ordering

## Key Features
- **Automated Data Extraction**: Scrapes top 100 movies from Empire Online
- **HTML Element Selection**: Targets specific h3 tags with "title" class
- **Text Processing**: Extracts clean text content from HTML elements
- **Data Ordering**: Reverses list to display movies in correct ranking order
- **File Output**: Saves results to text file with proper encoding
- **Error Prevention**: UTF-8 encoding handles special characters

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the scraper:
   ```bash
   python main.py
   ```
3. Check the generated `movies.txt` file for results

## Files & Directory Structure
```
Day - 45/
├── main.py
├── requirements.txt
├── movies.txt (generated)
└── README.md
```

## Web Scraping Process

### 1. HTTP Request
```python
response = requests.get(URL)
website_html = response.text
```

### 2. HTML Parsing
```python
soup = BeautifulSoup(website_html, "html.parser")
```

### 3. Element Selection
```python
all_movies = soup.find_all(name="h3", class_="title")
```

### 4. Data Extraction
```python
movie_titles = [movie.getText() for movie in all_movies]
```

### 5. Data Processing
```python
movies = movie_titles[::-1]  # Reverse order
```

## Beautiful Soup Methods Used
- **BeautifulSoup()**: Create parser object from HTML content
- **find_all()**: Locate all elements matching criteria
- **getText()**: Extract text content from HTML elements

## Technical Implementation
- **CSS Class Selection**: Targeting elements by class attribute
- **List Slicing**: Using `[::-1]` for list reversal
- **File Encoding**: UTF-8 encoding for international characters
- **List Comprehension**: Efficient text extraction from elements

## Data Output Format
```
1) The Godfather
2) The Shawshank Redemption
3) Schindler's List
...
100) Movie Title
```

## Web Scraping Best Practices
- **Respectful Scraping**: Single request to avoid server overload
- **Error Handling**: Proper encoding to prevent character issues
- **Data Validation**: Processing scraped data before output
- **Legal Compliance**: Scraping publicly available content

## Practical Applications
- **Data Collection**: Gathering information from websites
- **Market Research**: Collecting product/price information
- **Content Aggregation**: Building databases from web sources
- **Monitoring**: Tracking changes on websites
- **Research**: Academic data collection

## Libraries Used
- **requests**: HTTP library for web requests
- **beautifulsoup4**: HTML/XML parsing library

---
*Day 45 of 100 Days of Python Challenge - Introduction to Web Scraping*