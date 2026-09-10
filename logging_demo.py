# Simple logging example
import logging

# Set up logging - one line config
logging.basicConfig(level="INFO", format="Message: %(message)s")

def add(x, y):
    result = x + y
    logging.info(f"Added {x} + {y} = {result}")
    return result

def divide(x, y):
    try:
        result = x / y
        logging.info(f"Divided {x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Cannot divide by zero!")
        return None

# Test the functions
print("Testing add:")
add(5, 3)

print("\nTesting divide:")
divide(10, 2)
divide(10, 0)