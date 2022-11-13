# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from math import ceil
num = [int(i) for i in input(). split()]
for i in range(ceil(len(num)/2)):
    print(num[i]*num[-i-1])

# num = [int(i) for i in input(). split()]
# print(type(num))
# for i in range(0, len(num) / 2+1):
#     prod = num[i] * num[len(num) - i - 1]
# print(prod)
