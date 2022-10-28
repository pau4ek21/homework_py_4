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


# from random import randint
# import random
#
# k = int(input('Введите натуральную степень k: '))
# while k <= 0:
#     k = int(input('Введены не корректные данные! Введите натуральную степень k: '))
#
# result = [0 for i in range(k)]
# koef = random.sample(range(0, 101), k + 1)
# print(f'Рандомные коэффициенты: {koef}')
# for i in range(len(result)):
#     result[i] = f'{koef[i]}x^{k}'
#     k -= 1
# result.append(str(koef[-1]))
#
#
# print(f'До обработки: {result}')
# for elem in result:
#     if elem == 0:
#         result.remove(elem)
#     try:
#         ind_x = elem.find('x')
#         d = int(elem[:ind_x])
#     except AttributeError:
#         continue
#     if d == 0 or elem == '0':
#         result.remove(elem)
#     if '^1' in elem:
#         result.remove(elem)
# result.insert(-1, elem[:elem.find('^1')])
#
#
# print(f'После обработки: {result}')
# polynom = ''
# for i in range(len(result) - 1):
#     polynom += f'{result[i]} + '
# polynom += f'{result[-1]} = 0'
# print(polynom)
#
# with open('text.txt', 'w') as f:
#     f.write(polynom)
