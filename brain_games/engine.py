import prompt 

round_count = 3

def start_game(game_task, rules):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for i in range(round_count):
        question, correct_answer = game_task()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer != str(correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
