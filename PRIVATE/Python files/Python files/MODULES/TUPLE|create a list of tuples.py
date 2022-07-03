# lista z funkcja do potegi 3

# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple

list1 = [9, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified

res = [(val, pow(val, 3)) for val in list1]
print(res)