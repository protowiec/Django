class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super(). __init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system

class Szkolenia(Oprogramowanie):
    def __init__(self,nazwa, cena, jezyk, system, termin):
        super(). __init__(nazwa, cena, jezyk, system)
        self.termin = termin

ob = Szkolenia("Szkolenie Python", 100, "Python", "Windows", "2021-10-11")

print(ob.nazwa, ob.cena, ob.jezyk, ob.system, ob.termin)