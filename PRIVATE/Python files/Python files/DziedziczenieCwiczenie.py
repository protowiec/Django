

class Auto:
    def __init__(self, marka, model, kolor, silnik):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.silnik = silnik
    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, Kolor: {self.kolor}, Silnik: {self.silnik}"

ob = Auto("Mazda", 5, "Czarna", 2.5)
ob1 = Auto("Mazda", 6, "Czarna", 2.0)
ob2 = Auto("Mazda", "cx30", "Czarna", 1.5)
print(ob)
print(ob1)
print(ob2)