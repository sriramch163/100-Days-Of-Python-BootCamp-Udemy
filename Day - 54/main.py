from flask import Flask
import time
from functools import wraps

app = Flask(__name__)

# Decorator to calculate execution time
def speed_calc_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execution time: {end_time - start_time}s")
        return result
    return wrapper


@app.route("/")
@speed_calc_decorator
def home():
    return "Welcome to Day-54 Flask Decorator Mini Project"


@app.route("/fast")
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
    return "Fast function executed"


@app.route("/slow")
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
    return "Slow function executed"


if __name__ == "__main__":
    app.run(debug=True)
