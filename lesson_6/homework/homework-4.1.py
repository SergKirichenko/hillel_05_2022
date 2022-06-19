# Homework-4 - Decorators Part 1
def reverse_string(reverse=True):
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


@reverse_string()
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string(False)
def get_university_founding_year():
    return 1957


if __name__ == "__main__":
    print(get_university_name("Western Institute of Technology and Higher Education"))
    print(get_university_name(1957))
    print(get_university_name())
    print(get_university_founding_year())
    print(get_university_founding_year(2020))
    print(get_university_founding_year("Education it's well"))
