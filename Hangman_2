import random

def play_hangman():
    print("\nДобро пожаловать в игру: << Виселица >>\n")

    words = ["яблоко", "машина", "компьютер", "программа", "книга", "робот", "питон"]
    word = random.choice(words)  # Случайное слово
    guessed_word = ["_"] * len(word)  # Маскируем слово
    attempts = 6  # Количество попыток
    used_letters = set()  # Для хранения использованных букв

    print(f"Слово состоит из {len(word)} букв: {' '.join(guessed_word)}")
    print(f"У вас {attempts} попыток.\n")

    while attempts > 0 and "_" in guessed_word:
        letter = input("Введите букву (или попробуйте угадать слово): ").lower()

        # Проверка, если игрок ввел больше одной буквы
        if len(letter) > 1:
            if letter == word:
                print(f"\nПоздравляем! Вы угадали слово: {word}")
                return
            else:
                attempts -= 1
                print(f"Неверно! Это не то слово. Осталось попыток: {attempts}\n")
                continue

        # Проверка, что буква уже была введена
        if letter in used_letters:
            print("Вы уже использовали эту букву. Попробуйте другую.\n")
            continue

        # Добавляем букву в использованные
        used_letters.add(letter)

        if letter in word:
            print(f"Верно! Буква '{letter}' есть в слове.\n")
            # Обновляем отображаемое слово
            for i, char in enumerate(word):
                if char == letter:
                    guessed_word[i] = letter
        else:
            attempts -= 1
            print(f"Неверно! Буквы '{letter}' нет в слове. Осталось попыток: {attempts}\n")

        # Печать текущего состояния слова
        print("Слово: ", " ".join(guessed_word))
        print("Использованные буквы: ", ", ".join(sorted(used_letters)), "\n")

    # Проверяем, угадал ли игрок слово
    if "_" not in guessed_word:
        print(f"Поздравляем! Вы угадали слово: {''.join(guessed_word)}")
    else:
        print(f"Вы проиграли! Слово было: {word}")

# Запуск игры
if __name__ == "__main__":
    play_hangman()
