import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def run_game():
    print("Welcome to the Brain Prime Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):  # 3 попытки для игры
        number = random.randint(1, 100)
        print(f"Question: {number}")

        answer = input("Your answer (yes/no): ").strip().lower()
        correct_answer = "yes" if is_prime(number) else "no"

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == '__main__':
    main()