
class Student:
    def __init__(self, name, roll_number, grade):
        self.__name = name
        self.__roll_number = roll_number
        self.__grade = grade

    # Getter მეთოდები
    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_grade(self):
        return self.__grade

    # შეფასების განახლება
    def update_grade(self, new_grade):
        self.__grade = new_grade

    # სტუდენტის ინფორმაციის ჩვენება
    def display_info(self):
        print("-------------------------")
        print(f"სახელი: {self.__name}")
        print(f"სიის ნომერი: {self.__roll_number}")
        print(f"შეფასება: {self.__grade}")
        print("-------------------------")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # ახალი სტუდენტის დამატება
    def add_student(self):
        name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()

        if not name:
            print("შეცდომა! სახელი არ უნდა იყოს ცარიელი.")
            return

        try:
            roll_number = int(input("შეიყვანეთ სიის ნომერი: "))

            if roll_number <= 0:
                print("შეცდომა! ნომერი უნდა იყოს დადებითი.")
                return

        except ValueError:
            print("შეცდომა! ნომერი უნდა იყოს მთელი რიცხვი.")
            return

        # ნომრის უნიკალურობის შემოწმება
        if self.find_student(roll_number):
            print("ასეთი ნომრის მქონე სტუდენტი უკვე არსებობს!")
            return

        grade = input("შეიყვანეთ შეფასება (A-F): ").strip().upper()

        if grade not in ["A", "B", "C", "D", "E", "F"]:
            print("შეცდომა! შეფასება უნდა იყოს A, B, C, D, E ან F.")
            return

        student = Student(name, roll_number, grade)
        self.students.append(student)

        print("სტუდენტი წარმატებით დაემატა!")

    # ყველა სტუდენტის ჩვენება
    def display_all_students(self):
        if not self.students:
            print("სტუდენტების სია ცარიელია.")
            return

        print("\n===== ყველა სტუდენტი =====")

        for student in self.students:
            student.display_info()

    # სტუდენტის ძებნა ნომრით
    def find_student(self, roll_number):
        for student in self.students:
            if student.get_roll_number() == roll_number:
                return student

        return None

    def search_student(self):
        try:
            roll_number = int(input("შეიყვანეთ სტუდენტის სიის ნომერი: "))

            student = self.find_student(roll_number)

            if student:
                print("\nსტუდენტი მოიძებნა!")
                student.display_info()
            else:
                print("სტუდენტი ვერ მოიძებნა.")

        except ValueError:
            print("შეცდომა! შეიყვანეთ სწორი მთელი რიცხვი.")

    # შეფასების განახლება
    def update_student_grade(self):
        try:
            roll_number = int(
                input("შეიყვანეთ სტუდენტის სიის ნომერი: ")
            )

            student = self.find_student(roll_number)

            if student is None:
                print("სტუდენტი ვერ მოიძებნა.")
                return

            new_grade = input(
                "შეიყვანეთ ახალი შეფასება (A-F): "
            ).strip().upper()

            if new_grade not in ["A", "B", "C", "D", "E", "F"]:
                print("არასწორი შეფასება!")
                return

            student.update_grade(new_grade)

            print("შეფასება წარმატებით განახლდა!")

        except ValueError:
            print("შეცდომა! შეიყვანეთ სწორი ნომერი.")

    # მთავარი მენიუ
    def menu(self):
        while True:
            print("\n===== სტუდენტების მართვის სისტემა =====")
            print("1. ახალი სტუდენტის დამატება")
            print("2. ყველა სტუდენტის ნახვა")
            print("3. სტუდენტის ძებნა ნომრის მიხედვით")
            print("4. სტუდენტის შეფასების განახლება")
            print("5. გასვლა")

            choice = input("აირჩიეთ მოქმედება (1-5): ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_all_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student_grade()

            elif choice == "5":
                print("პროგრამა დასრულდა. ნახვამდის!")
                break

            else:
                print("არასწორი არჩევანი! სცადეთ თავიდან.")


# პროგრამის გაშვება
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()
