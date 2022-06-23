def dodaj(imie, nazwisko, grupa):
    plik = open("dane.txt", "a")
    plik.write(f"{imie};{nazwisko};{grupa}\n")
    plik.close()


def pokaz():
    plik = open("dane.txt", "r")

    for i in plik:
        dane = i.split(";")
        print(f"Imie: {dane[0]}, Nazwisko: {dane[1]}, Grupa: {dane[2].strip()}}}")

    plik.close()


def usun(nazwisko):
    plik = open("dane.txt", "r")
    dane = plik.readlines()
    plik.close()
    znaleziono = False
    for i in dane:
        iSplit = i.split(";")
        if iSplit[1] == nazwisko:
            znaleziono = True
            dane.remove(i)
            print("Usunieto")
            break
    if (znaleziono == False):
        print("Studenta nie został odnaleziony")
    else:
        plik = open("dane.txt", "w")
        plik.writelines(dane)
        plik.close()


def zmien(nazwisko, noweImie, noweNazwisko):
    plik = open("dane.txt", "r")
    dane = []
    znaleziono = False
    for i in plik:
        iSplit = i.split(";")
        if (iSplit[1] == nazwisko):
            znaleziono = True

            if (noweImie != ""):
                iSplit[0] = noweImie

            if (noweNazwisko != ""):
                iSplit[1] = noweNazwisko

            dane.append(f"{iSplit[0]};{iSplit[1]};{iSplit[2]}")
        else:
            dane.append(i)

    if (znaleziono == False):
        print("Studenta nie został odnaleziony")
    else:
        plik = open("dane.txt", "w")
        plik.writelines(dane)
        plik.close()

while (True):

    menu = input("D-dodaj, P-pokaz, U-usun, Z-zmien, K-koniec: ").upper()

    if (menu == "D"):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        grupa = input("Podaj grupe: ")

        dodaj(imie, nazwisko, grupa)
    elif (menu == "P"):
        pokaz()
    elif (menu == "U"):
        nazwisko = input("Podaj nazwisko: ")
        usun(nazwisko)
    elif (menu == "Z"):
        nazwisko = input("Podaj nazwisko: ")
        noweImie = input("Podaj noweImie: ")
        noweNazwisko = input("Podaj noweNazwisko: ")
        zmien(nazwisko, noweImie, noweNazwisko)

    elif (menu == "K"):
        break