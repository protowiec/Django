import pickle

print("Marynowanie list i obiektu.")

class Auto:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def hello(self):
        print("hello")

    def __str__(self):
        return self.marka + " " + self.model

obj = Auto("VW", "PASSAT")

smak = ["lagodny", "pikantny", "kwaszony"]
firma = ["Dawtona", "Klimex", "Vortumnus"]

f = open("dane.dat", "wb")

pickle.dump(smak, f)
pickle.dump(firma, f)
pickle.dump(obj, f)
f.close()

print("Odmarynowanie list i obiektu")

f = open("dane.dat", "rb")
smak = pickle.load(f)
firma = pickle.load(f)
obj = pickle.load(f)
obj.hello()
f.close()

print(smak)
print(firma)
print(obj)