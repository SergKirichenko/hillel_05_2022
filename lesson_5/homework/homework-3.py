print("hello")
team: list = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]
NUMBER = "number"
AGE = "age"
NAME = "name"
VALUE = NUMBER

def repr_players(players: list([dict]), sort: bool = False, key=lambda x: x[VALUE]
) -> None:
    v = input("If you want sorted team press: 'Enter',\n" 
    "if you want sorted at NAME press: '1',\n if you want sorted at 'AGE' press: '2'  ")
    
    print("The TEAM:")
    if sort:
        for player in players:
            print(
                f"\t{player['number']} - Name:{player['name']}, Age:{player['age']}"
            )
