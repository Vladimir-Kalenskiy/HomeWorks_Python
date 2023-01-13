# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

def Prime_factor(num):
    num = abs(num)
    i = 2
    factors = []

    while i * i <= num:
        if num % i:
            i += 1

        else:
            num //= i
            factors.append(i)

    if num > 1:
        factors.append(num)

    return factors

num1 = int(input('Введите натуральное число N: '))
new_num = Prime_factor(num1)
print('Список простых множителей числа N:')
print(num1, '=', ' * '.join(map(str, new_num)))