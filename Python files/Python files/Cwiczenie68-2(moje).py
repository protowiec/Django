class Student:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    
    def wypisz_oceny(self):
        for i in self.oceny:
            print(i, end = " ")
        print()


    def policz_srednia(self):
            a = sum(self.oceny)
            b = len(self.oceny)
            c = a / b
            print(c)

lista_studentow = []

while True:

    menu = input("D - dodaj studenta/ P- pokaz studenta/ U- usun studenta/ O- dodaj ocene studentowi/ W- wypisz oceny studenta/ S- srednia z ocen studenta").upper()

    if menu == "D":
        imie = input("Podaj imie studenta: ")
        nazwisko = input("Podaj nazwisko studenta: ")
        student = Student(imie, nazwisko)
        lista_studentow.append(student)
        print("Student pomyslnie dodany do listy.")

    elif menu == "P":
        for i in lista_studentow:
            print("Imie:", i.imie, "/ Nazwisko:", i.nazwisko, "/ Oceny:", i.oceny)

    elif menu == "U":
        nazwisko = input("Podaj nazwisko studenta ktorego chcesz usunac z listy: ")
        for i in lista_studentow:
            if i.nazwisko == nazwisko:
                lista_studentow.remove(i)
                print("Student pomyslnie usuniety z listy.")
            elif i.nazwisko != nazwisko:
                print("Nie odnaleziono studenta o takim nazwisku.")

    elif menu == "O":
        nazwisko = input("Podaj nazwisko studenta ktoremu chcesz wystawic ocene: ")
        for i in lista_studentow:
            if i.nazwisko == nazwisko:
                ocena = int(input("Wpisz ocene studentowi: "))
                i.dodaj_ocene(ocena)
                print("Ocena pomyslnie dodana.")
            elif i.nazwisko != nazwisko:
                print("Nie odnaleziono studenta o takim nazwisku.")
                

    elif menu == "W":
        nazwisko = input("Podaj nazwisko studenta: ")
        for i in lista_studentow:
            if i.nazwisko == nazwisko:
                i.wypisz_oceny()
            elif i.nazwisko != nazwisko:
                print("Nie odnaleziono studenta o takim nazwisku.")


    elif menu == "S":
        nazwisko = input("Podaj nazwisko studenta by wyliczyc jego srednia z ocen: ")
        for i in lista_studentow:
            if i.nazwisko == nazwisko:
                i.policz_srednia()
    else:
        print("Nierozpoznano wyboru.")
        

   