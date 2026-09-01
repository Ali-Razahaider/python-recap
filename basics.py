 # =============================================================================
# PART 1: DATA TYPES & STRUCTURES
# =============================================================================

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

# f-strings: embed expressions inside strings & formatting
full = f"{greeting}, {name}!"        # "Hello, World!"
calculated = f"2 + 2 = {2 + 2}"     # "2 + 2 = 4"
formatted_float = f"{3.14159:.2f}"   # "3.14" — specifier for decimal places
padded_num = f"{42:05d}"            # "00042" — zero-padded to 5 digits

# String methods — all return NEW strings, original unchanged
text = "  Hello, Python!  "
print(text.strip())                   # "Hello, Python!" — remove leading/trailing whitespace
print(text.strip().lower())           # "hello, python!"
print(text.strip().upper())           # "HELLO, PYTHON!"
print(text.strip().replace("Python", "World"))  # "Hello, World!"
print(text.strip().split(","))        # split into list by delimiter: ['Hello', ' Python!']

# Useful string checks & join (80/20 workhorses)
csv_line = "alice,admin,active"
items = csv_line.split(",")           # ['alice', 'admin', 'active']
joined_str = "-".join(items)         # "alice-admin-active" — join list of strings

print("filename.py".endswith(".py"))  # True — prefix/suffix checking
print("https://example.com".startswith("https")) # True
print("12345".isdigit())              # True — test character content

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
fruits.extend(["fig", "grape"])# append multiple elements from iterable
fruits.insert(1, "blueberry")  # insert at index
fruits.remove("banana")        # remove by value
popped = fruits.pop()          # remove & return last
fruits.sort()                  # sort in place (modifies list)
sorted_fruits = sorted(fruits) # returns new sorted list, leaves original intact

# Unpacking / Spreading lists (Python 3.5+)
combined = [*fruits, "kiwi", *"mango"]  # merge lists cleanly

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

# --- SETS ---
# Unordered, unique elements. Fast O(1) lookups and set mathematics.
tags = {"python", "coding", "django"}
tags.add("fastapi")
tags.remove("django")            # raises KeyError if missing; tags.discard() won't

# Deduplication (very common pattern)
duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(duplicates))  # [1, 2, 3, 4, 5]

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a | set_b)             # Union: {1, 2, 3, 4, 5, 6}
print(set_a & set_b)             # Intersection: {3, 4}
print(set_a - set_b)             # Difference: {1, 2}
print(set_a ^ set_b)             # Symmetric Difference: {1, 2, 5, 6}

# --- DICTIONARIES ---
# Key-value pairs, O(1) average lookup
person = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}

print(person["name"])            # KeyError if key missing
print(person.get("salary", 0))   # .get() returns default if key missing (safer)
person.setdefault("role", "dev") # sets default if key doesn't exist yet
person["email"] = "a@b.com"      # add/update
del person["age"]                # delete
if "name" in person:             # check key exists
    print("name is present")

print(person.keys())             # dict_keys([...])
print(person.values())           # dict_values([...])
print(person.items())            # dict_items([('name', 'Alice'), ...])

# Iterating dictionaries cleanly
for key, value in person.items():
    print(f"{key}: {value}")

# Dict comprehension
squares_dict = {x: x**2 for x in range(6)}

# Merging dicts (Python 3.9+) & Unpacking
defaults = {"color": "blue", "size": 10}
override = {"color": "red", "weight": 5}
merged = defaults | override              # union operator (override wins)
merged_unpacking = {**defaults, **override} # equivalent via dict unpacking

