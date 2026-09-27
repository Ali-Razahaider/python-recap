# Simple logging demo
import logging

# Set up logging: level INFO, format shows the message
logging.basicConfig(level="INFO", format=": %(message)s")

# Add two numbers and log the result
def add(x, y):
    result = x + y
    logging.info(f"Added {x} + {y} = {result}")
    return result

# Divide two numbers, log result, handle division by zero
def divide(x, y):
    try:
        result = x / y
        logging.info(f"Divided {x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Cannot divide by zero!")
        return None

# Test the functions
print("add(5, 3):", add(5, 3))
print("divide(10, 2):", divide(10, 2))
print("divide(10, 0):", divide(10, 0))