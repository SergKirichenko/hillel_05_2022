team: list([dict]) = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def repr_players(players: list([dict]), sorter: bool, key=lambda x: x["number"]) -> None:
    print("TEAM:")
    if sorter:
        for player in sorted(players, key=key):
            print(
                f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}"
            )
    else:
        for player in players:
            print(
                f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}"
            )
    print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <-")


def add_player(num: int, name: str, age: int) -> None:
    player = {"name": name, "number": num, "age": age}
    if num in {player["num"] for player in team}:
        print(log(message="You can't add player with the same number"))
        return

    team.append(player)
    log(message=f"Player {player['name']} added")


def remove_player(players: list([dict]), num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Player {player_name} removed")
            return


def update_player(num: int) -> None:
    for player in team:
        if player["number"] == num:
            player.update()
            player = {
                "name": player["name"],
                "age": player["age"],
                "number": player["number"],
            }
            team.append(player)


# =====================================================
def main():
    add_player(13, "Stiven", 12)
    repr_players(team, False)


# =====================================================

if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")