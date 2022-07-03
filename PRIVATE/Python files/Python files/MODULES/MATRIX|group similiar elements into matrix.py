#1 using list comprehension + groupby()
from itertools import groupby

test_list = [1, 3, 4, 4, 2, 3]
print("The original list: " + str(test_list))

res = [list(val) for key, val in groupby(sorted(test_list))]
print("Matrix after grouping: " + str(res))

#2 using list comprehension + Counter()
from collections import Counter
test_list = [1, 3, 4, 4, 2, 3]
print("The original list: " + str(test_list))

temp = Counter(test_list)
res = [[key] * val for key, val in temp.items()]
print("Matrix after grouping: " + str(res))
