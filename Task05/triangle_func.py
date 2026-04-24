class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a: float, b: float, c: float) -> str:
    """
    Определяет тип треугольника.

    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 4, 3)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides
    """

    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise IncorrectTriangleSides("Стороны должны быть числами")

    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными")

    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Треугольник не существует")

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"