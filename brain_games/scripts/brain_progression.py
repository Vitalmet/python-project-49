import random


def arithmetic_progression(start, difference, num_terms):
    return [start + i * difference for i in range(num_terms)]


def the_game_itself():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):  # Можно задать 3 попытки или сколько посчитаете нужным
        start = random.randint(1, 10)
        difference = random.randint(1, 10)
        progression = arithmetic_progression(start, difference, 10)

        # Выбираем случайную позицию в прогрессии, чтобы скрыть ее
        hidden_index = random.randint(0, len(progression) - 1)
        correct_answer = progression[hidden_index]

        # Подготавливаем строку для вывода пользователю с пропуском
        progression_with_gap = progression.copy()
        progression_with_gap[hidden_index] = '..'
        print("Progression:", ' '.join(map(str, progression_with_gap)))

        user_guess = input("What number is missing in the progression? ")

        if int(user_guess) == correct_answer:
            print("Correct!")
        else:
            print(f"{user_guess} is wrong answer. ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    the_game_itself()


if __name__ == '__main__':
    main()