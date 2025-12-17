# zad_3.py


def tylko_parzyste_petla_while(lista_liczb):
    print("\n--- Zadanie 3: Tylko Liczby Parzyste (While) ---")
    print(f"Lista glowna: {lista_liczb}")

    indeks = 0
    while indeks < len(lista_liczb):

        liczba = lista_liczb[indeks]

        # Sprawdzam parzystość
        if (liczba % 2) == 0:
            print("Parzysta:", liczba)
        else:
            # Wypisuje coś
            print(liczba, "jest nieparzysta, pomijamy.")

        indeks = indeks + 1


# Uruchomienie
lista_c = list(range(1, 11))  # 10 liczb
tylko_parzyste_petla_while(lista_c)
