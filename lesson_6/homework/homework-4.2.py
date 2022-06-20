# Homework 4 - Decorators Part 2


def mask_info(dict_key: str, mask="*"):
    def wrapper(func):
        def inner(name: str, age: int):
            return {dict_key: (mask * len(name)), "age": age}

        return inner

    return wrapper


@mask_info("name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


if __name__ == "__main__":
    print(get_user("bob", 33), get_user("Alice", 15), sep="\n")

###############################################################################################
# Homework 4 - Decorators Part 2.1


def mask_info(func):
    def wrapper(name: str, age: int):
        return {"name": ("*" * len(name)), "age": age}

    return wrapper


@mask_info
def get_user(name: str, age: int):
    return {"name": name, "age": age}


if __name__ == "__main__":
    print(get_user("bob", 33), get_user("Alice", 15), sep="\n")
