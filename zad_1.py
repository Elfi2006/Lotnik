class Student:
    """Klasa reprezentująca studenta z jego imieniem i listą stopni"""

    def __init__(self, name, marks):
        """Konstruktor klasy Student."""
        self.name = name
        self.marks = marks  # marks to lista stopni (liczb)

    def is_passed(self):
        """Sprawdza, czy średnia ocen jest > 50."""
        if not self.marks:

            return False

        average_mark = sum(self.marks) / len(self.marks)
        return average_mark > 50


student_passed = Student("Andżelika Jaskółka", [60, 75, 80, 55, 90])
print(f"Czy {student_passed.name} zaliczyła? {student_passed.is_passed()}")


student_failed = Student("Filip Kusiak", [45, 50, 30, 60, 40])
print(f"Czy {student_failed.name} zaliczył? {student_failed.is_passed()}")
