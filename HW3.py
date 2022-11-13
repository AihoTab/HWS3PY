# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Fn = Fn+1 - Fn+2 | F-n = (-1)n+1Fn. || F 0 = 0, F 1 = 1, F n = F n-1 + F n-2, n ≥ 2

num = int(input())
fib = [0, 1]
for i in range(num-2):
    to_the_end = fib[-1]+fib[-2]
    to_the_start = (-1) ** (i+1)*to_the_end
    fib.append(to_the_end)
    fib.insert(0, to_the_start)
print(*fib)


# num = int(input())
# fib = ''
# f_1 = f_2 = 1
# for i in range(2, num):
#     f_1, f_2 = f_2, f_1 + f_2
#     #fib.append(f_1)
#     print(f_2, end=' ')
# for i in range(num):
#     f_1, f_2 = f_2, f_1 - f_2
#     fib.insert(0, f_1)
# print(fib)
