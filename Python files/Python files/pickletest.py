import pickle

print("odmarynowanie list i obiektu.")
f = open("dane.dat", "rb")
smak = pickle.load(f)
firma = pickle.load(f)
obj = pickle.load(f)
obj.hello()
f.close()

print(smak)
print(firma)
print(obj)