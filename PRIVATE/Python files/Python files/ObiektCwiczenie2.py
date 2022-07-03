class Auto:

    def __init__(self, marka, model, cena, kolor, silnik): #parametr pola moze miec dowolna nazwe "silnik" może być "a"
        self.marka = marka
        self.model = model
        self.cena = cena
        self.kolor = kolor
        self.silnik = silnik
        self.predkosc = 0

    def przyspiesz(self):
        self.predkosc += 10

    def zwolnij(self):
        self.predkosc -= 10

ob1 = Auto("Lexus", "IS200T", "90K", "Czarny", "Benzyna")
ob2 = Auto("Alfa Romeo", "159", "30K", "Bialy", "Diesel")
ob3 = Auto("Mercedes", "Cclasse", "120K", "Srebrny", "Hybryda")

print(ob1.marka, ob1.model, ob1.cena, ob1.kolor, ob1.silnik, ob1.predkosc)
print(ob2.marka, ob2.model, ob2.cena, ob2.kolor, ob2.silnik, ob2.predkosc)
print(ob3.marka, ob3.model, ob3.cena, ob3.kolor, ob3.silnik, ob3.predkosc)

print("--------------------------------------------------------------------")

ob1.przyspiesz()
ob1.przyspiesz()
ob1.przyspiesz()
ob3.przyspiesz()

print(ob1.marka, ob1.model, ob1.cena, ob1.kolor, ob1.silnik, ob1.predkosc)
print(ob2.marka, ob2.model, ob2.cena, ob2.kolor, ob2.silnik, ob2.predkosc)
print(ob3.marka, ob3.model, ob3.cena, ob3.kolor, ob3.silnik, ob3.predkosc)