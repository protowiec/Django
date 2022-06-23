class Student:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodajOcene(self, ocena):
        self.oceny.append(ocena)

    def wypiszOceny(self):
        for i in self.oceny:
            print(i, end=" ")
        print()

    def policzSrednia(self):
        liczbaOcen = len(self.oceny)
        suma = 0
        for i in self.oceny:
            suma += i

        srednia = suma/liczbaOcen
        return srednia

listaStudentow = []

while(True):

    menu = input("D-dodaj studenta, P-pokaz studentów, U-usun studenta, O-dodaj ocene studentowi, "
                 "W-wypisz oceny studenta, S-srednia studenta, K-koniec").upper()

    if(menu == "D"):
        imie = input("Podaj imie do kontaktu: ")
        nazwisko = input("Podaj nazwisko do kontaktu: ")
        student = Student(imie, nazwisko)
        listaStudentow.append(student)
        print("Pomyslnie dodano nowy kontakt")

    elif(menu == "P"):
        for i in listaStudentow:
            print("Imie:", i.imie, "Nazwisko:", i.nazwisko)
    elif (menu == "U"):
        nazwisko = input("Podaj nazwisko kontaktu do usuniecia: ")
        znaleziono = False
        for i in listaStudentow:
            if (i.nazwisko == nazwisko):
                znaleziono == True
                listaStudentow.remove(i)
                print("Kontakt pomyslnie usuniety.")

            elif(znaleziono == False):
                print("Nie znaleziono kontaktu.")

    elif (menu == "O"):
        nazwisko = input("Podaj nazwisko dla oceny: ")
        for i in listaStudentow:
            if(i.nazwisko == nazwisko):
                ocena = int(input("Podaj ocene: "))
                i.dodajOcene(ocena)
                print("Ocena dodana pomyslnie")

    elif (menu == "W"):
        nazwisko = input("Podaj nazwisko studenta by zobaczyc oceny: ")
        for i in listaStudentow:
            if (i.nazwisko == nazwisko):
                i.wypiszOceny()

    elif (menu == "S"):
        nazwisko = input("Podaj nazwisko studenta by zobaczyc srednia z ocen: ")
        for i in listaStudentow:
            if (i.nazwisko == nazwisko):
                print(i.policzSrednia())

    elif (menu == "K"):
        print("Koniec programu")
        break
    else:
        print("Nierozpoznana opcja menu")
