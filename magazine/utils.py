

def format_price(price):
    """Formatuje cenę do formatu walutowego."""
    return f"{price:.2f} PLN"

def log_action(action):
    """Prosta funkcja do logowania."""
    print(f"[LOG] Akcja: {action} została wykonana.")