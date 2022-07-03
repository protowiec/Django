# import matplotlib.pyplot as plt

plik = open("72_4.txt", "r", encoding= "utf8") #zaliczanie polskich liter

dane = plik.readlines()
while True:
    if "Warszawa" in dane:
        for i in dane:
            print(i)


