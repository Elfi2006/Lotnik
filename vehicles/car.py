class Car:
    """Klasa reprezentująca samochód."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model}: Silnik uruchomiony."
        return f"{self.brand} {self.model}: Silnik już pracuje."

    def display_info(self):
        return f"Samochód: {self.brand} {self.model} ({self.year})"
