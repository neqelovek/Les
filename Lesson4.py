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


def non_repeating_numbers(sequence_numbers):
    resoult = []

    for number in sequence_numbers:
        if number in resoult:
            continue
        else:
            resoult.append(number)
    return print(resoult)

non_repeating_numbers([9, 2, 2, 3, 4, 5, 5, 2, 6, 7, 1, 9])




