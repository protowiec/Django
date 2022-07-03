import random

def Znaki():
    znaki = ["+", "-", "*"]
    znak = random.choice(znaki)
    return znak

correct = 0
incorrect = 0
for i in range(10):
    a = Znaki()
    num = random.randint(1, 10)
    num1 = random.randint(1, 10)
    iq = [num, a, num1]
    Output = eval(' '.join(str(x) for x in iq))
    print(Output)
    wynik = int(input(f"Jaki jest wynik dzialania: {iq}"))

    if wynik == Output:
        print("jest ok\n")
        correct += 1
    else:
        print("ZLE!!\n")
        incorrect += 1

print(f"Ilosc dobrych odpowiedzi: {correct}")
print(f"Ilosc zlych odpowiedzi: {incorrect}")

