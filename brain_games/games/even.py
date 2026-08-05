import random


def is_even(number):
    return number % 2 == 0


def is_even_game():
    number = random.randint(1, 1000)
    user_answer = 'yes' if is_even(number) else 'no'
    return str(number), user_answer