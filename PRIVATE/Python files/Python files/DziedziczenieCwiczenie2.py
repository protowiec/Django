class Pracownik:

    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontrakt = kontrakt
        self.pensja = pensja

    def __str__(self):
        return f"Imie: {self.imie}, Nazwisko: {self.nazwisko}, Kontrakt: {self.kontrakt}, Pensja: {self.pensja}"

class pracownikController:

    def __init__(self):
        self.listaPracownikow = []

    def dodajPracownika(self, imie, nazwisko, kontrakt = "staz", pensja = 1000):
        lista = Pracownik(imie, nazwisko, kontrakt, pensja)
        self.listaPracownikow.append(lista)


    def pokazPracownikow(self):
        for i in self.listaPracownikow:
            print(i)

    def usunPracownika(self, nazwisko):
        for i in self.listaPracownikow:
            if i in self.listaPracownikow:
                self.listaPracownikow.remove(i)
                print("Pracownik pomyslnie usuniety.")
                break

    def zmienKontrakt(self, nazwisko, pensja):
        for i in self.listaPracownikow:
            if i.nazwisko == nazwisko:
               i.pensja = pensja
               i.kontrakt = "etat"

class Firma(pracownikController):

    def __init__(self, nazwaFirmy):
        super().__init__()
        self.nazwaFirmy = nazwaFirmy
        self.menu()

    def menu(self):

        print(f"Witaj w firmie {self.nazwaFirmy}")
        while (True):

            menu = input("D-dodaj pracownika, P-pokaz pracownikow, U-usun pracownika, Z-zmien kontrakt pracownikowi, K-koniec").upper()

            if (menu == "D"):
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                kontrakt = input("Podaj kontrakt staz/etat: ")
                if(kontrakt == "etat"):
                    pensja = int(input("Podaj wysokosc pensji: "))
                    self.dodajPracownika(imie, nazwisko, kontrakt, pensja)
                elif(kontrakt == "staz"):
                    self.dodajPracownika(imie, nazwisko)
                else:
                    print("Podano bledny kontrakt.")

                print("Pomyslnie dodano informacje.")

            if(menu == "P"):
                print("Lista pracownikow: ")
                self.pokazPracownikow()

            if (menu == "U"):
                nazwisko = input("Podaj nazwisko pracownika: ")
                self.usunPracownika(nazwisko)

            elif (menu == "Z"):
                nazwisko = input("Podaj nazwisko do zmiany: ")
                pensja = input("Podaj pensje do zmiany: ")
                self.zmienKontrakt(nazwisko, pensja)

            elif (menu == "K"):
                print("Koniec programu")
                break

firma = Firma("Maciej Sp. z o.o.")