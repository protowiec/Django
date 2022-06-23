from datetime import datetime

day_num = "339"
print("The day number: " + str(day_num))

day_num.rjust(3 + len(day_num), "0")
year = "2020"
res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%m-%d-%Y")
print("Resolved date: " + str(res))
