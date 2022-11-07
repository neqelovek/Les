# задача 1. Задайте натуральное число N.
#           Напишите программу, которая составит список простых множителей числа N.
numbers = int(input('Введите число: '))

def multiplier_list(number):
    result = []
    num = 2
    while num * num <= number:
        if number % num == 0:
            result.append(num)
            number //= num
        else:
            num += 1
    if number > 1:
        result.append(number)
    return print("Ваше число " + str(numbers) + " состоит из множителей " + str(result))

multiplier_list(numbers)
