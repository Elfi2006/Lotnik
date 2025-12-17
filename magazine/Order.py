# Import niezależny (absolutny)
import magazine.utils


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        magazine.utils.log_action(f"Utworzono zamówienie dla: {self.customer}")

    def add_item(self, product):
        self.items.append(product)
        magazine.utils.log_action(f"Dodano {product.name} do zamówienia.")

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return (
            f"Suma zamówienia dla {self.customer}: {magazine.utils.format_price(total)}"
        )
