import functools


def mask_info(func):
    def wrapper(*args):
        print("mid")
        name, age = args
        k = len(name)
        return func(name="*" * k, age=age)

    print("start")
    return wrapper


@mask_info
def get_user(name: str, age: int):
    return {"name": name, "age": age}


print(get_user("John", 23))


# MODIFY THIS DECORATOR


def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mask = func(*args, **kwargs)
            mask[target_key] = replace_with * len(mask[target_key])
            return mask

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
