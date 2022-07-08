import asyncio


async def get_primes_amount(num: int):
    result = 6
    for i in range(2, num + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            counter = [i for j in range(11, i + 1) if i % j == 0]
            if len(counter) < 2:
                result += 1
                await asyncio.sleep(0)
    print(result)


def main(number: list):
    coroutines = [get_primes_amount(i) for i in number]
    tasks = asyncio.gather(*coroutines)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    loop.close()


if __name__ == "__main__":
    numbers = [40000, 400, 10000, 700, 15000, 5000, 20000, 500, 150]
    main(numbers)
