# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

def compress_rle(str):
    count = 1
    result = ''

    for i in range(len(str)- 1):
        if str[i] == str[i + 1]:
            count += 1
        else:
            result += f'{count}{str[i]}'
            count = 1

    if count > 1 or str[-2] != str[-1]:
        result += f'{count}{str[i]}'

    return result    

def decompress_rle(str):
    num = ''
    result = ''

    for i in range(len(str)):
        if str[i].isdigit():
            num += str[i]
        else:
            result += str[i] * int(num)
            num = ''

    return result

with open ('HW/HW5/file_3.txt', 'r') as file:
    data = file.read()

compress = compress_rle(data)
print(compress)

decompress = decompress_rle(compress)
print(decompress)

