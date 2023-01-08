# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

n = int(input('Введите размер списка: '))
list = []

for i in range(n):
    f = uniform(0, 9)
    list.append(round(f, 2))

print(list)

min = 1
max = 0
for i in range(len(list)):
    current = round(list[i] - int(list[i]),2)
    if current < min:
        min = current
    else:
        if current > max:
            max = current

print(round((max - min),2))
        

