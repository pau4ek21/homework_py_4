# # Вычислить число c заданной точностью d
# # Пример:
# # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#
# number = input('введите число: ')
# dexp = input('введите число до какого хотите округлить: ')
# while len(dexp) < len(number):
#     number = list(number)
#     del number[-1]
# print("".join(number))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# import math

# number=int(input('введите число: '))
# numbers_list = []
# for i in range(2, number + 1):
#     if number % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             numbers_list.append(i)
# print(numbers_list)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# numbers = list(input('введите числа через пробел: ').split())
# numbers_list = []
# for i in numbers:
#     if numbers.count(i) == 1:
#         numbers_list.append(i)
# print(numbers_list)

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


import random

some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
k = int(input('Введите натуральную степень k: '))
coef = [random.randint(0, 100) for _ in range(k + 1)]
print(coef)
with open('coef.txt', 'w', encoding='utf-8') as m:
    for i in range(len(coef)):
        if k - i != 1 and k - i != 0:
            m.write(f'{coef[i]}x{some_dict[k - i]} + ')
        elif k - i == 1:
            m.write(f'{coef[i]}x + ')
        elif k - i == 0:
            m.write(f'{coef[i]} = 0')