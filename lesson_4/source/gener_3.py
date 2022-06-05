import sys
from string import ascii_letters
from random import choice


def gen_letters(n: int) -> str:
    return "".join((choice(ascii_letters) for _ in range(n)))


data = [gen_letters(100) for _ in range(1_000_000)]

tup = (gen_letters(100) for _ in range(1_000_000))

print(len(data))
print(sys.getsizeof(data))

print(tup)
print(sys.getsizeof(tup))



