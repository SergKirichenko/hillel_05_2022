from typing import List

team: List[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]
NUMBER = "number"
AGE = "age"
NAME = "name"
VALUE: str = NUMBER


def repr_players(
    players: List[dict], sorter: bool = False, key=lambda x: x[VALUE]
) -> None:
    sub_list_dict = {
        "number": ["Name", "Age"],
        "name": ["Number", "Age"],
        "age": ["Name", "Number"],
    }
    print("The TEAM:")
    if sorter:
        val_a, val_b = sub_list_dict[VALUE]
        for player in sorted(players, key=key):
            print(
                f"\t{player[VALUE]} - "
                f"{val_a}:{player[val_a.lower()]}, {val_b}:{player[val_b.lower()]}"
            )
    else:
        for player in players:
            print(f"\t{player['number']} - Name:{player['name']}, Age:{player['age']}")
    print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <-")


def add_player(number: int, name: str, age: int) -> None:
    player = {"name": name, "number": number, "age": age}
    if number in [people["number"] for people in team]:
        return log(message="This player's number already exists. Change number!!!")
    team.append(player)
    log(message=f'Player {player["name"]} added')
    print("\n")


def remove_player(players: List[dict], number: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == number:
            player_name = player["name"]
            del players[index]
            log(message=f"Player {player_name} deleted")
            print("\n")


def update_player(
    number: int, new_number: int = None, new_name: str = None, new_age: int = None
) -> None:
    for player in team:
        if player["number"] == number:
            if new_name and new_age:
                player["name"] = new_name
                player["age"] = new_age
                log(
                    message=f"Player number: {number} now is: {new_name} (Age:{new_age}) "
                )
            elif new_number:
                player["number"] = new_number
                log(
                    message=f"You change player number: <{number}> on new number: <{new_number}> "
                )
            print("\n")


######################################################
def main():
    repr_players(team, True)
    add_player(13, "Stiven", 12)
    add_player(15, "Adam", 24)
    repr_players(team, False)
    update_player(12, 7)
    update_player(1, new_name="Bill", new_age=21)
    remove_player(team, 13)
    repr_players(team, False)


# ######################################################

if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
