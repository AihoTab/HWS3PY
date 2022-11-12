# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

num = [8, 7, 2, 14, 1, 3, 21, 41, 9, 6]
print(num)
summ = 0
for i in range(1, len(num), 2):
    summ += num[i]
print(summ)


# num = [8, 7, 2, 14, 1, 3, 21, 41, 9, 6]
# print(num)
# summ = 0
# for i in range(1, len(num)):
#     if i % 2 != 0:
#         summ += num[i]
# print(summ)
