# Задайте последовательность чисел. Напишите программу, которая выведет список элементов, 
# которые не имели повторов в исходной последовательности.

# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

from random import randint

def get_list_unique(list):
  
    new_list = []

    for number in list:
        if list.count(number) > 1:
            continue

        new_list.append(number)

    return new_list

number_els = int(input('Введите кол-во элементов: '))
max_number = int(input('введите максимальное число элемента: '))

list1 = [randint(0, max_number) for _ in range(number_els)]

print(list1)
print('Список уникальных элементов.')
print(get_list_unique(list1))