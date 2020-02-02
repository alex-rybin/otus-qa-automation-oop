import pytest

from figures import Circle


@pytest.mark.parametrize('name', ['random_name', 'circle', '12345', 'teeeeeest', '_____'])
def test_name(name):
    """
    Проверка на корректность заданного имени
    """
    circle = Circle(name, 1)
    assert circle.name == name


def test_area():
    """
    Проверка на корректность вычисления площади
    """
    circle = Circle('name', 2)
    assert round(circle.area, 2) == 12.57


def test_perimeter():
    """
    Проверка на корректность вычисления длины окружности
    """
    circle = Circle('name', 3)
    assert round(circle.perimeter, 2) == 18.85


def test_angles():
    """
    Проверка на корректность количества углов
    """
    circle = Circle('name', 1)
    assert circle.angles == 0


def test_add_square():
    """
    Проверка работы метода сложения площадей
    """
    circle1 = Circle('name1', 2)
    circle2 = Circle('name2', 3)
    assert round(circle1.add_square(circle2), 2) == 40.84
