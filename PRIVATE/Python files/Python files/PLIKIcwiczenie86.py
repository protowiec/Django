import pickle

class Kontakt:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefony = []
        self.email = []

class KontaktController:

    def __init__(self):
        self.kontakty = []

    def dodajKontakt(self, imie, nazwisko):
        kontakt = Kontakt(imie, nazwisko)
        self.kontakty.append(kontakt)
        print("\nDodano kontakt\n")
        

    def usunKontakt(self, nazwisko):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                self.kontakty.remove(i)
                print("\nKontakt pomyslnie usuniety.\n")


    def dodajTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.telefony.append(telefon)  
                print("\nTelefon dodany.\n")
    

    def usunTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.telefony.remove(telefon)
                print("Pomyslnie usunieto telefon")

            break

        

    def dodajEmail(self):
        pass

    def usunEmail(self):
        pass

    def wyswietlKontakty(self, nazwisko):
        for i in self.kontakty:
            print()
            print(f"Imie: {i.imie}/ Nazwisko: {i.nazwisko}")
            print()


class App(KontaktController):

    def __init__(self):
        super().__init__()
        try:
            plik = open("86_3.dat", "rb")
            self.kontakty = pickle.load(plik)
            plik.close()
        except:
            plik = open("86_3.dat", "wb")
            pickle.dump([], plik)
            plik.close()

        self.menu()

    def menu(self):

        while(True):

            menu = input("1-dodaj kontakt\n2-pokaz kontakty\n3-usun kontakt"
                         "\n4-dodaj telefon\n5-usun telefon\n6-dodaj email\n7-usun email\n8-koniec: ")

            if(menu == "1"):
                imie = input("\nPodaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                self.dodajKontakt(imie, nazwisko)

            elif (menu == "2"):
                nazwisko = input("\nPodaj nazwisko: ")
                self.wyswietlKontakty(nazwisko)

            elif (menu == "3"):
                nazwisko = input("\nPodaj nazwisko: ")
                self.usunKontakt(nazwisko)

            elif (menu == "4"):
                nazwisko = input("\nPodaj nazwisko: ")
                telefon = input("Podaj nr telefonu:")
                self.dodajTelefon(nazwisko, telefon)
                
            elif (menu == "5"):
                nazwisko = input("\nPodaj nazwisko: ")
                telefon = input("Podaj nr telefonu:")
                self.usunTelefon(nazwisko, telefon)
                # pytania: nazwisko, telefon
                pass
            elif (menu == "6"):
                # pytania: nazwisko, email
                pass
            elif (menu == "7"):
                # pytania: nazwisko, email
                pass
            elif (menu == "8"):

                plik = open("86_3.dat", "wb")
                pickle.dump(self.kontakty, plik)
                plik.close()
                break

app = App()