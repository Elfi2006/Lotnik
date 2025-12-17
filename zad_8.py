# zad_8.py

import requests
import argparse  # Moduł do obsługi argumentów z linii poleceń
from typing import Optional, Dict, Any, List


# --- Klasa Brewery (skopiowana z zad_7.py, aby plik był niezależny) ---


class Brewery:
    """Klasa reprezentująca browar."""

    # ... (definicja klasy jest taka sama jak w zad_7.py)
    id: str
    name: str
    brewery_type: str
    city: str
    country: str
    phone: Optional[str]
    website_url: Optional[str]

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id", "N/A")
        self.name = data.get("name", "Brak nazwy")
        self.brewery_type = data.get("brewery_type", "N/A")
        self.city = data.get("city", "N/A")
        self.country = data.get("country", "N/A")
        self.phone = data.get("phone")
        self.website_url = data.get("website_url")

    def __str__(self) -> str:
        return (
            f"--- 🍺 Browar: {self.name} ---\n"
            f"  Typ: {self.brewery_type.capitalize()}\n"
            f"  Lokalizacja: {self.city}, {self.country}\n"
            f"  Telefon: {self.phone if self.phone else 'Brak'}\n"
            f"  Strona WWW: {self.website_url if self.website_url else 'Brak'}"
        )


# KROK 1: Logika Pobierania z Filtrem


def fetch_breweries(city_filter: Optional[str] = None) -> List[Brewery]:
    """Pobiera do 20 browarów, opcjonalnie filtrując po mieście."""

    base_url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}

    if city_filter:
        params["by_city"] = city_filter
        print(f"Pobieranie browarów dla miasta: {city_filter}...")
    else:
        print("Pobieranie wszystkich (bez filtra) browarów...")

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        brewery_list = [Brewery(item) for item in data]
        return brewery_list

    except requests.RequestException as e:
        print(f"BŁĄD: Nie udało się połączyć z API: {e}")
        return []


def main():
    """Używa argparse do wczytania argumentów z linii poleceń."""

    # 1. Tworzenie parsera
    parser = argparse.ArgumentParser(
        description="Pobiera informacje o browarach z API. Użyj --city, aby filtrować."
    )

    # 2. Dodawanie argumentu --city
    parser.add_argument(
        "--city",
        type=str,
        help="Ogranicza pobierane browary do podanego miasta. Np.: --city=Chicago",
        default=None,  # Wartość domyślna to None, jeśli użytkownik nic nie poda
    )

    args = parser.parse_args()

    # Pobranie danych, używając wartości z argumentów
    breweries = fetch_breweries(args.city)

    print(f"\n--- Znaleziono {len(breweries)} browarów ---")

    # Wyświetlenie wyników
    for browar in breweries:
        print("\n" + "=" * 40)
        print(browar)

    if not breweries:
        print("\nNie znaleziono browarów spełniających kryteria.")


if __name__ == "__main__":
    main()
