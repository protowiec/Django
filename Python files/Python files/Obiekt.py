class Samolot:                   #projekt- zawsze z wielkiej litery

    def __init__(self):          #KONSTRUKTOR
        self.nazwa = None
        self.pulap = 0
        self.iloscpas = 0

ob1 = Samolot()
ob1.nazwa = "F15"
ob1.pulap = 12345
ob1.iloscpas = 2

ob2 = Samolot()
ob2.nazwa = "Boeing757"
ob2.pulap = 2345
ob2.iloscpas = 200

print(ob1.nazwa, ob1.pulap, ob1.iloscpas)

