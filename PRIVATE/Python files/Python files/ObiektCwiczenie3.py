class Zawodnik:

    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga


    def bmi(self):
        wynik = self.waga / (self.wzrost**2)
        print(f"{self.imie} moje BMI: {wynik}")

ob1 = Zawodnik("Maciek", 1.72, 72, )
ob2 = Zawodnik("Agnieszka", 1.59, 45)

ob1.bmi()
ob2.bmi()

# METODA DRUGA : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Zawodnik:
#
#     def __init__(self, imie, wzrost, waga):
#         self.imie = imie
#         self.wzrost = wzrost
#         self.waga = waga
#
#
#     def bmi(self):
#         wynik = self.waga / (self.wzrost**2)
#         return (f"{self.imie} moje BMI: {wynik}")
#
# ob1 = Zawodnik("Maciek", 1.72, 72, )
# ob2 = Zawodnik("Agnieszka", 1.59, 45)
#
#
# print(ob1.imie, ob1.wzrost, ob1.waga, ob1.bmi())
#
