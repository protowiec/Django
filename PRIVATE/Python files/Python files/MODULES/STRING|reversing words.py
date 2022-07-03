def reverse(stri):
    strList = stri.split()
    strList.reverse()
    stri = (" ".join(strList))
    return stri

string = "geeks quiz practice code"
print(reverse(string))
