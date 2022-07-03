class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.lista_pacjentow = []

    def dodaj_pacjenta(self, pac):
        self.lista_pacjentow.append(pac)
        print(f"\nDodano pacjenta do przychodni {nazwa}.")

    def usun_pacjenta(self, id):
        for i in self.lista_pacjentow:
            if i.id == id:
                self.lista_pacjentow.remove(i)
        print("\nPacjent pomyslnie usuniety z przychodni.")

    def pokaz_pacjentow(self, nazwa):
        for i in self.lista_pacjentow:
            print(f"\nImie: {i.imie}/ Nazwisko: {i.nazwisko}/ ID: {i.id}")


class Pacjent:

    def __init__(self, imie, nazwisko, id):
        self.imie = imie
        self.nazwisko = nazwisko
        self.id = id
        self.lista_chorob = []

    def dodaj_chorobe(self, choroba):
        self.lista_chorob.append(choroba)
        print("\nPomyslnie dodano chorobe pacjentowi.")

    def pokaz_chorobe(self, id):
        for i in self.lista_chorob:
            print(f"\nImie: {imie}/ Nazwisko: {nazwisko}/ Dolegliwosc: {choroba}")

przychodnia = []
pacjent = []

# menu = input("\nWitamy w NFZ\nProsze dokonac wyboru:\n1- Przychodnia/ 2- Pacjent/ 3- Koniec: ")

while True:
    menu = input("\nWitamy w NFZ\nProsze dokonac wyboru:\n1- Przychodnia/ 2- Pacjent/ 0- Koniec: ")

    while menu == "1":
    
        menu1 = input("\n....Przychodnia....\nProsze dokonac wyboru:\n1- dodaj przychodnie\n2- usun przychodnie\n3- dodaj pacjenta do przychodni\n4- usun pacjenta z przychodni\n5- lista przychodni\n6- lista pacjentow w przychodni\n7- powrot do poprzedniego menu: ")

        if menu1 == "1":
            nazwa = input("\nPodaj nazwe przychodni ktora chcesz dodac: ")
            miasto = input("Podaj miasto w ktorym znajduje sie przychodnia: ")
            przych = Przychodnia(nazwa, miasto)
            przychodnia.append(przych)
            print("    \nPomyslnie dodano nowa przychodnie.")
                
        elif menu1 == "2":
            nazwa = input("\nPodaj nazwe przychodni ktora chcesz usunac: ")
            for i in przychodnia:
                if i.nazwa == nazwa:
                    przychodnia.remove(i)
                    print("    \nPrzychodnia usunieta.")                  
        
        elif menu1 == "3":
            imie = input("\nPodaj imie pacjenta: ")
            nazwisko = input("Podaj nazwisko pacjenta: ")
            id = input("Stworz nowe ID dla pacjenta: ")
            pac = Pacjent(imie, nazwisko, id)
            pacjent.append(pac)
            print("\nPomyslnie utworzono profil nowego pacjenta.\n")
            nazwa = input("Podaj nazwe przychodni do ktorej chcesz dodac nowego pacjenta: ")
            for i in przychodnia:
                if i.nazwa == nazwa:
                    i.dodaj_pacjenta(pac)                                           
                    
        elif menu1 == "4":
            nazwa = input("\nW celu usuniecia pacjenta, podaj nazwe szpitala w ktorym sie znajduje: ")
            for i in przychodnia:
                if i.nazwa == nazwa:
                    id = input("Podaj id pacjenta: ")
                    i.usun_pacjenta(id)

        elif menu1 == "5":
            print()
            for i in przychodnia:
                print(f"Nazwa przychodni: {i.nazwa}/ Miasto przychodni: {i.miasto}.")
                    

        elif menu1 == "6":
            nazwa = input("\nPodaj nazwe przychodni w celu wyswietlenia pacjentow: ")
            for i in przychodnia:
                if i.nazwa == nazwa:
                    i.pokaz_pacjentow(nazwa)

        elif menu1 == "7":
            print()
            break
                           

    while menu == "2":

        menu2 = input("\n....Panel pacjenta....\n1- dodaj chorobe pacjentowi\n2- lista chorob pacjenta\n3- powrot do poprzedniego menu: ")

        if menu2 == "1":
            id = input("\nPodaj ID pacjenta ktoremu chcesz przypisac chorobe: ")
            choroba = input("Wpisz chorobe na ktora cierpi pacjent: ")
            for i in pacjent:
                if i.id == id:
                    i.dodaj_chorobe(choroba)

        elif menu2 == "2":
            id = input("\nPodaj ID pacjenta by wyswietlic jego choroby: ")
            for i in pacjent:
                if i.id == id:
                    i.pokaz_chorobe(id)


        if menu2 == "3":
            print()
            break


    if menu == "0":
        print("\nDo zobaczenia w szpitalu ;).\n")
        break

                
                
    


                        
                    

                    

            

