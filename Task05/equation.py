import math
from typing import Tuple, Union


class QuadraticEquationError(Exception):
    pass


def solve_quadratic(a: float, b: float, c: float) -> Union[Tuple[float, float], Tuple[float], tuple]:
    """
    Решает уравнение ax^2 + bx + c = 0

    Возвращает:
    - () — если нет корней
    - (x,) — если один корень
    - (x1, x2) — если два корня (в порядке возрастания)
    """


    if a == 0:
        raise QuadraticEquationError("Коэффициент 'a' не может быть равен 0")

    d = b ** 2 - 4 * a * c

    if d < 0:
        return ()
    elif d == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return tuple(sorted((x1, x2)))