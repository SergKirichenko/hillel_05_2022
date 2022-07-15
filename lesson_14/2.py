total = 0
counter = 0


def avarager(n: int) -> float:
    global total
    global counter

    total += n
    counter += 1
    return total / counter


while user_input := input("Enter the value: "):
    user_input = int(user_input)
    data = avarager(user_input)
    print(f"{data=}")
