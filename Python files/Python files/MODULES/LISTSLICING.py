a = list(range(10))
print(a[1:])
print(a[-1])
print(a[-1::-1])
print(a[::-1])

a[0:10:3] = ["zero", "trzy", "szesc", "dziewiec"]
print(a)