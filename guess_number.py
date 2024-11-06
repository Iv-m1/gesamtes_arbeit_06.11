# Игра: Угадай число
#
# Используя модуль `random`, напишите программу, которая случайным образом выбирает число от 0 до 100.
# У пользователя есть 6 попыток, чтобы угадать это число. Если пользователь угадывает число,
# выводится сообщение об успехе: "Отлично! Вы угадали число … с … попытки!". Если не угадывает за 6 попыток,
# выводится сообщение о неудаче: “К сожалению, вы не угадали число. Загаданное число было: …”.
#
# В конце программы должны выводиться все попытки пользователя и загаданное число.
#
# По ходу игры после каждой попытки пользователя компьютер выводит сообщение, было ли число пользователя
# больше или меньше загаданного числа: "Загаданное число больше.", "Загаданное число меньше." соответственно.
import random


def play_guess_number():
    print()
    print('Добро пожаловать в игру "Угадай число !')
    print('Я загадал число от 0 до 100 , попробуйте угадать его за 6 попыток . Удачи ! ')
    print()
    rand = random.randint(1,100)
    lis = []
    while True:
        if len(lis) > 6:
            print("Вы превысили количество попыток ! ")
            break
        a = int(input('Введите свое предполагаемое число :'))
        lis.append(a)
        if a > rand:
            print('К сожалению , Вы не угадали . \n Загаданое число меньше . \n Попробуйте еще раз )')
        elif a < rand:
            print('К сожалению , Вы не угадали . \n Загаданое число больше . \n Попробуйте еще раз )')
        else:
            print(f"Отлично! Вы угадали число  с {len(lis)} попытки!")

            break
    print(f"Ваши попытки : {lis} ")
    print (f"Число , которое я загадал : {rand}")



























