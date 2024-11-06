# Игра "Виселица"
#
# Напишите программу для игры "Виселица". Игроку дается слово, которое он должен угадать, называя буквы.
# Если игрок называет неправильную букву, ему начисляется штрафное очко.
# Игра заканчивается победой при угадывании слова или проигрышем при достижении лимита штрафных очков.
#
# Требования:
#
# 1. Программа должна случайным образом выбирать слово из списка.
# 2. Игрок должен иметь возможность вводить буквы по одной за попытку.
# 3. Если игрок угадал букву, она должна отображаться в правильных позициях в слове.
# Вместо остальных (скрытых) букв показываются звездочки *.
# 4. Если игрок назвал неправильную букву, количество штрафных очков должно увеличиваться.
# 5. Игра заканчивается победой, если все буквы слова угаданы, или проигрышем,
# если количество штрафных очков достигает лимита (например, 6).

import random

def play_hangman():
    print()
    print()
    print('play the game: << Виселица >>')
    print()

    words = ["яблоко", "машина", "компьютер", "программа", "книга", "робот", "питон"]

    rand_word = random.choice(words)
    print(rand_word)
    popitki = len(rand_word)

    for i in range(1, len(rand_word)):

        string = input("Угадай букву слова... {}, - Количество букв, у Вас {} попыток   ".format(popitki, len(rand_word)))

        bukwi = [a for a in rand_word]

        if string in bukwi:
            print("Такая буква есть!!!  Буква : ", string)
        else:
            popitki -= 1
            if popitki == 0:
                print("Вы проиграли...")



