# Zadanie 4: Porównanie sumy dwóch liczb z trzecią
def check_sum_vs_third(a: int, b: int, c: int) -> bool:
    """Sprawdza, czy suma a + b jest większa lub równa c."""
    return (a + b) >= c

# Uruchomienie i wyświetlenie wyników
wynik_1 = check_sum_vs_third(10, 5, 15)  # 15 >= 15 -> True
wynik_2 = check_sum_vs_third(10, 5, 16)  # 15 >= 16 -> False

print("--- Zadanie 4 ---")
print(f"Czy 10 + 5 >= 15? {wynik_1}")
print(f"Czy 10 + 5 >= 16? {wynik_2}")