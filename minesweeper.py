# Игра: Сапёр
#
# Цель игры: открыть все клетки, не содержащие мин.
#
# Правила игры:
#
# 1. Игровое поле состоит из клеток размером 5x5.
# 2. На поле случайным образом размещены 5 мин.
# 3. Игрок вводит координаты клетки (например, "2 3" для второй строки и третьего столбца), чтобы проверить ее.
# 4. Если игрок открывает клетку с миной, он проигрывает.
# 5. Если игрок открывает клетку без мины, на этой клетке отображается число, указывающее, сколько мин находится в соседних клетках (по горизонтали, вертикали и диагоналям).
# 6. Игрок побеждает, если открывает все клетки, не содержащие мин.
#
# Пример игрового процесса:
#
# 1. Игроку показывается пустое поле:
# - - - - -
# - - - - -
# - - - - -
# - - - - -
# - - - - -
#
# 2. Игрок вводит координаты клетки:
# Введите координаты клетки (строка столбец): 2 3
#
# 3. Если в этой клетке нет мины, открывается число:
# - - - - -
# - - 1 - -
# - - - - -
# - - - - -
# - - - - -
#
# 4. Игрок продолжает вводить координаты, пока не откроет все безопасные клетки или не попадет на мину.
# 5. Если игрок открывает клетку с миной, игра заканчивается:
# - - - - -
# - - * - -
# - - - - -
# - - - - -
# - - - - -
# Вы проиграли! Вы попали на мину.
#
# 6. Если игрок открывает все клетки без мин, игра заканчивается победой:
# - 1 1 1 -
# - 1 * 1 -
# - 2 2 2 -
# - 1 * 1 -
# - 1 1 1 -
# Поздравляем! Вы открыли все безопасные клетки.
import random
# FINAL

def play_minesweeper():
    print()
    print("############################################")
    print('Добро пожаловать в игру "Сапер !')
    print('Я расставил 5 мин. Задавая координаты *X, Y*, попробуй не взорватся!!! Удачи !!! ')
    print('Чтобы выйти из игры, нажмите ввод - << ENTER >>')
    print("############################################")
    print()
    # Erstellung einer Liste mit dem gewünschten Muster
    pattern_list = [
        [" ", "1", "2", "3", "4", "5"],
        ["1", "-", "-", "-", "-", "-"],
        ["2", "-", "-", "-", "-", "-"],
        ["3", "-", "-", "-", "-", "-"],
        ["4", "-", "-", "-", "-", "-"],
        ["5", "-", "-", "-", "-", "-"]]

    game_coord = []

    for v in range(0, 5):
        x1 = random.randrange(1, 6)
        y1 = random.randrange(1, 6)
        pl = [int(x1), int(y1)]
        game_coord.append(pl)

    for row in pattern_list:
        print(" ".join(row))

    print()
    #print(game_coord)
    points = 0

    while True:

        a = input("Введите координаты для удара : ")
        if not a:
            from main import main
            main()
        print()
        c = a.split()
        # print(a, c)
        mine_list = []

        y, x = int(c[0]), int(c[1])
        print()

        print("Координаты : x:", int(y), " y:", int(x))


        if [int(y+1), int(x)] in game_coord:
            mine_list.append(1)
        if [int(y-1), int(x)] in game_coord:
            mine_list.append(1)
        if [int(y+1), int(x+1)] in game_coord:
            mine_list.append(1)
        if [int(y+1), int(x-1)] in game_coord:
            mine_list.append(1)
        if [int(y), int(x+1)] in game_coord:
            mine_list.append(1)
        if [int(y), int(x-1)] in game_coord:
            mine_list.append(1)

        #print(mine_list)
        print()
        sum_mine_round = sum(mine_list)
        mine_list.clear()
        pattern_list[int(x)][int(y)] = str(sum_mine_round)
        #print(type(pattern_list[int(x)][int(y)]))
        if pattern_list[int(x)][int(y)] == "0":
            pattern_list[int(x)][int(y)] = '#'

        if [int(y), int(x)] in list(game_coord):
            print("Вы попали на МИНУ!!!")
            print()
            for dol in game_coord:
                x, y = dol[0], dol[1]
                pattern_list[int(x)][int(y)] = "✹"
            pattern_list[int(x)][int(y)] = 'O'

            for row in pattern_list:
                print(" ".join(row))
            print()
            input("Игра закончена. Клавиша ввод - дальше в меню")
            from main import main
            main()
        points +=1
        for row in pattern_list:
            print(" ".join(row))

        if points == 20:
            pattern_list[int(x)][int(y)] = '1'
            for row in pattern_list:
                print(" ".join(row))
            print()
            print("ПОБЕДА!!! Вы обошли все мины!")
            print()
            input("Игра закончена. Клавиша ввод - дальше в меню  ")
            from main import main
            main()



