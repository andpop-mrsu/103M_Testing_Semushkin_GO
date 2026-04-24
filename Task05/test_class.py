import pytest
from triangle_class import Triangle, IncorrectTriangleSides


# Позитивные тесты

def test_equilateral():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"


def test_isosceles_basic():
    t = Triangle(3, 4, 3)
    assert t.triangle_type() == "isosceles"


def test_scalene():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"


def test_isosceles_second_variant():
    t = Triangle(5, 5, 8)
    assert t.triangle_type() == "isosceles"


def test_float_values():
    t = Triangle(2.5, 2.5, 3.0)
    assert t.triangle_type() == "isosceles"


def test_perimeter():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12


# Негативные тесты

def test_triangle_inequality_equal_boundary():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)


def test_triangle_inequality_less():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 4)


def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)


def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 3)


def test_invalid_type_string():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 2, 3)


def test_invalid_type_none():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(None, 2, 3)


def test_all_zeros():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 0, 0)