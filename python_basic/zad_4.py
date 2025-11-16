# zad_4.py

def pokaz_co_drugi_while_manual(lista_liczb):
    print("\n--- Zadanie 4: Co Drugi Element (Manualny Krok) ---")
    print(f"Lista poczatkowa: {lista_liczb}")

    # Zaczynam od indeksu 0
    indeks_do_wyswietlenia = 0

    while indeks_do_wyswietlenia < len(lista_liczb):
        # Wypisuje element
        element = lista_liczb[indeks_do_wyswietlenia]
        print("Wybrany element:", element)

        # Zwiększam licznik
        indeks_do_wyswietlenia = indeks_do_wyswietlenia + 2


# Uruchomienie
lista_d = list(range(20, 30))  # 10 liczb (20, 21, ..., 29)
pokaz_co_drugi_while_manual(lista_d)