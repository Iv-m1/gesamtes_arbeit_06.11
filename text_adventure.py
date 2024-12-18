# Игра "Текстовый квест"
#
# Напишите программу для текстовой игры-квеста. Игроку предлагается сюжетная история с различными вариантами действий.
# В зависимости от выбора игрока, история развивается по-разному.
# Цель — пройти игру, приняв правильные решения и достигнув конца истории.
#
# Требования:
#
# 1. Программа должна предлагать игроку несколько вариантов действий в каждом шаге истории.
# 2. Игрок должен вводить свой выбор, который влияет на дальнейшее развитие сюжета.
# 3. Игра должна иметь несколько концовок в зависимости от выбора игрока.
# 4. Программа должна корректно обрабатывать ввод пользователя и предоставлять соответствующую обратную связь.
#
# Сюжет игры:
# Игрок оказывается в загадочном замке и должен пройти через несколько комнат, делая выборы,
# которые повлияют на развитие сюжета и конечный исход. Цель — найти выход из замка, избегая опасностей и решая загадки.
#
# Сюжет:
#
# 1. Начало приключения:
# Вы просыпаетесь в темной комнате замка. Перед вами две двери: левая и правая.
#     - Выбор:
#         - Левая дверь
#         - Правая дверь
# 2. Левая дверь:
# Вы входите в левую комнату и видите старинный сундук.
#     - Выбор:
#         - Открыть сундук
#         - Не открывать сундук и выйти
# 3. Открыть сундук:
# В сундуке оказывается карта с указанием выхода из замка.
#     - Выбор:
#         - Следовать по карте
#         - Игнорировать карту и исследовать комнату
# 4. Следовать по карте:
# Вы идете по карте и приходите к тайному проходу.
#     - Выбор:
#         - Войти в проход
#         - Оставить проход и вернуться назад
# 5. Войти в проход:
# Проход приводит вас к выходу из замка. Вы выиграли!
# 6. Не открывать сундук и выйти:
# Вы выходите из комнаты и попадаете в коридор с двумя новыми дверями.
#     - Выбор:
#         - Первая дверь
#         - Вторая дверь
# 7. Первая дверь:
# Вы входите в первую дверь и видите старого мага.
#     - Выбор:
#         - Поговорить с магом
#         - Игнорировать мага и выйти
# 8. Поговорить с магом:
# Маг дает вам волшебный ключ, который открывает все двери в замке.
#     - Выбор:
#         - Использовать ключ для выхода
#         - Оставить ключ и искать дальше
# 9. Использовать ключ для выхода:
# Вы находите дверь, открываете ее ключом и выходите из замка. Вы выиграли!
# 10. Правая дверь:
# Вы входите в правую комнату и видите лестницу, ведущую вниз.
#     - Выбор:
#         - Спуститься по лестнице
#         - Остаться наверху
# 11. Спуститься по лестнице:
# Лестница ведет вас в подземелье, где вас поджидает дракон.
#     - Выбор:
#         - Сражаться с драконом
#         - Бежать от дракона
# 12. Сражаться с драконом:
# Вы сражаетесь храбро, но дракон оказывается слишком сильным. Вы проиграли.
# 13. Бежать от дракона:
# Вы бежите обратно по лестнице, но дверь наверху оказывается заперта. Вы в ловушке. Вы проиграли.
# 14. Остаться наверху:
# Вы решаете не спускаться по лестнице и находите потайную дверь за картиной.
#     - Выбор:
#         - Войти в потайную дверь
#         - Игнорировать дверь и вернуться назад
# 15. Войти в потайную дверь:
# Потайная дверь приводит вас к выходу из замка. Вы выиграли!
# 16. Вторая дверь:
# Вы входите во вторую дверь и видите зеркало, в котором отражается другая комната.
#     - Выбор:
#         - Войти в зеркало
#         - Разбить зеркало
# 17. Войти в зеркало:
# Вы проходите через зеркало и оказываетесь в другой части замка, где находите выход. Вы выиграли!
# 18. Разбить зеркало:
# Зеркало разбивается, и вы оказываетесь в ловушке. Вы проиграли.
# FINAL


