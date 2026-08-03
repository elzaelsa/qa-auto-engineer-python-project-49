from brain_games.games.calc import calc_game
from brain_games.engine import start_game

def main():
    start_game(
        calc_game,
        'What is the result of the expression?'
    )


if __name__ == "__main__":
    main()