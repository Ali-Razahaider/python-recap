# Simple logging demo
import logging

logging.basicConfig(level="INFO", format=": %(message)s")

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

print("add(5, 3):", add(5, 3))
print("divide(10, 2):", divide(10, 2))
print("divide(10, 0):", divide(10, 0))