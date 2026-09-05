def countdown(n: int):
    """Generator that counts down from n to 1."""
    while n > 0:
        yield n
        n -= 1


def fibonacci_generator(limit: int):
    """Generator that yields Fibonacci numbers up to a limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def infinite_counter():
    """Infinite counter generator."""
    num = 0
    while True:
        yield num
        num += 1


if __name__ == "__main__":
    # countdown generator
    print("Countdown:")
    for num in countdown(5):
        print(num)

    # Fibonacci generator
    print("\nFibonacci (limit 100):")
    for num in fibonacci_generator(100):
        print(num, end=" ")
    print()

    # Infinite counter (first 5 values)
    print("\nInfinite counter (first 5):")
    counter = infinite_counter()
    for _ in range(5):
        print(next(counter), end=" ")
    print()

    # Generator expression
    squares = (x ** 2 for x in range(10))
    print("\nGenerator expression squares:")
    print(list(squares))