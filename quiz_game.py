# Игра: Викторина
#
# Создайте игру "Викторина", где пользователю задаются 5 вопросов с вариантами ответов.
# После выбора варианта ответ выводится, правильный ли был сделан выбор.
# В конце игры выводится общее количество правильных ответов.
#
# Столица Франции?
# — 1. Лондон
# — 2. Берлин
# — 3. Париж
#
# Столица Германии?
# — 1. Лондон
# — 2. Берлин
# — 3. Венеция
#
# Столица США?
# — 1. Нью-Йорк
# — 2. Лос-Анджелес
# — 3. Вашингтон
#
# Столица Греции
# — 1. Афины
# — 2. Стамбул
# — 3. Киев
#
# Столица Норвегии
# — 1. Осло
# — 2. Порту
# — 3. Мюнхен

# FINAL

def play_quiz_game():
    global odl, rigth_answer
    print()
    print("############################################")
    print('play the game: QUIZ_GAME')
    print("############################################")

    print()
    quest = {
        "Столица Франции": ["1. Лондон", "2. Берлин", "3. Париж"],
        "Столица Германии": ["1. Лондон", "2. Берлин", "3. Венеция"],
        "Столица США": ["1. Нью-Йорк", "2. Лос-Анджелес", "3. Вашингтон"],
        "Столица Греции": ["1. Афины", "2. Стамбул", "3. Киев"],
        "Столица Норвегии": ["1. Осло", "2. Порту", "3. Мюнхен"]
    }


    list_question = list(quest.keys())

    answers = {
        "Столица Франции": "Париж",
        "Столица Германии": "Берлин",
        "Столица США": "Вашингтон",
        "Столица Греции": "Афины",
        "Столица Норвегии": "Осло"
    }
    ans_top = {}
    land_top = [f for f in answers]
    counter = {}
    #print(land_top)
    town_3 = []
    rigth_answer = []

    for i in range(len(list_question)):
        print(list_question[i])
        print()

        list_3_quest = quest[list_question[i]]
        for listing in list_3_quest:
            print(listing)
            f_list = listing.split(" ")
            #print(f_list[0])
            odl = f_list[0][0].split(" ")
            #print(odl)
            counter[odl[0]] = f_list[1]
            ans_top[list_question[i]] = f_list[1]
            #print(ans_top[list_question[i]])
            town_3.append(f_list[1])
        print()
        q = input("Введите правельный ответ (1,2,3) : ")

        #print(list_question.index(land_top[counter[list_question[i]]]))  # 0
        #print(land_top[list_question.index(land_top[counter[list_question[i]]])]) # Столица Франции
        #print(town_3.index(answers[list_question[i]]))  # 2
        #print(answers[list_question[i]]) # Париж
        print()
        #print([q])
        #print(odl)
        #print(counter)
        keys = list(counter.keys())
        keys_rigth = keys[int(q)-1]
        #print(keys_rigth)
        #print()

        if q == str(keys_rigth): # == land_top[list_question.index(land_top[counter[list_question[i]]])]:
            rigth_answer.append(1)
        else:
            rigth_answer.append(0)

        #print(rigth_answer)
        print()

    print("Общее количество правильных ответов : ", sum(rigth_answer))


    s = input("Игра закончена. Клавиша ввод - дальше в меню  ")
    if not s:
        from main import main
        main()
