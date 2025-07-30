import random


def greatest_common_divisor(num1, num2):
    while num2 != 0:
        remainder = num1 % num2  # Сохраняем остаток
        num1 = num2              # Обновляем num1
        num2 = remainder         # Обновляем num2
    return num1


def run_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        correct_answer = greatest_common_divisor(num1, num2)
        answer = int(input("Your answer: "))

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                  f"'{answer}' is wrong answer ;(." 
                  f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == '__main__':
    main()
