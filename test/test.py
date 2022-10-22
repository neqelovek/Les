#  Напишите программу, которая принимает на вход вещественное или целое число и
#   показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


# n = int(input("as"))

# c = n % 10
# n = n // 10
# b = n % 10
# a = n // 10

# print(a+b+c)



# array = []
# array_neg = []

# n = 8

# for i in range(n):
#     if i == 0:array.append(0)
#     elif i == 1:array.append(1)
#     else: array.append(array[-1] + array[-2])
# for j in range(n):
#     array_neg.append(array[1]*array[2])


# print(array)

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# def Negafibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = [0]
# user_number = int(input("Введите размер списка: "))
# for i in range(1, user_number + 1):
#     list.append(Fibonacci(i))
#     list.insert(0, Negafibonacci(i))
# print(list)

# num = int(input("Введите количество членов ряда Негафибоначчи: "))
# result =[1, 0, 1]
# while num!=1: 
#     k = (result[-1]+result[-2])
#     result.append(k)
#     result.insert(0, (-1)**(num+1)*k)
#     num-=1
# print(result)

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 )
#  с помощью математических формул нахождения корней квадратного уравнения

n = 1
m = 1

a = 3
b = 6


for i in range(100):
    # n = a*(i+1)
    # m = b *(m+1)
    # if n == m:
        print(i)
