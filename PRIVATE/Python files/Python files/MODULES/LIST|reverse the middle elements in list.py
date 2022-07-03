def swapList(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


pos1, pos2 = 0, 2
list = [23, 65, 19, 90]

print(swapList(list, pos1, pos2))
