from brain_games.engine import start_game
from brain_games.games.even import is_even_game


def main():
    start_game(is_even_game, 
    'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == "__main__":
    main()