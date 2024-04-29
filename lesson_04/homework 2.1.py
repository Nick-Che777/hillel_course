my_list = [0, 34, True, 0, 7, 0, 12]

for el in my_list:
    if el == 0:
        my_list.remove(0)
        my_list.append(0)
print(my_list)