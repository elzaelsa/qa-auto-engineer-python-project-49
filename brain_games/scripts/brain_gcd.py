from brain_games.engine import start_game
from brain_games.games.gcd import gcd_game


def main():
    start_game(
        gcd_game,
        'Find the greatest common divisor of given numbers.'
    )


if __name__ == "__main__":
    main()