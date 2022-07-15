from typing import Generator


def avarager() -> Generator:
    total = 0
    counter = 0
    avarage = None

    while True:
        data = yield avarage
        total += data
        counter += 1
        avarage = total / counter


avarager_coro = avarager()
next(avarager_coro)

while user_input := input("Enter a number: "):
    user_input = int(user_input)
    data = avarager_coro.send(user_input)

    print(data)
