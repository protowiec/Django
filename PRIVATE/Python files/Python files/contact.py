class Contact:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def email(self): 
        return self.imie+"_"+self.nazwisko+"@firma.pl"

    def przedstawSie(self):
        return self.imie+" "+self.nazwisko