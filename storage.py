
import json
import os

from models import Student


# სპეციალური გამონაკლისი
class StorageError(Exception):
    pass


# სტუდენტების შენახვის კლასი
class StudentStorage:

    def __init__(self, filename="students.json"):
        self.filename = filename

    # სტუდენტების ჩატვირთვა JSON ფაილიდან
    def load_students(self):

        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise StorageError("JSON ფაილის ფორმატი არასწორია!")

            students = []

            for item in data:
                students.append(Student.from_dict(item))

            return students

        except json.JSONDecodeError as error:
            raise StorageError(
                f"JSON ფაილის წაკითხვის შეცდომა: {error}"
            ) from error

        except (KeyError, TypeError, ValueError) as error:
            raise StorageError(
                f"მონაცემების დამუშავების შეცდომა: {error}"
            ) from error

        except OSError as error:
            raise StorageError(
                f"ფაილის გახსნის შეცდომა: {error}"
            ) from error

    # სტუდენტების შენახვა JSON ფაილში
    def save_students(self, students):

        temp_filename = self.filename + ".tmp"

        try:
            data = [student.to_dict() for student in students]

            with open(temp_filename, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            os.replace(temp_filename, self.filename)

        except (OSError, TypeError, ValueError) as error:

            if os.path.exists(temp_filename):
                os.remove(temp_filename)

            raise StorageError(
                f"მონაცემების შენახვა ვერ მოხერხდა: {error}"
            ) from error
