import asyncio
from pprint import pprint as print
from typing import AsyncGenerator, Iterable

PLAYERS = [
    {"name": "John", "age": 20},
    {"name": "Marry", "age": 17},
    {"name": "Carl", "age": 33},
    {"name": "Bob", "age": 21},
]


async def filtered_players(players: Iterable) -> AsyncGenerator:
    for player in players:
        if player["age"] > 18:
            yield player


async def repr():
    async for player in filtered_players(PLAYERS):
        print(player)


asyncio.run(repr())
