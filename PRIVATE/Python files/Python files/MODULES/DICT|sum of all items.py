#1 method:
def sumDict(dict1):
    dict2 = dict1.values()
    print(sum(dict2))


dict1 = {"a": 100, "b": 200, "c": 300}
sumDict(dict1)

#2 method:
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#3 method:
def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))