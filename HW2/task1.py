# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число N: '))

result = []

for i in range(number):
    if i:
        temp_num = 1

        for j in range(i + 1):
            temp_num *= j + 1
    
        result.append(temp_num)
    else:
        result.append(i + 1)

print(result)

