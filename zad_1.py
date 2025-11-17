# zad_1.py
# Wymaganie Funkcja, która przyjmuje 2 stringi (name, surname

def create_greeting(name: str, surname: str) -> str:
    """Tworzy powitalny string "Cześć {name} {surname}!". """
    # f-stringi to najprostszy sposób na wstawienie zmiennych do tekstu
    return f"Cześć {name} {surname}!"

# Uruchomiam funkcję
result_greeting = create_greeting("Wiktor", "Jaskółka")

# Wyświetl zmienną
print(f"Zadanie 1:\n{result_greeting}\n")