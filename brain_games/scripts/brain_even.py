from brain_games.cli import welcome_user
from brain_games.even import is_even_game


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    result, correct_answer, user_answer = is_even_game()
    if not result:
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
        )
        print(f"Let's try again, {name}!")
        return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()