def play_text_adventure():
    print("\n" + "=" * 50)
    print("############################################")
    print("Welcome to the TEXT-ADVENTURE GAME!")
    print("############################################")

    print("=" * 50 + "\n")

    print("1. Начало приключения:")
    print("Вы просыпаетесь в темной комнате замка. Перед вами две двери: левая и правая.")
    q_1 = input("- Выбор: 1 - Левая дверь, 2 - Правая дверь: ")

    if q_1 == "1":
        print("\nВы входите в левую комнату и видите старинный сундук.")
        q_2 = input("- Выбор: 1 - Открыть сундук, 2 - Не открывать сундук и выйти: ")
        if q_2 == "1":
            print("\nВ сундуке оказывается карта с указанием выхода из замка.")
            q_3 = input("- Выбор: 1 - Следовать по карте, 2 - Игнорировать карту и исследовать комнату: ")
            if q_3 == "1":
                print("\nВы идете по карте и приходите к тайному проходу.")
                q_4 = input("- Выбор: 1 - Войти в проход, 2 - Оставить проход и вернуться назад: ")
                if q_4 == "1":
                    print("\nПроход приводит вас к выходу из замка. Вы выиграли!")
                else:
                    print("\nВы возвращаетесь назад, но теряете все шансы на выход. Вы проиграли.")
            else:
                print("\nВы решаете исследовать комнату и находите еще одну загадку. Вы застряли. Вы проиграли.")
        else:
            print("\nВы выходите из комнаты и попадаете в коридор с двумя новыми дверями.")
            q_5 = input("- Выбор: 1 - Первая дверь, 2 - Вторая дверь: ")
            if q_5 == "1":
                print("\nВы входите в первую дверь и видите старого мага.")
                q_6 = input("- Выбор: 1 - Поговорить с магом, 2 - Игнорировать мага и выйти: ")
                if q_6 == "1":
                    print("\nМаг дает вам волшебный ключ, который открывает все двери в замке.")
                    q_7 = input("- Выбор: 1 - Использовать ключ для выхода, 2 - Оставить ключ и искать дальше: ")
                    if q_7 == "1":
                        print("\nВы находите дверь, открываете ее ключом и выходите из замка. Вы выиграли!")
                    else:
                        print("\nВы продолжаете искать и теряетесь в замке. Вы проиграли.")
                else:
                    print("\nВы проигнорировали мага, но упустили шанс выбраться. Вы проиграли.")
            else:
                print("\nВы входите во вторую дверь и видите зеркало, в котором отражается другая комната.")
                q_8 = input("- Выбор: 1 - Войти в зеркало, 2 - Разбить зеркало: ")
                if q_8 == "1":
                    print("\nВы проходите через зеркало и оказываетесь в другой части замка, где находите выход. Вы выиграли!")
                else:
                    print("\nЗеркало разбивается, и вы оказываетесь в ловушке. Вы проиграли.")
    elif q_1 == "2":
        print("\nВы входите в правую комнату и видите лестницу, ведущую вниз.")
        q_9 = input("- Выбор: 1 - Спуститься по лестнице, 2 - Остаться наверху: ")
        if q_9 == "1":
            print("\nЛестница ведет вас в подземелье, где вас поджидает дракон.")
            q_10 = input("- Выбор: 1 - Сражаться с драконом, 2 - Бежать от дракона: ")
            if q_10 == "1":
                print("\nВы сражаетесь храбро, но дракон оказывается слишком сильным. Вы проиграли.")
            else:
                print("\nВы бежите обратно по лестнице, но дверь наверху оказывается заперта. Вы в ловушке. Вы проиграли.")
        else:
            print("\nВы решаете не спускаться по лестнице и находите потайную дверь за картиной.")
            q_11 = input("- Выбор: 1 - Войти в потайную дверь, 2 - Игнорировать дверь и вернуться назад: ")
            if q_11 == "1":
                print("\nПотайная дверь приводит вас к выходу из замка. Вы выиграли!")
            else:
                print("\nВы возвращаетесь назад, но теряете возможность выйти. Вы проиграли.")
    else:
        print("\nНеверный выбор. Игра окончена.")

    print("\nСпасибо за игру!")
    print()
    s = input("Игра закончена. Клавиша ввод - дальше в меню")
    if not s:
        from main import main
        main()


