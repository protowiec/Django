#1 method
test_list = [[5, 8, 10],[2, 0, 9], [5, 4, 2], [2, 3, 9]]

dict = {test_list[0][0]: test_list[1], test_list[0][1]: test_list[2],
        test_list[0][2]: test_list[3]}
print(dict, "\n")

#2 method using loop
test_list = [[5, 8, 10],[2, 0, 9], [5, 4, 2], [2, 3, 9]]
print("The original list: " + str(test_list))

res = {test_list[0][ele]: test_list[ele + 1] for ele in range(len(test_list) - 1)}
print("The assigned Matrix: " + str(res))

