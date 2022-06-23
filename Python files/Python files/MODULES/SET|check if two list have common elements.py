#1 method using traversal
def Common(a, b):
    result = False
    for x in a:
        for y in b:
            if x == y:
                result = True
                return result
    return result

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(Common(a, b))

#2 method using set and property
def common(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set and b_set):
        return True
    else:
        return False

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common(a, b))

#3 method using set Intersection
def common(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return True
    return False

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common(a, b))
