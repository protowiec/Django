#removing the second "e" from first word "geeks"

testString = "GeeksForGeeks"

newStr = testString[:2] + testString[3:]
print(newStr)