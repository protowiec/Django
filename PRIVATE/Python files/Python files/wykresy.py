import matplotlib.pyplot as plt

dane = [10, 20, 200, 40 ,50, 10, 70, 999, 90]
dane2 = [5, 600, 200, 34, 100, 50, 1000, 30, 1, 200]
plt.plot(dane2, label= "Dane2")
plt.plot(dane, label = "Dane")
plt.grid(color="lightblue", linestyle="-.", linewidth=0.6)
plt.legend()
# plt.savefig("output.png", dpi=300)     zapisywanie do pliku graficznego
plt.show()

