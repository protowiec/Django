import unittest
from contact import *

class testContact(unittest.TestCase):

    contact1 = Contact("Adam", "Nowak")
    contact2 = Contact("Tomasz", "Kowalski")

    def test_email(self):
        wynik1 = self.contact1.email()
        wynik2 = self.contact2.email()

        self.assertEqual(wynik1, "Adam_Nowak@firma.pl")
        self.assertEqual(wynik2, "Tomasz_Kowalski@firma.pl")

    def test_przedstawSie(self):
        wynik1 = self.contact1.przedstawSie()
        wynik2 = self.contact2.przedstawSie()

        self.assertEqual(wynik1, "Adam Nowak")
        self.assertEqual(wynik2, "Tomasz Kowalski")