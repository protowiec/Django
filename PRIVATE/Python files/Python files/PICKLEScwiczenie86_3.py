import pickle

class Kontakt:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefony = []
        self.emaile = []

class KontaktKontroller:
    def __init__(self):
        self.kontakty = []


    def dodajKontakt(self, imie, nazwisko):
        kontakt = Kontakt(imie, nazwisko)
        self.kontakty.append(kontakt)
        print("Kontakt utworzony !\n")

    def usunKontakt(self, nazwisko):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                self.kontakty.remove(i)
        print("Kontakt usuniety !\n")

    def dodajTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.telefony.append(telefon)
        print("Dodano nowy nr telefonu !\n")

    def usunTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.telefony.remove(telefon)
        print("Telefon usuniety !\n")

    def dodajEmail(self, nazwisko, email):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.emaile.append(email)
        print("Dodano nowy adres email !\n")

    def usunEmail(self, nazwisko, email):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.emaile.remove(email)
        print("Adres email usuniety !\n")

    def pokazKontakty(self, nazwisko):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                print(f"Imie: {i.imie} Nazwisko: {i.nazwisko}\n")
                for j in i.telefony:
                    print(f"Telefon: {j}\n")
                for r in i.emaile:
                    print(f"Email: {r}\n")
            elif (i.nazwisko != nazwisko):
                print("Nie odnaleziono kontaktu !\n")

class App(KontaktKontroller):
    def __init__(self):
        super().__init__()

        try:
            plik = open("86_3.dat", "rb")
            self.kontakty = pickle.load(plik)
            plik.close()

        except:
            plik = open("86_3.dat", "wb")
            pickle.dump([], plik)
            #  niewiadoma lista powyzej
            plik.close()

        self.menu()

    def menu(self):

        while True:
            menu = input("1-dodaj kontakt\n 2-pokaz kontakty\n 3-usun kontakt\n "
                         "4-dodaj telefon\n 5-usun telefon\n 6-dodaj email\n 7-usun email\n 8-koniec: ")

            if menu == "1":
                imie = input("Podaj imie:\n")
                nazwisko = input("Podaj nazwisko:\n")
                self.dodajKontakt(imie, nazwisko)


            if menu == "2":
                nazwisko = input("Podaj nazwisko:\n")
                self.pokazKontakty(nazwisko)

            if menu == "3":
                nazwisko = input("Podaj nazwisko:\n")
                self.usunKontakt(nazwisko)

            if menu == "4":
                nazwisko = input("Podaj nazwisko dla nowgo numeru telefonu:\n")
                telefon = input("Podaj nowy nr telefonu:\n")
                self.dodajTelefon(nazwisko, telefon)

            if menu == "5":
                nazwisko = input("Podaj nazwisko:\n")
                telefon = input("Podaj telefon: \n")
                self.usunTelefon(nazwisko, telefon)

            if menu == "6":
                nazwisko = input("Podaj nazwisko by dodac email:\n")
                email = input("Podaj nowy email:\n")
                self.dodajEmail(nazwisko, email)

            if menu == "7":
                nazwisko = input("Podaj nazwisko:\n")
                email = input("Podaj email:\n")
                self.usunEmail(nazwisko, email)

            if menu == "8":
                plik = open("86_3.dat", "wb")
                pickle.dump(self.kontakty, plik)
                plik.close()
                break

app = App()

