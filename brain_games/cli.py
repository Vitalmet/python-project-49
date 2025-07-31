import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def congratulate_user(name):
    print(f"Congratulations, {name}!")

def inform_failure(name, wrong_answer, correct_answer):
    print(f"'{wrong_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")