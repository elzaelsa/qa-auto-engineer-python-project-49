import random

symbols = ['+', '-', '*']


def calc(first: int, second: int, operator: str):
    match operator:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second


def calc_game():
    first = random.randint(1, 50)
    second = random.randint(1, 50)
    operator = random.choice(symbols)
    quastion = f'{first} {operator} {second}'
    user_answer = calc(first, second, operator)
    return quastion, user_answer

