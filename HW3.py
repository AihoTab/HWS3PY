# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

num = list(map(float, input().split()))
n_num = [round(i % 1, 2) for i in num if i % 1 != 0]
print(max(n_num) - min(n_num))


# num = [float(i) for i in input().split()]
# max_ost = num[0] - int(num[0])
# min_ost = num[0] - int(num[0])
# for i in num:
#     num - int(num)
#     if num > max_ost:
#         max_ost = num
#     elif num[i] < min_ost:
#         min_ost = num
# print(max_ost - min_ost)
