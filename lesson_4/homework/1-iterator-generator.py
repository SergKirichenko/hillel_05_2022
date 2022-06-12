from typing import Generator

FILENAME = "rockyou.txt"
SEARCH_KEYWORD = "user"


def read_lines_find_user_generator() -> Generator:
    with open(FILENAME) as file:
        while line := file.readline():
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")


def answer(line) -> bool:
    while True:
        quest = input(f"Do you want to add <<{line}>>? [Y/N]: ")
        if quest.lower() in ["y", "yes"]:
            return True
        elif quest.lower() in ["n", "no", "not"]:
            return False

        print("Non-correct input. Try again!")


def user_finder():
    results = [line for line in read_lines_find_user_generator() if answer(line)]
    print(f"Results: {results}.\nAmount of added lines: {len(results)}.")


if __name__ == "__main__":
    user_finder()