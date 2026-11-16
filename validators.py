
from functools import wraps


# შეფასების ვალიდაციის დეკორატორი
def validate_grade(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        grade = kwargs.get("grade")

        if grade is None and len(args) >= 2:
            grade = args[-1]

        if not isinstance(grade, str):
            raise ValueError("შეფასება უნდა იყოს სიმბოლო!")

        grade = grade.strip().upper()

        if grade not in ["A", "B", "C", "D", "E", "F"]:
            raise ValueError(
                "შეიყვანეთ სწორი შეფასება (A, B, C, D, E ან F)!"
            )

        return func(*args, **kwargs)

    return wrapper


# სახელის ვალიდაცია
def validate_name(name):

    if not isinstance(name, str) or not name.strip():
        raise ValueError("სახელი არ შეიძლება იყოს ცარიელი!")

    if not any(char.isalpha() for char in name):
        raise ValueError("სახელი უნდა შეიცავდეს ასოებს!")

    return name.strip()


# სიის ნომრის ვალიდაცია
def validate_roll_number(number):

    try:
        number = int(number)

    except (ValueError, TypeError):
        raise ValueError("სიის ნომერი უნდა იყოს მთელი რიცხვი!")

    if number <= 0:
        raise ValueError("სიის ნომერი უნდა იყოს დადებითი!")

    return number
