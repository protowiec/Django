#1 method:
set1 = set("GeEks")

for i in set1:
    print(i)

#2 method: Iterating over a set using enumerated for loop:
set2 = set("GeEks")

for id, i in enumerate(set2):
    print(id, i)

#3 method: ... using comprehension and list constructor/initializer
set3 = set("GeEks")

com = list(val for val in set3)
print(*com)