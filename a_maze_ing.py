import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return
    print(f"Config file: {sys.argv[1]}")


if __name__ == "__main__":
    main()
