from time import perf_counter


def get_primes_amount(num):
    result = 6
    for i in range(2, num + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            counter = [i for j in range(11, i + 1) if i % j == 0]
            if len(counter) < 2:
                result += 1
    return result


def main():
    numbers = [40000, 400, 10000, 700, 15000, 5000, 20000, 500, 150]

    for a in numbers:
        rad = get_primes_amount(a)
        print(rad)


if __name__ == "__main__":
    time_a = perf_counter()
    main()
    print(f"time: {perf_counter() - time_a}")
