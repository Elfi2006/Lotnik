# Zadanie 5: Sprawdzenie, czy wartość jest w liście
from typing import List


def contains_value(data_list: List[int], value: int) -> bool:
    """Sprawdza, czy podana wartość jest obecna w liście."""
    return value in data_list


# Uruchomienie
moja_lista = [100, 200, 300, 400]
wynik_obecny = contains_value(moja_lista, 300)
wynik_nieobecny = contains_value(moja_lista, 500)

print("--- Zadanie 5 ---")
print(f"Lista: {moja_lista}")
print(f"Czy lista zawiera 300? {wynik_obecny}")
print(f"Czy lista zawiera 500? {wynik_nieobecny}")
