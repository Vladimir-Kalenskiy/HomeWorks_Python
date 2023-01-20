# Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# 1 | 2 | X
# 4 | X | O
# X | 8 | O

# Инициализация карты
maps = [1,2,3,4,5,6,7,8,9]

# Инициализация победных линий
victories = [[0,1,2], [3,4,5], [6,7,8],
             [0,3,6], [1,4,7], [2,5,8],
             [0,4,8], [2,4,6]]

# Вывод карты на экран
def print_maps():
    print(f'\n{maps[0]}', end = " | ")
    print(maps[1], end = " | ")
    print(maps[2])
 
    print(maps[3], end = " | ")
    print(maps[4], end = " | ")
    print(maps[5])
 
    print(maps[6], end = " | ")
    print(maps[7], end = " | ")
    print(f'{maps[8]} \n')

# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# Получить текущий результат игры
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win

# Основная программа
player1 = input('Введите имя первого игрока (играет Х):')
player2 = input('Введите имя второго игрока (играет О):')
game_over = False
player = True
 
while game_over == False:
 
    # 1. Показываем карту
    print_maps()
 
    # 2. Спросим у играющего куда делать ход
    if player == True:
        symbol = "X"
        step = int(input(f"{player1}, ваш ход: "))
    else:
        symbol = "O"
        step = int(input(f"{player2}, ваш ход: "))
 
    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player = not player        
 
# Игра окончена. Покажем карту. Объявим победителя.        
print_maps()
print("Победил", win) 