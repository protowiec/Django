#1 method simple
def GFG(name, num):
    print("Hello from", name + ", " + num)

GFG("geeks for geeks", "25")

#2 method variable function arguments
def GFG(name, num="25"):
    print("hello from", name + ", " + num)

GFG("gfg")
GFG("gfg", "26")

#3 method concatenate strings
def GFG(name, num):
    print("hello from " + str(name) + ", " + str(num))

GFG("gfg", "25")

#4 method using the f-string formatting
def GFG(name, num):
    print(f"hello from {name} , {num}")

GFG("gfg", "25")

