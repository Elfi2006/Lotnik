

class Property:
    """Klasa bazowa opisująca posiadłość/nieruchomość."""

    def __init__(self, area, rooms, price, address):
        self.area = area  # Powierzchnia (np. w m2)
        self.rooms = rooms  # Liczba pokoi
        self.price = price  # Cena
        self.address = address

    def __str__(self):
        return (f"Nieruchomość: {self.address} | Powierzchnia: {self.area}m2, "
                f"Pokoje: {self.rooms} | Cena: {self.price} PLN")


class House(Property):
    """Klasa dziedzicząca po Property, opisująca Dom."""

    def __init__(self, area, rooms, price, address, plot):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(area, rooms, price, address)
        self.plot = plot  # Rozmiar działki (int, np. w m2)

    def __str__(self):
        # Używamy __str__ klasy nadrzędnej
        base_str = super().__str__()
        # Zmieniam opis
        return f"Dom: {base_str.replace('Nieruchomość', 'Opis bazowy')} | Działka: {self.plot}m2"


class Flat(Property):
    """Klasa dziedzicząca po Property, opisująca Mieszkanie."""

    def __init__(self, area, rooms, price, address, floor):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(area, rooms, price, address)
        self.floor = floor  # Piętro (int)

    def __str__(self):
        # Używamy __str__ klasy nadrzędnej
        base_str = super().__str__()
        # Zmieniam opis, aby pokazać, że to Mieszkanie
        return f"Mieszkanie: {base_str.replace('Nieruchomość', 'Opis bazowy')} | Piętro: {self.floor}"


#  Tworzenie obiektów i testowani
print("\n" + "=" * 50)
print("PRZYKŁADY DZIEDZICZENIA:")
print("=" * 50)

house1 = House(area=150, rooms=5, price=850000, address="Wesoła 10, Gdynia", plot=500)
print(house1)

flat1 = Flat(area=65, rooms=3, price=450000, address="Nowa 3/12, Sopot", floor=2)
print(flat1)