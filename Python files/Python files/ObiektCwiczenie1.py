class Kurs:
    def __init__(self, nazwa, termin, miasto):
        self.nazwa = nazwa
        self.termin = termin
        self.miasto = miasto
        self.uczestnicy = []



class Kursant:
    def __init__(self, imie, nazwisko, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon


listaKursow = []

while(True):

    print("System dla firmy szkoleniowej")
    menu = int(input("1-Dodaj kurs, 2-Wyświetl kursy, 3-Usuń kurs, 4-Dodaj kursanta do kursu, 5-Wyświetl kurs wraz z kursantami, "
                 "6-Usuń kursanta z kursu, 7-koniec"))

    if(menu == 1):
        nazwa = input("Podaj nazwe kursu: ")
        termin = input("Podaj termin kursu: ")
        miasto = input("Podaj miasto kursu: ")

        kurs = Kurs(nazwa, termin, miasto)
        listaKursow.append(kurs)
        print("Pomyslnie dodano nowy kurs")

    elif(menu == 2):
        for i in listaKursow:
            print("Nazwa kursu:", i.nazwa, "Termin kursu:", i.termin, "Miasto kursu:", i.miasto)

    elif (menu == 3):
        nazwisko = input("Podaj nazwe kursu: ")
        for i in listaKursow:
            if (i.nazwa == nazwa):
                listaKursow.remove(i)
                print("Kurs pomyslnie usuniety.")

    elif (menu == 4):
        nazwaKursu = input("Podaj nazwe kursu: ")
        imie = input("Podaj imie kursanta: ")
        nazwisko = input("Podaj nazwisko kursanta: ")
        telefon = input("Podaj nr telefonu kursanta: ")

        kursant = Kursant(imie, nazwisko, telefon)

        for i in listaKursow:
            if(i.nazwa == nazwaKursu):
                i.uczestnicy.append(kursant)

    elif (menu == 5):
        nazwaKusrsu = input("Podaj nazwe kursu: ")
        for i in listaKursow:
            if(i.nazwa == nazwaKursu):
                print("Nazwa kursu:", i.nazwa, "Termin kursu:", i.termin, "Miasto kursu:", i.miasto,)
                for j in i.uczestnicy:
                        print("Uczestnicy:", j.imie, j.nazwisko)

    elif (menu == 6):
            nazwaKursu = input("Podaj nazwe kursu: ")
            for i in listaKursow:
                for j in i.uczestnicy:
                    input("Podaj nazwisko kursanta: ")
                    if(j in i.uczestnicy):
                        i.uczestnicy.remove(j)

    #     # inputy: nazwaKursu, nazwisko
    #     pass
    # elif (menu == 7):
    #     print("koniec")
    #     break
    # else:
    #     print("Nierozpoznana opcja menu")
    #



