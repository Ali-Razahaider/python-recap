# Simple dataclasses example
from dataclasses import dataclass

# Create a data class - like a simple struct
@dataclass
class Student:
    name: str
    age: int
    grade: str = "A"  # default value

# Create a student object
s1 = Student(name="Alice", age=20)
print(f"Student: {s1.name}, {s1.age}, grade: {s1.grade}")

# Create another student with all fields
s2 = Student(name="Bob", age=22, grade="B")
print(f"Student: {s2.name}, {s2.age}, grade: {s2.grade}")

