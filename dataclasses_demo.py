# Simple dataclasses demo
from dataclasses import dataclass

# Data class = simple struct with auto-generated __init__ and __repr__
@dataclass
class Student:
    name: str    # student's name
    age: int     # student's age
    grade: str = "A"  # default grade is A

# Create student s1 with name and age (grade uses default "A")
s1 = Student(name="Alice", age=20)

# Create student s2 with all fields
s2 = Student(name="Bob", age=22, grade="B")

# Print both students (auto-generated __repr__)
print(s1)
print(s2)