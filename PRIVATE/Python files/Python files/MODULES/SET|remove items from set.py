#1 method with pop(). Pop always removing lovest value.
def remove(sets):
    while sets:
        sets.pop()
        print(sets)

sets = set([12, 10, 13, 15, 8, 9])
remove(sets)

