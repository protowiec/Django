def Dodaj(imie, nazwisko, grupa):
    plik = open("85.txt", "a")
    plik.write(f"{imie};{nazwisko};{grupa}\n")
    plik.close()
    print("Dodano studenta.")


def Pokaz():
    plik = open("85.txt", "r")
    for i in plik:
        dane = i.split(";")
        print(f"Imie: {dane[0]}, Nazwisko: {dane[1]}, Grupa: {dane[2]}")
    plik.close()

def Usun(nazwisko):
    plik = open("85.txt", "r")
    dane = plik.readlines()
    plik.close()

    znaleziono = False
    for i in dane:
        isplit = i.split(";")
        if isplit[1] == nazwisko:
            znaleziono = True
            dane.remove(i)
            plik = open("85.txt", "w")
            plik.writelines(dane)
            print("Usunieto.")
            plik.close()

    if (znaleziono == False):
        print("Studenta nie odnaleziono ! ")


def Zmien(nazwisko, noweImie, noweNazwisko, nowaGrupa):
    plik = open("85.txt", "r")
    dane = plik.readlines()
    plik.close()

    znaleziono = False
    for i in dane:
        isplit = i.split(";")
        if isplit[1] == nazwisko:
            znaleziono = True
            if noweImie != "":
                isplit[0] = noweImie
            if noweNazwisko != "":
                isplit[1] = noweNazwisko
            if nowaGrupa != "":
                isplit[2] = nowaGrupa
                dane.append(f"{isplit[0]};{isplit[1]};{isplit[2]}")
                plik = open("85.txt", "w")
                plik.writelines(dane)
                plik.close()
                print("Pomyslnie zaktualizowano.")
                break
        else:
            dane.append(i)

    if (znaleziono == False):
        print("Studenta nie odnaleziono ! ")





while True:

    menu = input("D - dodaj\nP - pokaz\nU - usun\nZ - zmien\nQ - wyjscie").upper()

    if menu == "D":
        imie = input("Podaj imie studenta: ")
        nazwisko = input("Podaj nazwisko studenta: ")
        grupa = input("Podaj nazwe grupy: ")
        Dodaj(imie, nazwisko, grupa)

    elif menu == "P":
        Pokaz()

    elif menu == "U":
        nazwisko = input("Podaj nazwisko studenta: ")
        Usun(nazwisko)

    elif menu == "Z":
        nazwisko = input("Podaj nazwisko: ")
        noweImie = input("Podaj nowe imie: ")
        noweNazwisko = input("Podaj nowe nazwisko: ")
        nowaGrupa = input("Podaj nowa grupe: ")
        Zmien(nazwisko, noweImie, noweNazwisko, nowaGrupa)




