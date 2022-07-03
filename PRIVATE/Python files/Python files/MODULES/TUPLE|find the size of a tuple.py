import sys

Tuple1 = (22, "geeks", 123, "for", 22.3, "geeks")
Tuple2 = ("this", "is", "so", "funny")
Tuple3 = ((1, "lion"), (2, "elephant"), (3, "crocodile"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")
