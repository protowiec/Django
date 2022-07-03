#1 using get()
country_code = {"Poland": "+48", "Australia": "+10",
                "USA": "+00"}
print(country_code.get("Poland", "Not Found"))
print(country_code.get("Japan", "Not Found"))

#2 using setdefault()
country_code = {"Poland": "+48", "Australia": "+10",
                "USA": "+00"}
country_code.setdefault("Japan", "Not Present")
print(country_code["Poland"])
print(country_code["Japan"])

#3 using defaultdict
import collections
defd = collections.defaultdict(lambda : "Key not found")

defd["a"] = 1
defd["b"] = 2

print("The value assotiated with 'a' is: ", end="")
print(defd["a"])
print("The value assotiated with 'c' is: ", end="")
print(defd["c"])

