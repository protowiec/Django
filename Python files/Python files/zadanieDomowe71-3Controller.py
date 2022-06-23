class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.listaPacjentow = []

class Pacjent:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaChorob = []

    def __str__(self):
        return f"Imię: {self.imie} Nazwisko: {self.nazwisko}"

class PrzychodniaController:

    def __init__(self):
        self.listaPrzychodni = []

    def dodajPrzychodnie(self, nazwa, miasto):
        przychodnia = Przychodnia(nazwa, miasto)
        self.listaPrzychodni.append(przychodnia)
        print("Przychodnia dodana pomyslnie")

    def usunPrzychodnie(self, nazwa):
        for i in self.listaPrzychodni:
            if(i.nazwa == nazwa):
                self.listaPrzychodni.remove(i)
                print("Przychodnia pomyslnie usunieta")
                break

    def dodajPacjentaDoPrzychodni(self, nazwa, imie, nazwisko):
        for i in self.listaPrzychodni:
            if(i.nazwa == nazwa):
                pacjent = Pacjent(imie, nazwisko)
                i.listaPacjentow.append(pacjent)
                print("Pacjent pomyslnie dodany do przychodni")
                break

    def usunPacjentaZPrzychodni(self, nazwa, nazwisko):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if(j.nazwisko == nazwisko):
                        i.listaPacjentow.remove(j)
                        print("Pacjent usunieto pacjenta z przychodni")
                        break

    def pokazPrzychodne(self):
        for i in self.listaPrzychodni:
            print(f"Nazwa: {i.nazwa} Miasto: {i.miasto}")

    def listaPacjentowWPrzychodni(self, nazwa):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    print(j)

    def dodajChorobePacjentowi(self, nazwa, nazwisko, choroba):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if (j.nazwisko == nazwisko):
                        j.listaChorob.append(choroba)
                        print("Chorba zostala dodana")
                        break

    def listaChorobPacjenta(self, nazwa, nazwisko):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if (j.nazwisko == nazwisko):
                        for k in j.listaChorob:
                            print(k)

    def sprawdzPrzychodnie(self, nazwa):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                return True

        return False

    def sprawdzPacjenta(self, nazwa, nazwisko):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if(j.nazwisko == nazwisko):
                        return True

        return False


class Nfz(PrzychodniaController):

    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):

        while(True):

            menu = input("1-Przychodnie, 2-Pacjenci, 3-Koniec")

            if(menu == "1"):

                while(True):
                    submenu = input("1-dodaj przychodnie, 2-usun przychodnie, 3-dodaj pacjenta do przychodni, "
                                "\n4-usun pacjenta z przychodnia, 5-lista przychodnia, 6-lista pacjentow w przychodni, 7-koniec")

                    if(submenu == "1"):

                        nazwa = input("Podaj nazwe:")
                        miasto = input("Podaj miasto:")
                        self.dodajPrzychodnie(nazwa, miasto)

                    elif (submenu == "2"):
                        nazwa = input("Podaj nazwe:")
                        if(self.sprawdzPrzychodnie(nazwa) == True):
                            self.usunPrzychodnie(nazwa)
                        else:
                            print("Bledna nazwa przychodni")

                    elif (submenu == "3"):
                        nazwa = input("Podaj nazwe:")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            imie = input("Podaj imie pacjenta")
                            nazwisko = input("Podaj nazwisko pacjenta")
                            self.dodajPacjentaDoPrzychodni(nazwa, imie, nazwisko)
                        else:
                            print("Bledna nazwa przychodni")

                    elif (submenu == "4"):
                        nazwa = input("Podaj nazwe:")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            nazwisko = input("Podaj nazwisko pacjenta")
                            if(self.sprawdzPacjenta(nazwisko) == True):
                                self.usunPacjentaZPrzychodni(nazwa, nazwisko)
                            else:
                                print("Brak pacjenta")
                        else:
                            print("Bledna nazwa przychodni")

                    elif (submenu == "5"):
                        self.pokazPrzychodne()

                    elif (submenu == "6"):
                        nazwa = input("Podaj nazwe:")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            self.listaPacjentowWPrzychodni(nazwa)
                        else:
                            print("Bledna nazwa przychodni")

                    elif (submenu == "7"):
                        break
                    else:
                        break


            elif(menu == "2"):

                while (True):
                    submenu = input("1-dodaj chorobe pacjentowi, 2-lista chorob pacjenta, 3-koniec")

                    if (submenu == "1"):
                        nazwa = input("Podaj nazwe:")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            nazwisko = input("Podaj nazwisko pacjenta:")
                            if(self.sprawdzPacjenta(nazwa, nazwisko) == True):
                                choroba = input("Podaj chorobe:")
                                self.dodajChorobePacjentowi(nazwa, nazwisko, choroba)
                            else:
                                print("Brak pacjenta w przychodnia")
                        else:
                            print("Bledna nazwa przychodni")

                    elif (submenu == "2"):
                        nazwa = input("Podaj nazwe:")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            nazwisko = input("Podaj nazwisko pacjenta:")
                            if (self.sprawdzPacjenta(nazwa, nazwisko) == True):
                                self.listaChorobPacjenta(nazwa, nazwisko)
                            else:
                                print("Brak pacjenta w przychodnia")
                        else:
                            print("Bledna nazwa przychodni")

                    elif (submenu == "3"):
                        break


            elif(menu == "3"):
                print("koniec")
                break

            else:
                print("Nierozpoznana opcja menu")


ob = Nfz()