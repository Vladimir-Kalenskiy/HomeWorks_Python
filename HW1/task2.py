# (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

def check_predicat (x, y, z):
    left = not (x | y | z)
    right = (not x) & (not y) & (not z)
    result = left == right
    return result

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'({x},{y},{z}) = {check_predicat(x,y,z)}')
