# zad_2.py (Wersja 2.0)


def mnozenie_petla_niedoświadczona(lista_liczb):
    print("\n--- Zadanie 2 (i): Mnozenie petla for (Indeksy) ---")



    # Petla przechodzi przez indeksy: 0, 1, 2, 3, 4
    for i in range(len(lista_liczb)):

        lista_liczb[i] = lista_liczb[i] * 2

    return lista_liczb



def mnozenie_skladana_prosta(lista_liczb):
    print("\n--- Zadanie 2 (ii): Mnozenie lista skladana ---")
    lista_wynikowa = [x * 2 for x in lista_liczb]
    return lista_wynikowa


# Uruchomienie
liczby_a = [10, 2, 8, 4, 15]
print(f"Lista do mnozenia (przed petla): {liczby_a}")
wynik_petla = mnozenie_petla_niedoświadczona(liczby_a)
print(f"Lista po pętli (zmieniona!): {wynik_petla}")

liczby_b = [1, 3, 5, 7, 9]
wynik_skladana = mnozenie_skladana_prosta(liczby_b)
print(f"Lista po składanej (nowa lista): {wynik_skladana}")