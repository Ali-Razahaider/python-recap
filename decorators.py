def debug(func):
    """Decorator that prints function call info."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


def timer(func):
    """Decorator that measures and prints execution time."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def repeat(times: int):
    """Decorator factory that repeats function execution n times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@debug
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@timer
def slow_function() -> None:
    """Function that sleeps briefly."""
    import time
    time.sleep(0.1)


@repeat(3)
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print("Debug decorator:")
    result = add(3, 5)
    print(f"Result: {result}\n")

    print("Timer decorator:")
    slow_function()

    print("\nRepeat decorator:")
    msg = greet("Alice")
    print(f"Returned: {msg}")