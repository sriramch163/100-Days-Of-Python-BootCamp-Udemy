# Day 54 - Flask Web Development & Python Decorators

## Project Overview
A Flask web application demonstrating Python decorators for performance monitoring. This project combines web development with advanced Python concepts to create a speed calculation decorator that measures function execution time.

## Features
- **Flask Web Framework**: Basic web application with multiple routes
- **Custom Decorator**: Speed calculation decorator to measure execution time
- **Performance Monitoring**: Real-time function execution timing
- **Multiple Endpoints**: Different routes with varying computational loads

## Routes
- `/` - Home page with welcome message
- `/fast` - Fast function with light computational load (1M iterations)
- `/slow` - Slow function with heavy computational load (10M iterations)

## Key Concepts Learned
- **Flask Framework**: Web application development basics
- **Python Decorators**: Advanced decorator patterns with `@wraps`
- **Performance Monitoring**: Execution time measurement
- **Function Wrapping**: Preserving function metadata
- **Web Routing**: URL routing and endpoint handling

## Installation & Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open browser and navigate to:
- `http://127.0.0.1:5000/` - Home page
- `http://127.0.0.1:5000/fast` - Fast function
- `http://127.0.0.1:5000/slow` - Slow function

## Technical Implementation

### Speed Calculator Decorator
```python
def speed_calc_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execution time: {end_time - start_time}s")
        return result
    return wrapper
```

## Dependencies
- Flask 2.3.3
- Python 3.x built-in modules (time, functools)

## Learning Outcomes
- Understanding Flask web framework fundamentals
- Mastering Python decorator patterns
- Implementing performance monitoring tools
- Combining web development with advanced Python concepts
- Function metadata preservation with `@wraps`

## Next Steps
- Add more complex decorators (authentication, logging)
- Implement database integration
- Create more sophisticated web interfaces
- Add error handling and validation

---
*Day 54 of 100 Days of Python Challenge*