test_tup = (5, 20, 3, 7, 6, 8)

K = 2

#sorting tuple:
test_tup = list(test_tup)
temp = sorted(test_tup)
print(temp)

#removing K elements:
res = tuple(temp[:K] + temp[-K:])
print(res)
