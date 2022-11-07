# Задача 1
#  Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list = [2, 3, 5, 9, 3, 2, 4, 2, 1.2, 4.3]
list2 = []
for i in range(len(list)):
    if i % 2 !=0:
        list2.append(list[i])
print(sum(list2))


# Задача 2.
#  Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def sum_numbers(num, resoult):
    if num[0] != num[-1]:
        for i in num:
            delete_numbers = num[0] * num[-1]
            num.pop(0)
            num.pop(-1)
            resoult.append(delete_numbers)
    else: num[0] == num[-1]
    delete_numbers = num[0] * num[-1]       
    resoult.append(delete_numbers)
    print(resoult)

sum_numbers([2, 3, 4, 5, 6], [])


# Задача 3. Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.

# *Пример:*


import math

def diserence_numbers (list): 
    maximum = list[0]
    minimum = list[0]
    num1 = 0
    num2 = 0
    for i in range(1, len(list)):
        if list[i] > maximum:
            maximum = list[i]
        if list[i] < minimum:
            minimum = list[i]
    num1 = math.modf(maximum) 
    num2 = math.modf(minimum)
    resoult = num1[0] - num2[0]
    
    print(round(-resoult,3))

diserence_numbers([1.1, 1.2, 3.1, 5, 10.01])


# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_in_binary (number):

    resoult = 0
    num = 1
    while number > 0:
        resoult = resoult + number % 2 * num
        num = num * 10
        number = number // 2
    print(resoult)

decimal_in_binary(45)