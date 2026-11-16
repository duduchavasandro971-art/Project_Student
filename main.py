
from models import Student
from storage import StudentStorage, StorageError
from validators import (
    validate_grade,
    validate_name,
    validate_roll_number
)


class StudentManagementSystem:

    def __init__(self):
        self.storage = StudentStorage()
        self.students = self.storage.load_students()

    def save(self):
        self.storage.save_students(self.students)

    # სტუდენტის ძებნა
    def find_student(self, roll_number):

        for student in self.students:
            if student.roll_number == roll_number:
                return student

        return None

    # ახალი სტუდენტის დამატება
    @validate_grade
    def add_student(self, name, roll_number, grade):

        name = validate_name(name)
        roll_number = validate_roll_number(roll_number)

        if self.find_student(roll_number):
            raise ValueError("ეს სიის ნომერი უკვე გამოყენებულია!")

        student = Student(name, roll_number, grade)

        self.students.append(student)

        try:
            self.save()
        except StorageError:
            self.students.remove(student)
            raise

        print("\nსტუდენტი წარმატებით დაემატა!")

    # ყველა სტუდენტის ნახვა
    def show_all_students(self):

        if not self.students:
            print("\nსტუდენტების სია ცარიელია!")
            return

        print("\n========== სტუდენტების სია ==========")

        for index, student in enumerate(self.students, start=1):
            print(f"{index}. {student}")

        print("=====================================")

    # სტუდენტის ძებნა ნომრით
    def search_student(self, roll_number):

        roll_number = validate_roll_number(roll_number)
        student = self.find_student(roll_number)

        if student:
            print("\nსტუდენტი მოიძებნა:")
            print(student.get_info())
        else:
            print("\nსტუდენტი ვერ მოიძებნა!")

    # შეფასების განახლება
    @validate_grade
    def update_grade(self, roll_number, grade):

        roll_number = validate_roll_number(roll_number)
        student = self.find_student(roll_number)

        if not student:
            print("\nსტუდენტი ვერ მოიძებნა!")
            return

        old_grade = student.grade
        student.grade = grade

        try:
            self.save()
        except StorageError:
            student.grade = old_grade
            raise

        print("\nშეფასება წარმატებით განახლდა!")

    # მენიუ
    def display_menu(self):

        print("\n===================================")
        print("      STUDENT MANAGEMENT SYSTEM")
        print("===================================")
        print("1. ახალი სტუდენტის დამატება")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. სტუდენტის ძებნა ნომრით")
        print("4. სტუდენტის შეფასების განახლება")
        print("5. გასვლა")
        print("===================================")

    # პროგრამის გაშვება
    def run(self):

        print("\nმოგესალმებით სტუდენტების მართვის სისტემაში!")

        while True:

            self.display_menu()

            choice = input("აირჩიეთ ოპერაცია (1-5): ").strip()

            try:

                if choice == "1":

                    print("\n--- ახალი სტუდენტი ---")

                    name = input("სახელი: ")
                    roll_number = input("სიის ნომერი: ")
                    grade = input("შეფასება (A-F): ")

                    self.add_student(name, roll_number, grade)

                elif choice == "2":

                    self.show_all_students()

                elif choice == "3":

                    number = input("შეიყვანეთ სიის ნომერი: ")
                    self.search_student(number)

                elif choice == "4":

                    number = input("შეიყვანეთ სიის ნომერი: ")
                    grade = input("ახალი შეფასება (A-F): ")

                    self.update_grade(number, grade)

                elif choice == "5":

                    print("\nპროგრამიდან გამოსვლა...")
                    print("ნახვამდის!")
                    break

                else:

                    print("\nარასწორი არჩევანი! აირჩიეთ 1-დან 5-მდე.")

            except ValueError as error:

                print(f"\nშეყვანის შეცდომა: {error}")

            except StorageError as error:

                print(f"\nფაილის შეცდომა: {error}")

            except KeyboardInterrupt:

                print("\nპროგრამა შეწყდა მომხმარებლის მიერ.")
                break

            except Exception as error:

                print(f"\nმოულოდნელი შეცდომა: {error}")


if __name__ == "__main__":

    try:
        app = StudentManagementSystem()
        app.run()

    except StorageError as error:
        print(f"მონაცემების ჩატვირთვის შეცდომა: {error}")

    except Exception as error:
        print(f"პროგრამის გაშვების შეცდომა: {error}")

