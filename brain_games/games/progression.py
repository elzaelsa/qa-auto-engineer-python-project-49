import random


def generate_progression(start, step, progression_length):
    progression = []
    for i in range(progression_length):
        currentElement = start + i * step
        progression.append(currentElement)
    return progression


def progression_game():
    progression_length = random.randint(5, 15)
    start = random.randint(1, 20)
    step = random.randint(1, 20)
    progression = generate_progression(start, step, progression_length)
    hidden_index = random.randint(0, progression_length - 1)

    user_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    question = " ".join(map(str, progression))
    return question, user_answer





