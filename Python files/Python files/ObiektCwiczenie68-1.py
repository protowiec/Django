class Kontakt:

    def __init__(self, imie, nazwisko, email, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.telefon = telefon

listaKontaktow = []

while True:
    menu = input("D- dodaj, P- pokaz, U- usun, Z- zmien, K- koniec").upper()
    if(menu == "D"):
        imie = input("Podaj imie do kontaktu: ")
        nazwisko = input("Podaj nazwisko do kontaktu: ")
        email = input("Podaj email do kontaktu: ")
        telefon = input("Podaj telefon do kontaktu")

        kontakt = Kontakt(imie, nazwisko, email, telefon)
        listaKontaktow.append(kontakt)
        print("Pomyslnie dodano nowy kontakt")



    elif(menu == "P"):
        for i in listaKontaktow:
            print("Imie:", i.imie, "Nazwisko:", i.nazwisko, "Email:", i.email, "Telefon:", i.telefon)
    elif(menu == "U"):
         nazwisko = input("Podaj nazwisko kontaktu do usuniecia: ")
         znaleziono = False
         for i in listaKontaktow:
            if(i.nazwisko == nazwisko):
                znaleziono == True
                listaKontaktow.remove(i)
                print("Kontakt pomyslnie usuniety.")

         if(znaleziono == False):
             print("Nie znaleziono kontaktu.")

    elif(menu == "Z"):
        nazwisko = input("Podaj nazwisko kontaktu do zmiany: ")
        for i in listaKontaktow:
            if(i.nazwisko == nazwisko):
                a = input("Podaj nowe imie: ")
                b = input("Podaj nowe nazwisko: ")
                c = input("Podaj nowy email: ")
                d = input("Podaj nowy telefon: ")
                i.imie = a
                i.nazwisko = b
                i.email = c
                i.telefon = d
            elif(i.nazwisko != nazwisko):
                print("Nie ma takiego kontaktu.")
        print("Kontakt pomyslnie zaktualizowany")

    elif(menu == "K"):
        print("Koniec programu")
        break
    else:
        print("Nierozpoznana opcja menu")

