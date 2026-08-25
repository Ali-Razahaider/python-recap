# PYTHON BASICS - The 20% Used 80% of the Time

# --- VARIABLES & ASSIGNMENT ---
name = "Alice"           # str, no type declaration needed
age = 30                 # int
height = 5.9             # float
is_active = True         # bool
nothing = None           # Python's "null"

x, y, z = 1, 2, 3       # unpack values in one line
a = b = c = 0            # same value to multiple variables
population = 1_000_000   # underscores ignored, just for readability

# --- STRINGS ---
greeting = "Hello"
name = 'World'           # single or double quotes, same thing

# f-strings: embed expressions inside strings
full = f"{greeting}, {name}!"        # "Hello, World!"
calculated = f"2 + 2 = {2 + 2}"     # "2 + 2 = 4"

# String methods — all return NEW strings, original unchanged
text = "  Hello, Python!  "
print(text.strip())                   # "Hello, Python!" — remove leading/trailing whitespace
print(text.strip().lower())           # "hello, python!"
print(text.strip().upper())           # "HELLO, PYTHON!"
print(text.strip().replace("Python", "World"))  # "Hello, World!"
print(text.strip().split(","))        # split into list by delimiter

# Slicing: [start:stop:step] — works on all sequences
word = "Python"
print(word[0:3])        # "Pyt" — index 0 up to (not including) 3
print(word[-1])          # "n" — negative index counts from end
print(word[::-1])        # "nohtyP" — step -1 reverses the string

# --- NUMBERS & MATH ---
print(10 / 3)            # 3.3333 — true division, always returns float
print(10 // 3)           # 3 — floor division
print(10 % 3)            # 1 — modulo (remainder)
print(2 ** 10)           # 1024 — exponentiation

print(abs(-5))           # 5
print(min(3, 1, 4))      # 1
print(max(3, 1, 4))      # 4
print(sum([1, 2, 3]))    # 6
print(round(3.14159, 2)) # 3.14

# Type conversion — Python won't auto-convert
num_str = "42"
num_int = int(num_str)         # str -> int
num_float = float(num_str)     # str -> float
back_to_str = str(num_int)     # int -> str

# --- LISTS ---
# Ordered, mutable sequences — the workhorse of Python


fruits = ["apple", "banana", "cherry"]
fruits.append("date")          # add to end
fruits.insert(1, "blueberry")  # insert at index
fruits.remove("banana")        # remove by value
popped = fruits.pop()          # remove & return last
fruits.sort()                  # sort in place

# List comprehension — [expression for item in iterable if condition]
squares = [x ** 2 for x in range(10)]                    # [0, 1, 4, 9, ..., 81]
evens = [x for x in range(20) if x % 2 == 0]             # filter: only even
upper_words = [w.upper() for w in ["hello", "world"]]     # transform each

# Extended unpacking: * collects "the rest" into a list
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5

# Nested lists (2D)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])      # row 1, column 2

# --- TUPLES ---
# Like lists but IMMUTABLE. Can be dict keys, lists cannot.
point = (3, 4)
x, y = point             # unpacking — common for multiple return values
locations = {(0, 0): "origin"}  # tuples as dict keys

single = (42,)           # trailing comma makes it a tuple
not_a_tuple = (42)       # this is just int 42

# --- DICTIONARIES ---
# Key-value pairs, O(1) average lookup
person = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}

print(person["name"])            # KeyError if key missing
print(person.get("salary", 0))   # .get() returns default if key missing (safer)
person["email"] = "a@b.com"      # add/update
del person["age"]                # delete
if "name" in person:             # check key exists
    print("name is present")

print(person.keys())             # dict_keys([...])
print(person.items())            # dict_items([('name', 'Alice'), ...])

# Dict comprehension
squares_dict = {x: x**2 for x in range(6)}

# Merging dicts 
defaults = {"color": "blue", "size": 10}

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
status = "adult" if age >= 18 else "minor"

