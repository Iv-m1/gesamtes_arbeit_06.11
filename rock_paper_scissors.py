# Игра: Камень, ножницы, бумага
#
# Создайте игру "Камень, ножницы, бумага", где пользователь играет против компьютера.
# Компьютер случайным образом выбирает одно из трех значений: камень, ножницы или бумагу.
# Пользователь вводит свой выбор, и программа определяет победителя. Если выборы одинаковы, игра объявляет ничью.
# Игра продолжается до тех пор, пока один из игроков (пользователь или компьютер)
# не одержит на три победы больше, чем соперник. В конце показывается итоговый счет и объясляется победитель.


import random
# FINAL

def play_rock_paper_scissors():
    print()
    print("############################################")
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("############################################")
    print()
    print("Правила: Камень бьёт ножницы, ножницы бьют бумагу, бумага бьёт камень.")
    print("Вы играете против компьютера. Первый, кто наберёт 3 победы, выигрывает!")
    print()

    choices = ["камень", "ножницы", "бумага"]
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        print("Ваш счёт:", user_score, "| Счёт компьютера:", computer_score)
        print()
        print("Выберите: 1 - Камень, 2 - Ножницы, 3 - Бумага")
        user_choice = input("Ваш выбор: ")

        if user_choice not in ["1", "2", "3"]:
            print("Неправильный выбор! Попробуйте снова.")
            continue

        user_choice = choices[int(user_choice) - 1]
        computer_choice = random.choice(choices)

        print()
        print("Вы выбрали:", user_choice)
        print("Компьютер выбрал:", computer_choice)

        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "камень" and computer_choice == "ножницы") or \
                (user_choice == "ножницы" and computer_choice == "бумага") or \
                (user_choice == "бумага" and computer_choice == "камень"):
            print("Вы выиграли раунд!")
            user_score += 1
        else:
            print("Компьютер выиграл раунд!")
            computer_score += 1

    print()
    print("Игра окончена!")
    print("Ваш счёт:", user_score, "| Счёт компьютера:", computer_score)
    if user_score > computer_score:
        print("Поздравляем! Вы выиграли!")
    else:
        print("Компьютер победил! Попробуйте ещё раз.")
        print()
        input("Игра закончена. Клавиша ввод - дальше в меню")
        from main import main
        main()



