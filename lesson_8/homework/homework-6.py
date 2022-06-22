from abc import ABC, abstractclassmethod
from random import choice
from typing import List


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("\n----\n|  |\n----\n")


class Circle(Shape):
    def draw(self):
        print("\n -- \n-  -\n -- \n")


def get_shape() -> Shape:
    options: List[Shape] = [Rectangle(), Circle()]
    return choice(options)


def main():
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
