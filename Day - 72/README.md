# Day 72 - Data Exploration with Pandas: College Major Salary Analysis 📊

## Project Overview
This project explores salary data for different college majors using Pandas for data analysis and manipulation. The analysis focuses on understanding salary trends, identifying high-potential majors, and comparing different academic groups.

## 🎯 Learning Objectives
- Master Pandas DataFrame operations
- Perform data cleaning and exploration
- Analyze salary data across different majors
- Group and aggregate data for insights
- Calculate salary spreads and risk analysis

## 📊 Dataset
- **File**: `salaries_by_college_major.csv`
- **Records**: 50 college majors
- **Columns**: 
  - Undergraduate Major
  - Starting Median Salary
  - Mid-Career Median Salary
  - Mid-Career 10th Percentile Salary
  - Mid-Career 90th Percentile Salary
  - Group (STEM, Business, HASS)

## 🔍 Key Analysis Performed

### Data Exploration
- Dataset shape and structure analysis
- Missing value identification and cleaning
- Column data types examination

### Salary Analysis
- **Highest Starting Salary**: Physician Assistant ($74,300)
- **Highest Mid-Career Salary**: Chemical Engineering ($107,000)
- **Lowest Starting Salary**: Spanish ($34,000)
- **Lowest Mid-Career Salary**: Education ($52,000)

### Risk vs Potential Analysis
- **Salary Spread Calculation**: 90th percentile - 10th percentile
- **Lowest Risk Majors**: Nursing, Physician Assistant, Nutrition
- **Highest Potential Majors**: Economics, Finance, Chemical Engineering
- **Most Volatile**: Economics (highest spread of $159,400)

### Group Comparisons
- **STEM**: Highest average salaries across all metrics
- **Business**: Moderate salaries with good growth potential
- **HASS**: Lower starting salaries but varied outcomes

## 🛠️ Technologies Used
- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **Jupyter Notebook**: Interactive development environment
- **NumPy**: Numerical computations

## 📈 Key Insights
1. **STEM majors** generally offer the highest starting and mid-career salaries
2. **Economics and Finance** show the highest earning potential but with higher risk
3. **Healthcare-related majors** (Nursing, Physician Assistant) offer stability with lower risk
4. **Engineering disciplines** consistently rank high in both starting and mid-career salaries
5. **Liberal arts majors** show lower starting salaries but some have high earning potential

## 🚀 How to Run
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open `Data_Exploration_Pandas_College_Major_(complete).ipynb`

4. Run all cells to see the complete analysis

## 📊 Analysis Highlights
- **Data Cleaning**: Removed invalid entries and handled missing values
- **Statistical Analysis**: Calculated means, medians, and spreads
- **Grouping**: Analyzed data by academic groups (STEM, Business, HASS)
- **Sorting**: Identified top and bottom performers across different metrics
- **Risk Assessment**: Evaluated salary volatility using percentile spreads

## 🎓 Skills Developed
- Pandas DataFrame manipulation
- Data cleaning and preprocessing
- Statistical analysis and aggregation
- Data grouping and pivoting
- Salary trend analysis
- Risk vs reward evaluation

## 📝 Notes
This project demonstrates practical data analysis skills using real-world salary data. The analysis provides valuable insights for students choosing college majors based on earning potential and career stability.

---
**Day 72 of 100 Days of Python** ✅