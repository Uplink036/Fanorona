"""Module entrypoint for `python -m cli.fanorona`.

Runs the minimal terminal play loop using `terminal.simple_play_loop()`.
"""
import argparse
from cli.terminal import play_loop


def main():
    parser = argparse.ArgumentParser(description="Fanorona Terminal Game")
    parser.add_argument('--start', action='store_true', help='Start the game loop')
    args = parser.parse_args()

    if args.start:
        play_loop()
    else:
        print("No action specified. Use --start to begin the game.")


if __name__ == '__main__':
    main()
