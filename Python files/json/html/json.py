import requests

res = requests.get("https://api.chucknorris.io/jokes/categories")
x = (res.json())
print(x)

for i in x:
    print(i)

a = input("Choose category: ")

res = requests.get(f"https://api.chucknorris.io/jokes/random?category={a}")
x = (res.json())
txt = x["value"]
v = txt.replace("Chuck Norris", "Maciej Prot")
print(v)



