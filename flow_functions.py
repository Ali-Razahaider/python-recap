# =============================================================================
# PART 2: CONTROL FLOW, FUNCTIONS & FILE I/O
# =============================================================================

# --- CONTROL FLOW ---
# Indentation (4 spaces) defines blocks — no braces
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"

# Ternary — one-liner if/else
age = 30
status = "adult" if age >= 18 else "minor"

# Truthiness: Falsy = False, None, 0, 0.0, "", [], {}, set(). Everything else is truthy.
if []:     print("won't print")
if [1, 2]: print("will print")

# Structural Pattern Matching (Python 3.10+) — match / case
status_code = 404
match status_code:
    case 200:
        message = "OK"
    case 400 | 404:
        message = "Client Error"
    case 500:
        message = "Server Error"
    case _:
        message = "Unknown Status"  # wildcard default case

# --- LOOPS ---
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

# enumerate — loop with index + value
for index, value in enumerate(["a", "b", "c"]):
    print(f"{index}: {value}")

# zip — loop over multiple sequences in parallel
names = ["Alice", "Bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# while
count = 0
while count < 3:
    count += 1

# break exits loop, continue skips to next iteration
for i in range(10):
    if i == 3: continue
    if i == 7: break
    print(i)           # 0, 1, 2, 4, 5, 6

# for...else — else runs only if loop finished without break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0: break
    else:
        print(f"{n} is prime")

# --- FUNCTIONS & TYPE HINTS ---
# Basic function with default parameter & type annotations
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# Keyword-only arguments (forces named parameters at call site after '*')
def create_user(username: str, *, is_admin: bool = False) -> dict:
    return {"username": username, "is_admin": is_admin}

# Correct usage: create_user("alice", is_admin=True)

# *args = extra positional args (tuple), **kwargs = extra keyword args (dict)
def flexible(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible(1, 2, 3, x=10, y=20)

# Lambda — anonymous one-liner functions
square = lambda x: x ** 2

# map applies function to every item, filter keeps items where func returns True
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))       # [2, 4, 6, 8, 10]
odds = list(filter(lambda x: x % 2 != 0, nums))   # [1, 3, 5]

# --- ERROR HANDLING ---
# Custom Exception class
class ValidationError(Exception):
    """Raised when validation fails."""
    pass

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Can't divide by zero!")
except (TypeError, ValueError) as e:
    print(f"Type or Value error: {e}")
else:
    # Runs ONLY if no exceptions were raised in try block
    print(f"Calculation succeeded: {result}")
finally:
    # ALWAYS runs regardless of errors
    print("Cleanup complete.")

# raise — enforce preconditions with built-in or custom exceptions
def set_age(age: int) -> int:
    if not isinstance(age, int) or age < 0:
        raise ValidationError("Age must be a non-negative integer")
    return age

# --- FILE I/O & CONTEXT MANAGERS ---
# Always use 'with' — auto-closes file even if error occurs
with open("output.txt", "w") as f:     # "w" = write (overwrites), "a" = append
    f.write("Hello, file!\n")

with open("output.txt", "r") as f:
    content = f.read()        # entire file as one string

with open("output.txt", "r") as f:
    for line in f:            # line by line — memory efficient
        print(line.strip())

import os
if os.path.exists("output.txt"):
    os.remove("output.txt")

# Custom Context Manager via contextlib (80/20 standard library helper)
from contextlib import contextmanager

@contextmanager
def temporary_status(new_status):
    print(f"Setting status to: {new_status}")
    yield new_status
    print("Resetting status back to normal")

with temporary_status("MAINTENANCE") as status:
    print(f"Performing task under status: {status}")

# --- BUILT-IN FUNCTIONS ---
print(list(range(5)))               # [0, 1, 2, 3, 4]
print(any([False, True]))           # True if ANY element is truthy
print(all([True, True]))            # True if ALL elements are truthy
print(sorted([3, 1, 2]))           # [1, 2, 3] — new sorted list
print(sorted(["b", "a"], key=str.lower))  # custom sort key

# Type checking — isinstance is preferred over type()
print(isinstance(42, int))          # True
print(isinstance("hi", (int, str))) # True — check multiple types

# Chained comparisons
x_val = 5
print(1 < x_val < 10)              # True — same as 1 < x_val and x_val < 10

