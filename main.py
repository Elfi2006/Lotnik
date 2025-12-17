# --Import z Zadania 1 (Pakiet magazine)
# Importuje Product i Order
from magazine.Product import Product
from magazine.Order import Order

# --- Importy z Zadania 2 (Pakiet vehicles) ---
# Importuje klasę Car
from vehicles.car import Car

if __name__ == "__main__":
    print("--- START APLIKACJI - Modularyzacja Własnego Kodu ---")

    # =========================================================
    #            TESTOWANIE ZADANIA 1 (magazine)
    # =========================================================
    print("\n[TEST KLAS PRODUCT I ORDER]")

    # Tworzenie produktów
    laptop = Product("Laptop Gamingowy", 5999.50)
    myszka = Product("Myszka bezprzewodowa", 99.99)

    # Wyświetlenie sformatowanej ceny
    print(laptop.get_formatted_price())

    # Tworzenie i sumowanie zamówieni
    zamowienie = Order("Jan Kowalski")
    zamowienie.add_item(laptop)
    zamowienie.add_item(myszka)

    # Wyświetlenie sumy zamówienia
    print(zamowienie.calculate_total())

    print("-" * 30)

    # =========================================================
    #            TESTOWANIE ZADANIA 2 (vehicles)
    # =========================================================
    print("[TEST KLASY CAR]")

    # Tworzę obiekt (instancję klasy Car)
    my_car = Car("Honda", "Civic", 2020)

    # Używam metod obiektu
    print(my_car.display_info())
    print(my_car.start_engine())
    print(my_car.start_engine())

    print("\n--- KONIEC APLIKACJI ---")
