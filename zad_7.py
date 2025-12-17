# zad_7.py

import requests
from typing import Optional, Dict, Any, List


# KROK 1: Definicja Klasy z Typowaniem


class Brewery:
    """Klasa reprezentująca browar na podstawie danych z openbrewerydb.org."""

    # Atrybuty z adnotacjami typów
    id: str
    name: str
    brewery_type: str
    city: str
    country: str
    # Używam Optional[str], bo te pola mogą być puste (None)
    phone: Optional[str]
    website_url: Optional[str]

    def __init__(self, data: Dict[str, Any]):
        """Konstruktor: Inicjuje obiekt danymi ze słownika z API."""
        self.id = data.get("id", "N/A")
        self.name = data.get("name", "Brak nazwy")
        self.brewery_type = data.get("brewery_type", "N/A")
        self.city = data.get("city", "N/A")
        self.country = data.get("country", "N/A")
        self.phone = data.get("phone")
        self.website_url = data.get("website_url")

    # Magiczna metoda __str__ - definiuje, jak obiekt ma się wyświetlać
    def __str__(self) -> str:
        """Zwraca przyjazny opis obiektu (wymagane w zadaniu)."""
        # Używam prostego formatowania, żeby dane były czytelne
        return (
            f"--- 🍺 Browar: {self.name} ---\n"
            f"  Typ: {self.brewery_type.capitalize()}\n"
            f"  Lokalizacja: {self.city}, {self.country}\n"
            f"  Telefon: {self.phone if self.phone else 'Brak'}\n"
            f"  Strona WWW: {self.website_url if self.website_url else 'Brak'}"
        )


#  KROK 2: Logika Pobierania Danych


def fetch_breweries() -> List[Brewery]:
    """Pobiera 20 pierwszych browarów z API i zwraca listę obiektów Brewery."""

    base_url = "https://api.openbrewerydb.org/v1/breweries"
    # Parametr per_page=20 zapewnia, że pobierzemy 20 obiektów
    params = {"per_page": 20}

    print("Pobieranie 20 pierwszych obiektów...")

    try:
        # Łącze z API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Wyrzuci błąd, jeśli status to 4xx lub 5xx
        data = response.json()

        # Tworze liste instancji Brewery
        brewery_list = [Brewery(item) for item in data]
        return brewery_list

    except requests.RequestException as e:
        print(f"BŁĄD: Nie udało się połączyć z API lub pobrać danych: {e}")
        return []


# --- KROK 3: Główna Logika Skryptu (Uruchomienie) ---

if __name__ == "__main__":
    # Pobranie danych
    browary = fetch_breweries()

    print(f"\n--- Znaleziono łącznie {len(browary)} browarów ---")

    # Przeiterowanie i wyświetlenie każdego obiektu
    for browar in browary:
        print("\n" + "=" * 40)
        print(browar)  # Wywołuje metodę __str__

    if not browary:
        print("\nLista browarów jest pusta. Sprawdź połączenie z internetem.")
