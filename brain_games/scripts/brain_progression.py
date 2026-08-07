from brain_games.engine import start_game
from brain_games.games.progression import progression_game


def main():
    start_game(
        progression_game,
        'What number is missing in the progression?'
    )


if __name__ == "__main__":
    main()