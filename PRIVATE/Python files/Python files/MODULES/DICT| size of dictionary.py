#1 method:
import sys

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

print("Size of dic1: " + str(sys.getsizeof(dic1)))
print("Size of dic2: " + str(sys.getsizeof(dic2)))
print("Size of dic3: " + str(sys.getsizeof(dic3)))

#2 method:
ic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

print("Size of dic1: " + str(dic1.__sizeof__()) + "bytes")
print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")
print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")