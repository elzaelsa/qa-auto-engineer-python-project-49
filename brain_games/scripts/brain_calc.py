from brain_games.engine import start_game
from brain_games.games.calc import calc_game


def main():
    start_game(
        calc_game,
        'What is the result of the expression?'
    )


if __name__ == "__main__":
    main()