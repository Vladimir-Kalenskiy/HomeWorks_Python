from methods import add, sub, div, mult

def parseable_data(data):          # Получение уравнения в виде строки и преобразование в список
    math_equation = []             # Пример: 1+2*5 -> ['1', '+', '2', '*', '5']
    math_elem = []

    for i in data:
        if i.isdigit():
            math_elem.append(i)
        elif (not i.isdigit()) and math_elem:
            math_equation.append(int(''.join(math_elem)))
            math_equation.append(i)
            math_elem = []
        elif (not i.isdigit()) and (not math_elem):
            math_equation.append(i)
    
    if math_elem:
        math_equation.append(int(''.join(math_elem)))

    return math_equation

def calculate(list):               # Вычисление примера, полученного в виде списка
    result = 0
    if len(list) == 1:
        return list[0]

    for s in list:
        if s == '/' or s == '*':
            if s == '/':
                index = list.index(s)
                result = div(list[index - 1], list[index + 1])
                list = list[:index - 1] + [result] + list[index + 2:]
            else:
                index = list.index(s)
                result = mult(list[index - 1], list[index + 1])
                list = list[:index - 1] + [result] + list[index + 2:]

    for s in list:
        if s == '-' or s == '+':
            if s == '-':
                index = list.index(s)
                result = sub(list[index - 1], list[index + 1])
                list = list[:index - 1] + [result] + list[index + 2:]
            else:
                index = list.index(s)
                result = add(list[index - 1], list[index + 1])
                list = list[:index - 1] + [result] + list[index + 2:]
    
    return result
