# Zadanie 3: Funkcja sprawdzająca parzystość
def is_even(number: int) -> bool:
    """Sprawdza, czy liczba jest parzysta (zwraca True lub False)."""
    return number % 2 == 0


# Uruchomienie funkcji i zapisanie
test_number = 15
czy_parzysta = is_even(test_number)

# Warunek logiczny
print("--- Zadanie 3 ---")
print(f"Sprawdzana liczba: {test_number}")

if czy_parzysta:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
