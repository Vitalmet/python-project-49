import random


def is_even(number):
    return number % 2 == 0


def run_game():
    print("Welcome to the Brain Even Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer (yes or no): ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == '__main__':
    main()
