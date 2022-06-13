import os
from typing import Generator

KEYWORD = "user"
PATH_FILE = os.path.join("./lesson_4/homework/.temp/rockyou.txt")


def lines_reader_and_words_finder_generator() -> Generator:
    with open(PATH_FILE, "r", encoding="utf-8") as file:
        while line := (None if not file.readline() else file.readline()):
            if KEYWORD in line:
                yield line.replace("\n", "")


def user_input(line) -> bool:
    while True:
        answer = input(f"Do you want to add this line # {line}? # [Y/N]: ")
        if answer.lower() in ["y", "yes"]:
            return True
        elif answer.lower() in ["n", "no", "not"]:
            return False
        else:
            print("Non-correct input. Try again!")


def generates_list():
    results = [
        word for word in lines_reader_and_words_finder_generator() if user_input(word)
    ]
    print(f"Results: {results}.\n\n ")
    print(f"Total amount of added lines: #{len(results)}#. \n")


if __name__ == "__main__":
    generates_list()
