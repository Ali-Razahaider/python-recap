# =============================================================================
# PART 3: INTERMEDIATE CONCEPTS
# =============================================================================

# --- IMPORTS (80/20 standard library toolkit) ---
import os                          # environment variables & OS paths
import sys                         # argv, path, exit
import json                        # json.loads() / json.dumps()
import re                          # regular expressions
from datetime import datetime, timedelta, timezone
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from functools import lru_cache, partial
from pathlib import Path           # modern file paths
from typing import Optional, Union, Callable, Any

# --- DATACLASSES (Modern Python Data Containers) ---
@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True
    roles: list[str] = field(default_factory=list)  # dynamic default via field()

user1 = User(id=1, name="Alice", email="alice@example.com", roles=["admin"])
print(user1)  # Auto-generated string representation: User(id=1, name='Alice', ...)

# --- JSON HANDLING & ENVIRONMENT VARIABLES ---
# Environment variables with fallback defaults
api_key = os.getenv("API_KEY", "default_secret_key")
debug_mode = os.getenv("DEBUG", "False").lower() in ("true", "1")

# JSON Serialization (dict -> string) & Deserialization (string -> dict)
data_dict = {"name": "Bob", "active": True, "count": 42}
json_string = json.dumps(data_dict, indent=2)    # formatted JSON string
parsed_data = json.loads(json_string)            # python dict

# --- DATETIME & TIMEZONES ---
now_utc = datetime.now(timezone.utc)
formatted_now = now_utc.strftime("%Y-%m-%d %H:%M:%S %Z")  # "2026-09-01 18:25:00 UTC"
future_date = now_utc + timedelta(days=7, hours=3)        # date math

iso_str = "2026-09-01T12:00:00+00:00"
parsed_dt = datetime.fromisoformat(iso_str)                # parse ISO string

# --- REGULAR EXPRESSIONS (re) ---
sample_text = "Contact us at support@example.com or info@domain.org"
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", sample_text)  # find all pattern matches
clean_text = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "[REDACTED]", sample_text) # replacement

# --- LIST & DICT COMPREHENSIONS (advanced) ---
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in nested for num in row]  # [1, 2, 3, 4, 5, 6]

keys = ["a", "b", "c"]
values = [1, 2, 3]
mapping = {k: v for k, v in zip(keys, values)}  # {'a': 1, 'b': 2, 'c': 3}

# --- COMMON PATTERNS ---
# Counter — count occurrences instantly
words_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words_list)
print(word_counts.most_common(2))  # [('apple', 3), ('banana', 2)]

# defaultdict — auto-creates missing keys with a default
grouped = defaultdict(list)
for word in words_list:
    grouped[word[0]].append(word)

# Pathlib — modern path manipulation
p = Path(".")
abs_path = p.resolve()             # full absolute path
data_file = p / "data" / "file.json" # path joining with '/' operator

# Walrus operator (:=) — assign and use in one expression (Python 3.8+)
data = [1, 2, 3, 4, 5, 6]
results = [y for x in data if (y := x ** 2) > 10]  # [16, 25, 36]

# --- CLASSES ---
class Dog:
    species = "Canis familiaris"   # class variable — shared across all instances

    def __init__(self, name: str, age: int): # constructor
        self.name = name           # instance variable
        self.age = age

    def bark(self) -> str:         # instance method
        return f"{self.name} says Woof!"

    def __str__(self) -> str:      # what print()/str() returns
        return f"Dog(name={self.name}, age={self.age})"

    def __repr__(self) -> str:     # dev-facing representation
        return self.__str__()

buddy = Dog("Buddy", 5)
print(buddy.bark())

# --- GENERATORS & MEMOIZATION ---
# yield instead of return — produces values lazily (saves memory)
def countdown(n: int):
    while n > 0:
        yield n                    # pauses function, returns value
        n -= 1                     # resumes here on next call

# Generator expression — like list comp but with (), lazy evaluation
gen = (x ** 2 for x in range(1_000_000))  # nothing stored in memory upfront
print(next(gen))   # 0
print(next(gen))   # 1

# Memoization with @lru_cache (caches expensive function calls)
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# --- DECORATORS ---
# Wraps a function to add behavior (logging, timing, auth, etc.)
def timer(func: Callable) -> Callable:
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer                              # @syntax applies the decorator
def slow_function():
    import time; time.sleep(0.1)

# --- GOTCHAS & BEST PRACTICES ---
# 1. Mutable default args are SHARED between calls
def append_to(item, target=None):  # GOOD — create new list each call
    if target is None:
        target = []
    target.append(item)
    return target

# 2. Use 'is' for None/True/False, '==' for values
x_val = None
if x_val is None: print("correct")

# 3. Shallow vs deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()           # first level copied, inner lists still shared
deep = copy.deepcopy(original)      # fully independent at all levels

