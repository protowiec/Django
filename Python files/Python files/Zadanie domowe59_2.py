import random

for x in range(5):
    liczba1 = random.randint(1, 10)
    liczba2 = random.randint(1, 10)
    while True:
        odp = input(f"jaki jest wynik mnozenia {liczba1} * {liczba2} = ?")
        wynikkomputera = liczba1 * liczba2
        print(wynikkomputera)

        if (wynikkomputera == odp):
            print("Poprawna odpowiedz")
            break
        else:
            print("Zla odpowiedz")