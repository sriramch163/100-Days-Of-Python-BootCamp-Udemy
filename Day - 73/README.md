# Day 73 - Programming Languages Data Analysis

## Project Overview
This project analyzes the popularity of programming languages over time using Stack Overflow data. The analysis explores trends in programming language usage from 2008 to 2020 based on the number of posts tagged with specific programming languages.

## Features
- Data exploration and cleaning of Stack Overflow programming language data
- Time series analysis of programming language popularity
- Data visualization using matplotlib
- Pivot table operations for data reshaping
- Statistical analysis and trend identification

## Technologies Used
- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Jupyter Notebook** - Interactive development environment

## Dataset
The dataset contains Stack Overflow post data with the following columns:
- DATE: Month and year of posts
- TAG: Programming language tag
- POSTS: Number of posts for that language in that month

Programming languages analyzed include:
- Java, Python, JavaScript, C#, PHP, C++, C, R, Ruby, Swift, Go, Assembly, Perl, Delphi

## Key Insights
- JavaScript has the highest total number of posts across all time periods
- Python shows significant growth over the analyzed timeframe
- Different programming languages have varying entry points in the dataset
- Some languages like Go and Swift entered later due to their newer nature

## Installation & Setup

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Launch Jupyter Notebook:
```bash
jupyter notebook
```

3. Open `Programming_Languages_(complete).ipynb`

## Usage
The notebook contains step-by-step analysis including:
1. Data loading and exploration
2. Data cleaning and preprocessing
3. Statistical analysis
4. Data visualization
5. Trend analysis

## Data Analysis Highlights
- **Data Shape**: 1,991 rows × 3 columns
- **Time Range**: July 2008 to July 2020
- **Most Popular Language**: JavaScript (2,056,510 total posts)
- **Fastest Growing**: Python shows consistent upward trend
- **Data Quality**: Clean dataset with no missing values after preprocessing

## Visualizations
The project includes various charts showing:
- Individual language trends over time
- Comparative analysis between languages
- Growth patterns and seasonal variations

## Learning Outcomes
- Data manipulation with Pandas
- Time series data analysis
- Data visualization best practices
- Statistical analysis techniques
- Working with real-world datasets

## Files
- `Programming_Languages_(complete).ipynb` - Main analysis notebook
- `requirements.txt` - Required Python packages
- `README.md` - Project documentation

## Future Enhancements
- Add more recent data (2020-2024)
- Include additional programming languages
- Implement predictive modeling for future trends
- Add interactive visualizations with Plotly
- Correlation analysis between languages

---
*This project is part of the 100 Days of Python coding challenge - Day 73*