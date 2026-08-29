# =============================================================================
# PART 3: INTERMEDIATE CONCEPTS
# =============================================================================

# --- IMPORTS ---
import os                          # file paths, dirs, env vars
import sys                         # argv, path, exit
import json                        # json.loads() / json.dumps()
import re                          # regular expressions
from datetime import datetime, timedelta
from collections import Counter, defaultdict
from pathlib import Path           # modern file paths

# --- LIST COMPREHENSIONS (advanced) ---
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
