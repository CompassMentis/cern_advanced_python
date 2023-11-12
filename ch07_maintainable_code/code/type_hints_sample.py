class Student:
    def __init__(self, name: str, age: int | None) -> None:
        self.name: str = name
        self.age: int | None = age

    def greet(self) -> str:
        return f'Hello, my name is {self.name}!'


def filter_even_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


numbers: list[int] = [1, 2, 3, 4, 5, 6]
even_numbers: list[int] = filter_even_numbers(numbers)
print(even_numbers)  # [2, 4, 6]

student: Student = Student('Alex', 21)
greeting: str = student.greet()
print(greeting)      # Hello, my name is Alex!

a: list[int] = [1, 2, 3, 4]
b: list[int | float] = [1, 2.1]
c: tuple[int, float, float] = (1, 2.1, 3.5)

# Invalid:
# b: list[int, float, float] = [1, 2.1, 3.5]

d: dict[str, int] = {'amount': 10}
