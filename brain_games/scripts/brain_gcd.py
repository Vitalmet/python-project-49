from brain_games.cli import welcome_user, congratulate_user, inform_failure
import secrets


def greatest_common_divisor(num1, num2):
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1


def generate_question():
    num1 = secrets.randbelow(100) + 1
    num2 = secrets.randbelow(100) + 1
    question = f"{num1} {num2}"
    correct_answer = str(greatest_common_divisor(num1, num2))
    return question, correct_answer



def run_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()

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
