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
