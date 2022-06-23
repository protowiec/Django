a = [1, 2, [3, 4]]
b = a.copy()

print(id(a))
print(id(b))

print(id(a[2]))
print(id(b[2]))

# index of copied list are different but list inside the list have the same index number

