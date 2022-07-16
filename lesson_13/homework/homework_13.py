import asyncio
import random
from time import perf_counter

import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
SIZE = 1000
DATA = []


def get_url_with_random_id() -> str:
    return BASE_URL + str(random.randint(1, 401))


async def main():
    async with aiohttp.ClientSession() as session:
        for _ in range(SIZE):
            url = get_url_with_random_id()
            async with session.get(url) as resp:
                result = await resp.json()
                DATA.append(result["name"])


if __name__ == "__main__":
    start_1 = perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f"Pokemon: {DATA}")
    print(round((perf_counter() - start_1), 3), "c")
    print(len(DATA), "шт")
