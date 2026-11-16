
from abc import ABC, abstractmethod


# საბაზისო კლასი
class Person(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("სახელი არასწორია!")
        self._name = value.strip()

    @abstractmethod
    def get_info(self):
        pass


# Student კლასი მემკვიდრეობით იღებს Person კლასს
class Student(Person):

    def __init__(self, name, roll_number, grade):
        super().__init__(name)

        self._roll_number = None
        self._grade = None

        self.roll_number = roll_number
        self.grade = grade

    @property
    def roll_number(self):
        return self._roll_number

    @roll_number.setter
    def roll_number(self, value):
        if type(value) is not int or value <= 0:
            raise ValueError("სიის ნომერი უნდა იყოს დადებითი მთელი რიცხვი!")
        self._roll_number = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        valid_grades = ["A", "B", "C", "D", "E", "F"]

        if not isinstance(value, str):
            raise ValueError("შეფასება უნდა იყოს სიმბოლო!")

        value = value.strip().upper()

        if value not in valid_grades:
            raise ValueError("შეფასება უნდა იყოს A, B, C, D, E ან F!")

        self._grade = value

    def get_info(self):
        return (
            f"სახელი: {self.name}\n"
            f"სიის ნომერი: {self.roll_number}\n"
            f"შეფასება: {self.grade}"
        )

    # პოლიმორფიზმი
    def __str__(self):
        return (
            f"სახელი: {self.name} | "
            f"ნომერი: {self.roll_number} | "
            f"შეფასება: {self.grade}"
        )

    # სერიალიზაცია
    def to_dict(self):
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "grade": self.grade
        }

    # დესერიალიზაცია
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["roll_number"],
            data["grade"]
        )
