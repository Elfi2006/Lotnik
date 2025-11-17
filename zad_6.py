# Zadanie 6: Łączenie, usuwanie duplikatów i potęgowanie
from typing import List


def process_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    """Łączy listy, usuwa duplikaty, podnosi elementy do potęgi 3."""

    # 1. Złączenie list
    combined_list = list_a + list_b

    # 2. Usunięcie duplikatów
    unique_elements_set = set(combined_list)

    # 3. Podniesienie każdego elementu do potęgi 3
    powered_list = [element ** 3 for element in unique_elements_set]

    # 4. Zwrócenie listy (zamieniam set z powrotem na listę)
    return powered_list


# Uruchomienie
lista_A = [1, 2, 3, 3]
lista_B = [4, 5, 1]

wynikowa_lista = process_lists(lista_A, lista_B)

print("--- Zadanie 6 ---")
print(f"Łączone elementy unikalne: {sorted(list(set(lista_A + lista_B)))}")
print(f"Wynik po potęgowaniu: {wynikowa_lista}")