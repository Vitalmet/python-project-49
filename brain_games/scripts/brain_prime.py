from brain_games.cli import welcome_user, congratulate_user, inform_failure
import secrets


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    number = secrets.randbelow(100) + 1
    question = number
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):  # 3 попытки для игры
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        answer = input("Your answer (yes/no): ").strip().lower()

        if answer == correct_answer:
            print("Correct!")
        else:
            inform_failure(name, answer, correct_answer)
            return

    congratulate_user(name)


def main():
    game()


if __name__ == '__main__':
    main()