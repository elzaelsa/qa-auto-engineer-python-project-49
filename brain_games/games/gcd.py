import random


def gcd(first, second):
    while second != 0:
        first, second = second, first % second
    return first 


def gcd_game():
    first = random.randint(1, 10)
    second = random.randint(1, 10)
    question = f"{first} {second}"
    answer = str(gcd(first, second))
    return question, answer