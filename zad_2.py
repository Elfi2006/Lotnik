class Student:
    def __init__(self, n, o):
        self.name = n
        self.oceny = o

    def __str__(self):
        # Bardzo prosta reprezentacja
        return f"Student: {self.name}"


class Library:
    def __init__(self, miasto, ulica, kod, godziny_otwarcia, tel):

        self.miasto = miasto
        self.street = ulica
        self.zip_code = kod
        self.godziny_otwarcia = godziny_otwarcia
        self.telefon = tel

    def __str__(self):
        # Proste, nieformatowane ciągi znaków
        return "Biblioteka w " + self.miasto + ", tel: " + self.telefon


class Employee:
    def __init__(self, imie, nazwisko, data_zatr, urodz, miasto, ulica, kod, tel):
        self.first_name = imie
        self.nazwisko = nazwisko
        self.data_zatr = data_zatr
        self.birth_date = urodz
        self.miasto = miasto
        self.ulica = ulica
        self.zip_code = kod
        self.phone = tel

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.nazwisko}, zatr. {self.data_zatr}"


class Book:
    def __init__(self, lib, pub_date, aut_imie, aut_nazw, stron):
        self.library = lib  # Obiekt biblioteki
        self.data_publikacji = pub_date
        self.author_name = aut_imie
        self.aut_nazw = aut_nazw
        self.liczba_stron = stron

    def __str__(self):

        return (
            f"Tytuł: {self.author_name} {self.aut_nazw} | Strony: {self.liczba_stron} | "
            f"Lokalizacja: {str(self.library)}"
        )  # Użycie str() zamiast f-stringów


class Order:
    def __init__(self, pracownik, student, lista_ksiazek, data):
        self.pracownik = pracownik
        self.student = student
        self.lista_ksiazek = lista_ksiazek
        self.data = data

    def __str__(self):

        opis = f"Zamówienie z dnia {self.data}\n"
        opis += f"  Obsługa: {self.pracownik.first_name}\n"
        opis += f"  Klient: {self.student.name}\n"
        opis += "  KSIĄŻKI:\n"

        for ksiazka in self.lista_ksiazek:
            opis += f"    - {str(ksiazka)}\n"

        return opis


lib_wawa = Library(
    "Warszawa", "Marszałkowska 10", "00-501", "Pn-Pt 9-18", "123-456-789"
)
lib_krak = Library("Kraków", "Długa 5", "31-147", "Pn-Sb 10-17", "987-654-321")

book1 = Book(lib_wawa, "2020-05-15", "Adam", "Mickiewicz", 350)
book2 = Book(lib_wawa, "1998-11-01", "Eliza", "Orzeszkowa", 620)
book3 = Book(lib_krak, "2023-01-20", "Olga", "Tokarczuk", 120)

emp1 = Employee(
    "Marta",
    "Kowalska",
    "2018-03-01",
    "1990-05-12",
    "Warszawa",
    "Kwiatowa 5",
    "01-100",
    "500-111-222",
)
emp2 = Employee(
    "Jan",
    "Wójcik",
    "2021-07-15",
    "1985-01-20",
    "Kraków",
    "Słoneczna 8",
    "31-001",
    "500-333-444",
)

stud1 = Student("Anna Nowak", [60, 70, 80])
stud3 = Student("Ewa Lis", [40, 50, 45])


order1 = Order(emp1, stud1, [book1, book2], "2025-11-25")
order2 = Order(emp2, stud3, [book3], "2025-11-25")


print("\n" + "=" * 40)
print("ZAMÓWIENIE 1:")
print("=" * 40)
print(order1)

print("\n" + "=" * 40)
print("ZAMÓWIENIE 2:")
print("=" * 40)
print(order2)
