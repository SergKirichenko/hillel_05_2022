from random import randint
from threading import Thread
from time import perf_counter, sleep

SPEC_LIST = []
N = 10000


def wait_on() -> None:  # Function for decoration
    def t_() -> None:
        sleep(0.25)
        print(" .", end="")

    t_(), t_(), t_(), t_()
    print(" ")


def random_list(n: int) -> None:
    print("Loading...")
    for _ in range(n):
        SPEC_LIST.append(randint(1, 100))
    wait_on()
    print("Done")


def two(int_list: list) -> None:
    print(f"Sum of list: {sum(int_list)}")


def three(int_list: list) -> None:
    print(f"Middle meaning: {sum(int_list) / len(int_list)}")


# def foo():
#     time_a = perf_counter()
#     random_list(N)
#     two(SPEC_LIST)
#     three(SPEC_LIST)
#     print(f"time: {round(perf_counter() - time_a, 2)},c\n")


def main():
    time_a = perf_counter()
    thread_1 = Thread(target=random_list, args=(N,))
    thread_2 = Thread(target=two, args=(SPEC_LIST,))
    thread_3 = Thread(target=three, args=(SPEC_LIST,))
    thread_1.start()
    thread_1.join()
    thread_2.start()
    thread_3.start()
    print(f"time: {round(perf_counter()-time_a, 2)},c\n")


if __name__ == "__main__":
    main()

    # t_1 = Thread(target=foo).start()
    # t_2 = Thread(target=foo).start()
    # t_3 = Thread(target=foo).start()
