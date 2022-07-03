#drukuje jedynie parzyste slowa

def evenStr(string):
    string = string.split(" ")
    for i in string:
        if len(i)%2==0:
            print(i)

string = "This is a python language"

evenStr(string)
