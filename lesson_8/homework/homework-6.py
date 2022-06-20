from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        # horizon_line = self.h_line
        # vertical_line = self.v_line
        pass


class Rectangle(Shape):
    """Change me"""


class Circle(Shape):
    """Change me"""


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = ["change_me"]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
