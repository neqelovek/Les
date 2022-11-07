# задача 1. Задайте натуральное число N.
#           Напишите программу, которая составит список простых множителей числа N.

# numbers = int(input('Введите число: '))

# def multiplier_list(number):
#     result = []
#     num = 2
#     while num * num <= number:
#         if number % num == 0:
#             result.append(num)
#             number //= num
#         else:
#             num += 1
#     if number > 1:
#         result.append(number)
#     return print("Ваше число " + str(numbers) + " состоит из множителей " + str(result))

# multiplier_list(numbers)



# задача 2 . Задайте последовательность чисел. Напишите программу,
#            которая выведет список неповторяющихся элементов исходной последовательности.


# def non_repeating_numbers(sequence_numbers):
#     resoult = []

#     for number in sequence_numbers:
#         if number in resoult:
#             continue
#         else:
#             resoult.append(number)
#     return print(resoult)

# non_repeating_numbers([9, 2, 2, 3, 4, 5, 5, 2, 6, 7, 1, 9])


# задача 3. Задана натуральная степень k. 
#            Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#            многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

k = 2

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c \
    in itertools.zip_longest(ratios, var, range(k, 1, -1),fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('Polynomial.txt', 'w') as data:
    data.write(polynom1)

