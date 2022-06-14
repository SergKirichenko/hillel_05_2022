team: list = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]
NUMBER = "number"
AGE = "age"
NAME = "name"
VALUE = NUMBER


def repr_players(players: list([dict]), sorter: bool = False, key=lambda x: x[VALUE]
) -> None:  
    sub_list_dict = [
        {"Number":["Name", "Age"]},
        {"Name": ["Number", "Age"]},
        {"Age": ["Name", "Number"]}
    ]
    print("The TEAM:")
    if sorter and VALUE == NUMBER:
        for player in sorted(players, key=key):
            print(
                f"\t{player['number']} -" f"{sub_list_dict[VALUE][0]}:{player['name']}," f"{sub_list_dict[VALUE][1]}:{player['age']}"
            )
    else :
        print(
                f"\t{player['name']} -" f"Name:{player['name']}," f"Age:{player['age']}"
            )
    print("\n")

def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <-")





if __name__ == "__main__":
    repr_players(team, True)
    # main()
# else:
#     raise SystemExit("This module in only for running")

