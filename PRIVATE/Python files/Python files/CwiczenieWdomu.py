class Koszyk:

    def __init__(self):
        self.zakupy = {}

    def dodaj_produkt(self, produkt, ilosc):
        if produkt in self.zakupy:
            dotychczasowa_ilosc = self.zakupy[produkt]
            nowa_ilosc = dotychczasowa_ilosc + ilosc
            self.zakupy[produkt] = nowa_ilosc
        else:
            self.zakupy[produkt] = ilosc

        print("Produkt pomyslnie dodany do koszyka.")
        
    def usun_produkt(self, produkt, ilosc):
        if ilosc > self.zakupy[produkt]:
            print("Podana zbyt duza ilosc.")
        elif ilosc == self.zakupy[produkt]:
            self.zakupy.pop(produkt)   
        elif ilosc < self.zakupy[produkt]:
            dotychczasowa_ilosc = self.zakupy[produkt]
            nowa_ilosc = dotychczasowa_ilosc - ilosc
            self.zakupy[produkt] = nowa_ilosc

        
            

sklep = {"chleb":3.5, "sok":6.0, "woda":1.80, "cukier":4.25}
koszyk = Koszyk()

while True:
    
    menu = input("Witaj w sklepie!! \nD- dodaj produkt / U- usun produkt / P- pokaz koszyk / K- koniec zakupow: ").upper()
    
    if(menu == "D"):
        print("K- wyjscie z koszyka.")
        while True:
            produkt = input("Jaki produkt chcesz kupic?: ")
            if produkt in sklep:
                ilosc = int(input("Podaj ilosc jaka chcesz kupic: "))
                koszyk.dodaj_produkt(produkt, ilosc)
            elif produkt == "K":
                print("Skonczyles dodawac produkty do koszyka.")
                break
            

    elif(menu == "P"):
        for i in koszyk.zakupy:
            print(f"Produkt: {i}, Ilosc: {koszyk.zakupy[i]}")

    elif(menu == "U"):
        produkt = input("Jaki produkt chcesz usunac z koszyka? ")
        if produkt in koszyk.zakupy:
            ilosc = int(input("Podaj ilosc do usuniecia: "))
            koszyk.usun_produkt(produkt, ilosc)
            print("Produkt pomyslnie usuniety z koszyka.")


    elif(menu == "K"):
        print("PARAGON")
        suma = 0
        for i in koszyk.zakupy:
            wartosc = koszyk.zakupy[i] * sklep[i]
            print(f"Produkt: {i} Ilosc: {koszyk.zakupy[i]} Cena: {sklep[i]} Wartosc: {wartosc}")
            suma += wartosc
        print(f"Razem do zaplacenia: {suma}")
        break



