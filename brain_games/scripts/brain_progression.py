from brain_games.cli import welcome_user, congratulate_user, inform_failure
import secrets


# Константы
PROGRESSION_LENGTH = 10


def arithmetic_progression(start, difference, num_terms):
    return [start + i * difference for i in range(num_terms)]


def the_game_itself():
    name = welcome_user()

    for _ in range(3):  # Можно задать 3 попытки или сколько посчитаете нужным
        start = secrets.randbelow(10) + 1
        difference = secrets.randbelow(10) + 1
        progression = arithmetic_progression(
            start,
            difference,
            PROGRESSION_LENGTH
        )

        # Выбираем случайную позицию в прогрессии, чтобы скрыть ее
        hidden_index = secrets.randbelow(PROGRESSION_LENGTH)
        correct_answer = progression[hidden_index]

        # Подготавливаем строку для вывода пользователю с пропуском
        progression_with_gap = progression.copy()
        progression_with_gap[hidden_index] = '..'
        print("Question:", ' '.join(map(str, progression_with_gap)))

        user_guess = input("What number is missing in the progression? ")
        if int(user_guess) == correct_answer:
            print("Correct!")
        else:
            inform_failure(name, user_guess, correct_answer)
            return

    congratulate_user(name)


def main():
    the_game_itself()


if __name__ == '__main__':
    main()
