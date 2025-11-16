# zad_1.py

def zadanie_1_imiona(lista_imion):
    print("--- Zadanie 1: Wyświetl 5 Imion ---")

    # Używam while
    licznik = 0
    while licznik < len(lista_imion):
        # Pobieram imię
        imie = lista_imion[licznik]
        print("Imie numer", licznik + 1, ":", imie)


        licznik = licznik + 1


# uruchamiam
moja_lista_imion = ["Wiktor", "Teresa", "Maria", "Kamil", "Alicja"]
zadanie_1_imiona(moja_lista_imion)