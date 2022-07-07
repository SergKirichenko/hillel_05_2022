from random import randint
from threading import Thread
from time import perf_counter, sleep

N = 100000


def random_list(n) -> list:
    print("наполнение списка")
    list_r = [randint(1, 100) for _ in range(n)]
    # print(f".{sleep(1)}.{sleep(1)}.{sleep(1)}.{sleep(1)}.")
    sleep(1)
    print("список заполнен")
    return list_r


def two(int_list: list) -> None:
    print(f"Сумма списка: {sum(int_list)}")


def three(int_list) -> None:
    print(f"Среднее значение: {sum(int_list)/len(int_list)}")


def main():
    time1 = perf_counter()
    ram = random_list(N)
    two(ram)
    three(ram)
    print(perf_counter() - time1)


thr_1 = Thread(target=random_list, args=(N,))
