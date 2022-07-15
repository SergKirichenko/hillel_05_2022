import asyncio
import random
from time import perf_counter

import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
SIZE = 800
DATA = []


def get_url_with_random_id():
    return BASE_URL + str(random.randint(1, 401))


async def main():
    async with aiohttp.ClientSession() as session:
        for _ in range(SIZE):
            url = get_url_with_random_id()
            async with session.get(url) as resp:
                result = await resp.json()
                DATA.append(result["name"])


if __name__ == "__main__":
    stat_1 = perf_counter()
    asyncio.get_event_loop().run_until_complete(main())
    # asyncio.run(main())  # результат с ошибками
    print(f"Pokemon: {DATA}")
    print(round((perf_counter() - stat_1), 3))