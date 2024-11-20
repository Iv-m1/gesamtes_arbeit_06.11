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

# Игра "Виселица"
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование начала и окончания игры и всех попыток игрока с временными метками (дата и время).
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Добавить возможность сохранять текущий прогресс игры в файл для продолжения игры позже,
# если игра не была завершена победой или поражением (то есть было прерывание программы во время игры).

import random
import datetime

def log_action(message):
    with open("hangman_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message}\n")

# FINAL


def play_hangman():
    print()
    print("############################################")
    print('play the game: << Виселица >>')
    print("############################################")
    print()
    hang_man = [
        """
               -----
                   |
                   |
                   |
                   |
                   |
            =========
            """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """]
    next_hangman = iter(hang_man)

    words = ["яблоко", "машина", "компьютер", "программа", "книга", "робот", "питон"]

    rand_word = random.choice(words)
    list_letter = list(rand_word)
    print(list_letter)

    attemp = 7
    len_word = len(rand_word)
    print(len_word)
    df = 0
    if_letter_ = []

    word_append_letter = []

    for i in range(0, (len_word)):
        word_append_letter.append("*")

    print(next(next_hangman))
    print()
    # for win_letter in range((len_word) - 1):
    #    word_append_letter[win_letter] = "_"
    print("Слово :  " + " ".join(word_append_letter))
    log_action(f"Начало игры. Загаданное слово:  {rand_word}")

    while True:
        string = input("Угадай букву слова  , Количество букв = {} , у Вас {} попыток! \nВведите букву :".format(len(rand_word), attemp-1))
        print()

        if string in list_letter:
            log_action(f"Введённая буква: {string}")
            if string in if_letter_:
                print("Эта буква уже была : ", string)
                log_action(f"Повторный ввод буквы: {string}, количество оставшихся попыток: {attemp-1}")
                hangman = next(next_hangman)
                print(hangman)
                #if attemp == 1:
                #    print("Последняя попытка!!! . Попробуй еще раз ! ")
                #    print("Слово :  " + " ".join(word_append_letter))
                #    attemp -= 1
                if attemp < 1:
                    #hangman = next(next_hangman)
                    #print(hangman)
                    print("Вы проиграли... :( , это СЛОВО : ", rand_word)
                    log_action(f"Пользователь проиграл.")
                    print()
                    s = input("Игра закончена. Клавиша ввод - дальше в меню")
                    if not s:
                        from main import main
                        main()
                attemp -= 1
                continue
            print("Такая буква есть!!!  Буква : ", string)
            for idx, letter in enumerate(list_letter):
                if letter == string:
                    word_append_letter[idx] = string
                if_letter_.append(letter)

            print("Слово :" + " ".join(word_append_letter))

        else:
            if attemp > 1:
                print("К сожалению , такой буквы нет в загаданном слове . Попробуй еще раз ! ")
                print("Слово :  " + " ".join(word_append_letter))
                log_action(f"Игрок ввёл неправильную букву: {string}, количество оставшихся попыток: {attemp-1}")
                hangman = next(next_hangman)
                print(hangman)
                attemp -= 1
            elif attemp == 1:
                #hangman = next(next_hangman)
                #print(hangman)
                print("Последняя попытка!!! . Попробуй еще раз ! ")
                print("Слово :  " + " ".join(word_append_letter))
                attemp -= 1

            elif attemp < 1:
                hangman = next(next_hangman)
                print(hangman)
                print("Вы проиграли... :( , это СЛОВО : ", rand_word)
                log_action(f"Игрок проиграл. Загаданное слово: {rand_word} \n------------------------------")
                print()
                s = input("Игра закончена. Клавиша ввод - дальше в меню")
                if not s:
                    from main import main
                    main()
            print(attemp+1)
