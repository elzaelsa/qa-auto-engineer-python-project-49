import random


def is_even(number):
    return number % 2 == 0


rounds_count = 3


def is_even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(rounds_count):
        number = random.randint(1, 1000)
        correct_answer = "yes" if is_even(number) else "no"
        print(f"Question: {number}")
        user_answer = input("Your answer: ")
        if user_answer != correct_answer:
            return False, correct_answer, user_answer
        print("Correct!")
    return True, None, None
