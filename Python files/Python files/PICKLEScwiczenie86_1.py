import pickle

class Znajomi:
    def __init__(self):
        self.kontakty = {}

    def dodajKontakt(self,godnosc, nrtel):
        self.kontakty[godnosc] = nrtel
        cont = self.kontakty
        f = open("kontakty.dat", "wb")
        pickle.dump(cont, f)
        f.close()
        print("Kontakt utworzony.\n")

    def usunKontakt(self, godnosc):
        if godnosc in self.kontakty:
            self.kontakty.pop(godnosc)
            cont = self.kontakty
            f = open("kontakty.dat", "wb")
            pickle.dump(cont, f)
            f.close()
            print("Kontakt usuniety.\n")

    def pokazKontakt(self):
        f = open("kontakty.dat", "rb")
        cont = pickle.load(f)
        f.close()
        for i, j in cont.items():
            print("Nazwa kontaktu:", i, "Numer telefonu:", j)


kontakt = Znajomi()

while True:
    menu = input("D - dodaj kontakt\nU - usun kontakt\nP - pokaz kontakty\nK - koniec\n").upper()

    if menu == "D":
        godnosc = input("Podaj imie i nazwisko: ")
        nrtel = input("Podaj nr telefonu: ")
        kontakt.dodajKontakt(godnosc, nrtel)

    if menu == "U":
        godnosc = input("Podaj imie i nazwisko kontaktu do usuniecia:\n")
        kontakt.usunKontakt(godnosc)

    if menu == "P":
        kontakt.pokazKontakt()

    if menu == "K":
        break




