from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        length, breadth = 3, 4
        for i in range(length):
            if i == 0 or i == (length - 1):
                for j in range(breadth):
                    print("-", end="")
                print()
            else:
                for j in range(breadth):
                    if j == 0 or j == breadth - 1:
                        print("|", end="")
                    else:
                        print(" ", end="")
                print()


class Circle(Shape):
    def draw(self):
        length, breadth = 3, 4
        for i in range(length):
            if i == 0 or i == (length - 1):
                for j in range(breadth):
                    if j == 0 or j == (breadth - 1):
                        print(" ", end="")
                    else:
                        print("-", end="")
                print()
            else:
                for j in range(breadth):
                    if j == 0 or j == (breadth - 1):
                        print("-", end="")
                    else:
                        print(" ", end="")
                print()


def get_shape() -> Shape:
    options: list[Shape] = [Circle()]
    return choice(options)


def main():
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
