from tkinter import *
 
kontakty = []
 
class Kontakt:

    def  __init__(self,  imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

def dodajKontakt():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email = entry_email.get()

    kontakt = Kontakt(imie, nazwisko, telefon, email)
    kontakty.append(kontakt)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)
    entry_imie.focus()

    listaKontaktow()
 
def listaKontaktow():
    listbox_listaKontaktow.delete(0, END)
    for index, value in enumerate(kontakty):
        listbox_listaKontaktow.insert(index, value.imie+" "+value.nazwisko)

def usunKontakt():
    index = listbox_listaKontaktow.index(ACTIVE) 
    kontakty.pop(index)
    listaKontaktow()        

def pokazSzczegoly():
    index = listbox_listaKontaktow.index(ACTIVE)
    label_szczegolyImieValue.config(text = kontakty[index].imie)
    label_szczegolyNazwiskoValue.config(text= kontakty[index].nazwisko)
    label_szczegolyTelefonValue.config(text= kontakty[index].telefon)
    label_szczegolyEmailValue.config(text= kontakty[index].email)

def edytujKontakt():
    index = listbox_listaKontaktow.index(ACTIVE)
    imie = kontakty[index].imie
    nazwisko = kontakty[index].imie
    telefon = kontakty[index].imie
    email = kontakty[index].imie

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)

    entry_imie.insert(0, imie)
    entry_nazwisko.insert(0, nazwisko)
    entry_telefon.insert(0, telefon)
    entry_email.insert(0, email)

    button_dodajKontakt.config(text= "Zmien kontakt", command= zmienKontakt)

def zmienKontakt():
    index = listbox_listaKontaktow.index(ACTIVE)

    kontakty[index].imie = entry_imie.get()
    kontakty[index].nazwisko = entry_nazwisko.get()
    kontakty[index].telefon = entry_telefon.get()
    kontakty[index].email = entry_email.get()


    listaKontaktow()

    button_dodajKontakt.config(text= "Dodaj kontakt", command= dodajKontakt)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)
    entry_imie.focus()


root = Tk()
 
root.title("Ksiazka telefoniczna")
root.geometry("800x300")
 
def test(liczba):
    print(liczba)
 
 
 
appLeft = Frame(root)
appRight = Frame(root)
appBottom = Frame(root)
 
appLeft.grid(row=0, column=0, sticky=N, pady=20, padx=20)
appRight.grid(row=0, column=1, pady=20)
appBottom.grid(row=1, column=0, columnspan=2, sticky=W, padx=20)
 
# appLeft
 
label_listaKontaktow = Label(appLeft, text="Lista kontaktow")
listbox_listaKontaktow = Listbox(appLeft, width=20, height=7)
button_pokazSzczegoly = Button(appLeft, text="Pokaz szczegoly kontaktu", command = pokazSzczegoly)
button_usunKontakt = Button(appLeft, text="Usun kontakt", command= usunKontakt)
button_edytujKontakt = Button(appLeft, text="Edytuj kontakt", command= edytujKontakt)
 
label_listaKontaktow.grid(row=0, column=0, columnspan=3)
listbox_listaKontaktow.grid(row=1, column=0, columnspan=3)
button_pokazSzczegoly.grid(row=2, column=0)
button_usunKontakt.grid(row=2, column=1)
button_edytujKontakt.grid(row=2, column=2)
 
# appRight
 
label_nowyKontakt = Label(appRight, text="Nowy  Kontakt")
label_imie = Label(appRight, text="Imie")
label_nazwisko = Label(appRight, text="Nazwisko")
label_telefon = Label(appRight, text="Telefon")
label_email = Label(appRight, text="Email")
entry_imie = Entry(appRight)
entry_nazwisko = Entry(appRight, width=30)
entry_telefon = Entry(appRight)
entry_email = Entry(appRight)
#wywolujemy funkcje normalnie, ktora nie ma paramaetrow
# button_dodajKontakt = Button(appRight, text="Dodaj kontakt", command=test)
#przekazujemy parametr do funkcji
button_dodajKontakt = Button(appRight, text="Dodaj kontakt", command= dodajKontakt)
 
label_nowyKontakt.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_telefon.grid(row=3, column=0, sticky=W)
label_email.grid(row=4, column=0, sticky=W)
entry_imie.grid(row=1, column=1, sticky=W)
entry_nazwisko.grid(row=2, column=1, sticky=W)
entry_telefon.grid(row=3, column=1, sticky=W)
entry_email.grid(row=4, column=1, sticky=W)
button_dodajKontakt.grid(row=5, column=0, columnspan=2)
 
# appBottom
 
label_szczegolyKontaktu = Label(appBottom, text="Szczegoly kontaktu")
label_szczegolyImie = Label(appBottom, text="Imie")
label_szczegolyImieValue = Label(appBottom, text="...", width=10)
label_szczegolyNazwisko = Label(appBottom, text="Nazwisko")
label_szczegolyNazwiskoValue = Label(appBottom, text="...", width=10)
label_szczegolyTelefon = Label(appBottom, text="Telefon")
label_szczegolyTelefonValue = Label(appBottom, text="...", width=10)
label_szczegolyEmail = Label(appBottom, text="Email")
label_szczegolyEmailValue = Label(appBottom, text="...", width=10)
 
label_szczegolyKontaktu.grid(row=0, column=0, columnspan=8, sticky=W)
label_szczegolyImie.grid(row=1, column=0, sticky=W)
label_szczegolyImieValue.grid(row=1, column=1, sticky=W)
label_szczegolyNazwisko.grid(row=1, column=2, sticky=W)
label_szczegolyNazwiskoValue.grid(row=1, column=3, sticky=W)
label_szczegolyTelefon.grid(row=1, column=4, sticky=W)
label_szczegolyTelefonValue.grid(row=1, column=5, sticky=W)
label_szczegolyEmail.grid(row=1, column=6, sticky=W)
label_szczegolyEmailValue.grid(row=1, column=7, sticky=W)
 
root.mainloop()
 