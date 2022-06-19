def reverce_str(func):
    def wrapper(text: str):
        if isinstance(text, str):
            result = text[::-1]
        else:
            result = None
        return result

    return wrapper


@reverce_str()
def get_string(text: str = input("Print text: ")):
    return text


if __name__ == "__main__":
    print(get_string())
