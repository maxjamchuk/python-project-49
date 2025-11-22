from brain_games.game_engine import run_game
from brain_games.games.calc import DESCRIPTION, make_round


def main() -> None:
    run_game(make_round, DESCRIPTION)


if __name__ == "__main__":
    main()
