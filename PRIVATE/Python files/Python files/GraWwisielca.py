haslo = input("Podaj haslo do odgadniecia: ")
literyOdgadywane = set()

while True:

    koniecgry = True
    for litera in haslo:
        if(litera in literyOdgadywane):
            print(litera, end=" ")
        else:
            print("*", end=" ")
            koniecgry = False
    print()

    if (koniecgry == True):
        print("Koniec gry")
        break

    zgadywanalitera = input("Podaj litere z hasla: ")
    literyOdgadywane.add(zgadywanalitera)

