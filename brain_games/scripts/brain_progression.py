from brain_games.cli import welcome_user, congratulate_user, inform_failure
import secrets


# Константы
PROGRESSION_LENGTH = 10


def arithmetic_progression(start, difference, num_terms):
    return [start + i * difference for i in range(num_terms)]


def generate_question():
    start = secrets.randbelow(10) + 1
    difference = secrets.randbelow(10) + 1
    progression = arithmetic_progression(
        start,
        difference,
        PROGRESSION_LENGTH
    )
    hidden_index = secrets.randbelow(PROGRESSION_LENGTH)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, str(correct_answer)


def the_game_itself():
    name = welcome_user()
    print("What number is missing in the progression?")

    for _ in range(3):  # Можно задать 3 попытки или сколько посчитаете нужным
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_guess = input("Your answer: ").strip()

        if user_guess == correct_answer:
            print("Correct!")
        else:
            inform_failure(name, user_guess, correct_answer)
            return

    congratulate_user(name)


def main():
    the_game_itself()


if __name__ == '__main__':
    main()
