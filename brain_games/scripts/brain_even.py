from brain_games.cli import welcome_user, congratulate_user, inform_failure
import secrets


def is_even(number):
    return number % 2 == 0


def run_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = secrets.randbelow(100) + 1
        print(f"Question: {number}")
        answer = input("Your answer (yes or no): ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
            print("Correct!")
        else:
            inform_failure(name, answer, correct_answer)
            return

    congratulate_user(name)


def main():
    run_game()


if __name__ == '__main__':
    main()
