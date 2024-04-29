import random

digit_el = random.randint(3, 10)

my_list = [random.randint(1, 10) for _ in range(digit_el)]
print("список випадкових чисел :",  my_list)

second_list = [my_list[0], my_list[2], my_list[-2]]

print("список з 3 елементів початкового списку - першим, третім і другим з кінця:", second_list)