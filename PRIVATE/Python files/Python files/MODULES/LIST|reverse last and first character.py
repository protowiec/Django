def swapList(list):

    a = list.pop()
    b = list.pop(0)
    list.insert(0, a)
    list.insert(4, b)
    return list

newList = [1, 2, 3, 4, 5]

print(swapList(newList))