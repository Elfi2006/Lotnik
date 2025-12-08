# magazine/Product.py

# Import niezależny (absolutny)

import magazine.utils

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        magazine.utils.log_action(f"Stworzono produkt: {self.name}")

    def get_formatted_price(self):
        # Używam funkcji formatującej z zaimportowanego modułu utils
        formatted = magazine.utils.format_price(self.price)
        return f"Produkt: {self.name}, Cena: {formatted}"