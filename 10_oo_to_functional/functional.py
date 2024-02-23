from math import pi
from typing import Callable
from functools import partial


# rectangle functions
def rectangle_area(width: float, height: float) -> float:
    return width * height


def rectangle_perimeter(width: float, height: float) -> float:
    return 2 * (width + height)

# square functions


def square_area(side_length: float) -> float:
    return rectangle_area(side_length, side_length)


def square_perimeter(side_length: float) -> float:
    return rectangle_perimeter(side_length, side_length)

# circle functions


def circle_area(radius: float) -> float:
    return pi * radius**2


def circle_perimeter(radius: float) -> float:
    return 2 * pi * radius

# get total area and perimeter


def total_area(*area_funcs: Callable[[], float]) -> float:
    return sum(area_func() for area_func in area_funcs)


def total_perimeter(*perimeter_funcs: Callable[[], float]) -> float:
    return sum(perimeter_func() for perimeter_func in perimeter_funcs)


def main() -> None:
    print("Total Area:",
          total_area(
              partial(square_area, 3),
              partial(rectangle_area, 4, 5),
              partial(circle_area, 2)
          ))
    print("Total Perimeter:",
          total_perimeter(
              partial(square_perimeter, 3),
              partial(rectangle_perimeter, 4, 5),
              partial(circle_perimeter, 2)
          ))


if __name__ == "__main__":
    main()
