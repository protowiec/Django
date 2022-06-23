class Koszyk:

    def __init__(self):
      self.zakupy = {}

    def dodajProdukt(self, produkt, ilosc):
        if(produkt in self.zakupy):
            dotycgczasowaIlosc = self.zakupy[produkt]
            nowaIlosc = dotycgczasowaIlosc + ilosc
            self.zakupy[produkt] = nowaIlosc


        #     self.zakupy[produkt] += ilosc
        else:
            self.zakupy[produkt] = ilosc

    def usunProdukt(self, produkt, ilosc):
        if(ilosc == self.zakupy[produkt]):
            self.zakupy.pop(produkt)
        elif(ilosc > self.zakupy[produkt]):
            print("Nieprawidlowa ilosc")
        elif(ilosc < self.zakupy[produkt]):
            self.zakupy[produkt] -= ilosc


sklep = {"chleb":2.50, "sok":1.80, "woda":2.80, "piwo":5.55}
koszyk = Koszyk()

while(True):

    menu = input("Witaj w sklepie !!!\nD-dodaj produkt, P-pokaz zawartosc koszyka, U-usun produkt, K-kasa/koniec").upper()

    if(menu == "D"):
        produkt = input("Dodaj produkt z oferty: ")
        if produkt in sklep:
            ilosc = int(input("Podaj ilosc produktu: "))
            koszyk.dodajProdukt(produkt, ilosc)

    elif (menu == "P"):
        for i in koszyk.zakupy:
            print(f"Produkt: {i} Ilosc: {koszyk.zakupy[i]}")

    elif (menu == "U"):
        produkt = input("Podaj nazwe produktu do usuniecia: ")
        if(produkt in koszyk.zakupy):
                ilosc = int(input("Podaj ilosc ktora chcesz usunac: "))
                koszyk.usunProdukt(produkt, ilosc)
                print("Produkt pomyslnie usuniety.")

    elif (menu == "K"):
        print("PARAGON")
        suma = 0
        for i in koszyk.zakupy:
            wartosc = koszyk.zakupy[i] * sklep[i]
            print(f"Produkt: {i} Ilosc: {koszyk.zakupy[i]} Cena: {sklep[i]} Wartosc: {wartosc}")
            suma += wartosc
        print(f"Razem do zaplaty: {suma}")
        break