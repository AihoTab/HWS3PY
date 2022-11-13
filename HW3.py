# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input())
dvoich = ''
while num != 0:
    dvoich += str(num % 2)
    num //= 2
print(dvoich[::-1])
