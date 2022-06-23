#1 method to zip two lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]

mapped = zip(name, roll_no)

print(set(mapped), "\n")

#2 method to zip with enumerate
names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age, "\n")

#3 method zip with dictionary
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
                               prices in zip(stocks, prices)}
print(new_dict, "\n")

#4 unzipping zipped lists
name = ["Maciej", "Agnieszka", "Amelia", "Adam"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

mapped = zip(name, roll_no, marks)
mapped = list(mapped)

print("The zipped result is : ", end="")
print(mapped)
print("\n")

name, roll_no, marks = zip(*mapped)
print("The unzipped result: \n", end="")

print("The name list is : ", end="")
print(name)

print("The roll_no list is : ", end="")
print(roll_no)

print("The marks list is : ", end="")
print(marks)

#5 method Practical Applications:
players = ["Maciej", "Piotrek", "Sebastian", "Mariusz", "Adam"]
scores = [100, 15, 17, 28, 43]
for pl, sc in zip(players, scores):
    print("Player : %s    Score : %d" % (pl,sc))

"""
The %s operator is put where the string is to be specified. 
The number of values you want to append to a string should be
equivalent to the number specified in parentheses after 
the % operator at the end of the string value

The %d operator is used as a placeholder to specify integer 
values, decimals or numbers. It allows us to print numbers 
within strings or other values. The %d operator is put where 
the integer is to be specified. Floating-point numbers are 
converted automatically to decimal values. 
"""
