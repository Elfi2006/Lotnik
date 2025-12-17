# zad_2d.py


def co_drugi_element(moja_lista):
    print("Co drugi element z listy:")

    # Lepiej zrobic to tak, zeby bylo widac, ze sie nie uzywa slicing
    index = 0
    while index < len(moja_lista):
        print(moja_lista[index])
        index = index + 2  # Licznik co 2


# Testowanie
lista_wejsciowa = []
for k in range(10):
    lista_wejsciowa.append(k)

co_drugi_element(lista_wejsciowa)