# Truthiness: Falsy = False, None, 0, 0.0, "", [], {}, set(). Everything else is truthy.
if []:     print("won't print")
if [1, 2]: print("will print")

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





# --- FUNCTIONS ---
def add(a, b):
    return a + b

def greet(name, greeting="Hello"):       # default parameter
    return f"{greeting}, {name}!"

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
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
except (TypeError, ValueError) as e:
    print(f"Type or Value error: {e}")
except Exception as e:
    print(f"Something else: {e}")     # catch-all, use sparingly
finally:
    print("This ALWAYS runs")

# raise — enforce preconditions
def set_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer")
    return age

# --- FILE I/O ---
# Always use 'with' — auto-closes file even if error occurs
with open("output.txt", "w") as f:     # "w" = write (overwrites), "a" = append
    f.write("Hello, file!\n")

with open("output.txt", "r") as f:
    content = f.read()        # entire file as one string

with open("output.txt", "r") as f:
    for line in f:            # line by line — memory efficient
        print(line.strip())

import os
os.remove("output.txt")

# --- LIST COMPREHENSIONS (advanced) ---
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in nested for num in row]  # [1, 2, 3, 4, 5, 6]

keys = ["a", "b", "c"]
values = [1, 2, 3]
mapping = {k: v for k, v in zip(keys, values)}  # {'a': 1, 'b': 2, 'c': 3}

# --- IMPORTS ---
import os                          # file paths, dirs, env vars
import sys                         # argv, path, exit
import json                        # json.loads() / json.dumps()
import re                          # regular expressions
from datetime import datetime, timedelta
from collections import Counter, defaultdict
from pathlib import Path           # modern file paths

# --- COMMON PATTERNS ---
# Counter — count occurrences instantly
words_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words_list)
print(word_counts.most_common(2))  # [('apple', 3), ('banana', 2)]

# defaultdict — auto-creates missing keys with a default
grouped = defaultdict(list)
for word in words_list:
    grouped[word[0]].append(word)

# Pathlib
p = Path(".")
print(p.resolve())                 # full absolute path

# Walrus operator (:=) — assign and use in one expression (Python 3.8+)
data = [1, 2, 3, 4, 5, 6]
results = [y for x in data if (y := x ** 2) > 10]  # [16, 25, 36]

# --- CLASSES ---
class Dog:
    species = "Canis familiaris"   # class variable — shared across all instances

    def __init__(self, name, age): # constructor, self = the instance being created
        self.name = name           # instance variable — unique per instance
        self.age = age

    def bark(self):                # instance method, self is always first param
        return f"{self.name} says Woof!"

    def __str__(self):             # what print()/str() returns
        return f"Dog(name={self.name}, age={self.age})"

    def __repr__(self):            # dev-facing representation (for debugging)
        return self.__str__()

buddy = Dog("Buddy", 5)
print(buddy.bark())

# --- GENERATORS ---
# yield instead of return — produces values lazily, one at a time (saves memory)
def countdown(n):
    while n > 0:
        yield n                    # pauses function, returns value
        n -= 1                     # resumes here on next call

for num in countdown(5):
    print(num)

# Generator expression — like list comp but with (), lazy evaluation
gen = (x ** 2 for x in range(1_000_000))  # nothing in memory
print(next(gen))   # 0
print(next(gen))   # 1

# --- DECORATORS ---
# Wraps a function to add behavior (logging, timing, auth, etc.)
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer                              # @syntax applies the decorator
def slow_function():
    import time; time.sleep(1)

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

# --- GOTCHAS ---
# 1. Mutable default args are SHARED between calls
def append_to(item, target=[]):     # BAD — list persists across calls
    target.append(item)
    return target

def append_to_fixed(item, target=None):  # GOOD — create new list each call
    if target is None:
        target = []
    target.append(item)
    return target

# 2. Use 'is' for None/True/False, '==' for values
x_val = None
if x_val is None: print("correct")
if x_val == None: print("works but bad style")

# 3. Shallow vs deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()           # first level copied, inner lists still shared
deep = copy.deepcopy(original)      # fully independent at all levels
