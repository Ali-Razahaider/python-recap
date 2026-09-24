# Simple dataclasses demo
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: str = "A"

s1 = Student(name="Alice", age=20)
s2 = Student(name="Bob", age=22, grade="B")

print(s1)
print(s2)