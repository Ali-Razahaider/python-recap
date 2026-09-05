class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def eat(self) -> str:
        return f"{self.name} is eating"

    def sleep(self) -> str:
        return f"{self.name} is sleeping"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self.breed = breed

    def bark(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.color = color

    def meow(self) -> str:
        return f"{self.name} says Meow!"


if __name__ == "__main__":
    dog = Dog("Buddy", 3, "Golden Retriever")
    print(dog.eat())
    print(dog.bark())
    print(f"Name: {dog.name}, Age: {dog.age}, Breed: {dog.breed}")

    cat = Cat("Whiskers", 5, "Black")
    print(cat.eat())
    print(cat.meow())
    print(f"Name: {cat.name}, Age: {cat.age}, Color: {cat.color}")

    print("\nPolymorphism demo:")
    for animal in [dog, cat]:
        print(animal.sleep())