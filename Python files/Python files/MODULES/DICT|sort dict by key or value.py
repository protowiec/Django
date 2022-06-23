#1 Displaying keys alphabetically:
def dictionary():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:\n")
    print("Keys are")

    for i in sorted(key_value.keys()):
        print(i, end = " ")

def main():
    dictionary()

if __name__ == "__main__":
    main()

#2 sorting the keys and values in alphabetical order using key
def dictionary():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("\nTask2:\nKeys and Values sorted in",
          "alphabetical order by the key ")

    for i in sorted(key_value):
        print((i, key_value[i]), end = " ")

def main():
    dictionary()

if __name__ == "__main__":
    main()

#3 sorting the keys and values in alphabetical using the value
def dictionary():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("\nTask3:\nKeys and Values sorted in",
          "alphabetical order by the value ")

    print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))

def main():
    dictionary()

if __name__ == "__main__":
    main()
