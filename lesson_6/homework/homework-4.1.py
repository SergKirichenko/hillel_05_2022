# Homework-4 - Decorators Part 1
def reverse_str(reverse=True):
    def wrapper(func):
        def inner(*args):
            if args:
                text, *_ = args
                result = (
                    (text[::-1] if reverse else text) if isinstance(text, str) else None
                )
            else:
                text = func()
                result = (
                    (text[::-1] if reverse else text) if type(text) == str else None
                )
            return result

        return inner

    return wrapper


@reverse_str()
def get_string():
    return "Western Institute of Technology and Higher Education"


@reverse_str(False)
def get_not_string():
    return 1957


if __name__ == "__main__":
    print(get_string("Western Institute of Technology and Higher Education"))
    print(get_string(1957))
    print(get_string())
    print(get_not_string())
    print(get_not_string(2020))
    print(get_not_string("Education it's well"))
