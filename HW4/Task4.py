# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 

# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

#     a, b, c, d, e, h - рандом

from random import randint

def generate_polynom(powers_dict):
    result = []

    for power, coef in sorted(powers_dict.items(), reverse=True):
        if power == 0:
            if coef == 0:
                continue

            result.append(str(coef))
            continue

        if coef == 0:
            continue

        elif coef == 1:
            if power == 1:
                result.append(f'x')

            else:
                result.append(f'x^{power}')

        else:
            if power == 1:
                result.append(f'{coef}*x')

            else:
                result.append(f'{coef}*x^{power}')

    return result

def get_polynom(power: int, max_coef: int = 100) -> str:
    lst_coefs = [randint(0, max_coef) for _ in range(power + 1)]
    dct_pows = {power - i: lst_coefs[i] for i in range(power + 1)}

    result = generate_polynom(dct_pows)

    return ' + '.join(result)

max_power = int(input('Введите натуральную степень k: '))
print(f'Многочлен степени {max_power}:', get_polynom(max_power))