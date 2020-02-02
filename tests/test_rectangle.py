import pytest

from figures import Rectangle


@pytest.mark.parametrize('name', ['random_name', 'rectangle', '12345', 'teeeeeest', '_____'])
def test_name(name):
    """
    Проверка на корректность заданного имени
    """
    rectangle = Rectangle(name, 1, 1, 3, 3)
    assert rectangle.name == name


def test_area():
    """
    Проверка на корректность вычисления площади
    """
    rectangle = Rectangle('name', 1, 1, 2, 4)
    assert rectangle.area == 3


def test_perimeter():
    """
    Проверка на корректность вычисления периметра
    """
    rectangle = Rectangle('name', 1, 1, 4, 2)
    assert rectangle.perimeter == 8


def test_angles():
    """
    Проверка на корректность количества углов
    """
    rectangle = Rectangle('name', 1, 1, 1, 2)
    assert rectangle.angles == 4


def test_add_square():
    """
    Проверка работы метода сложения площадей
    """
    rectangle1 = Rectangle('name1', 1, 1, 3, 2)
    rectangle2 = Rectangle('name2', 1, 1, 2, 2)
    assert rectangle1.add_square(rectangle2) == 3
