# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

number = int(input('Введите кол-во элементов в списке: '))

list = []

for i in range(number):
    list.append(random.randint(0,9))
print(list)

result = []

for i in range(len(list)):
    while i < len(list) / 2 and number > len(list) / 2:
        number -= 1
        result.append(list[i]*list[number])
        i += 1
        
print(result)
