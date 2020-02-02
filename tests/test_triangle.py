import pytest

from figures import Triangle


@pytest.mark.parametrize('name', ['random_name', 'triangle', '12345', 'teeeeeest', '_____'])
def test_name(name):
    """
    Проверка на корректность заданного имени
    """
    triangle = Triangle(name, 1, 1, 3, 3, 2, 5)
    assert triangle.name == name


def test_area():
    """
    Проверка на корректность вычисления площади
    """
    triangle = Triangle('name', 1, 1, 2, 2, 3, 1)
    assert round(triangle.area) == 1


def test_perimeter():
    """
    Проверка на корректность вычисления периметра
    """
    triangle = Triangle('name', 1, 1, 1, 2, 2, 1)
    assert round(triangle.perimeter, 2) == 3.41


def test_angles():
    """
    Проверка на корректность количества углов
    """
    triangle = Triangle('name', 1, 1, 1, 2, 2, 1)
    assert triangle.angles == 3


def test_add_square():
    """
    Проверка работы метода сложения площадей
    """
    triangle1 = Triangle('name1', 1, 1, 1, 2, 2, 1)
    triangle2 = Triangle('name2', 1, 1, 2, 2, 3, 1)
    assert round(triangle1.add_square(triangle2), 1) == 1.5
