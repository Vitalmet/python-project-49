import random
import operator


def generate_question():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(operations.keys()))
    question = f"{num1} {op} {num2}"
    correct_answer = operations[op](num1, num2)
    return question, correct_answer


def run_game():
    print("Welcome to the Brain Calculator Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        answer = int(input("Your answer: "))

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
