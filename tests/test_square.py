import pytest

from figures import Square


@pytest.mark.parametrize('name', ['random_name', 'square', '12345', 'teeeeeest', '_____'])
def test_name(name):
    """
    Проверка на корректность заданного имени
    """
    square = Square(name, 1, 1, 3, 3)
    assert square.name == name


def test_area():
    """
    Проверка на корректность вычисления площади
    """
    square = Square('name', 1, 1, 4, 4)
    assert square.area == 9


def test_perimeter():
    """
    Проверка на корректность вычисления периметра
    """
    square = Square('name', 1, 1, 4, 4)
    assert square.perimeter == 12


def test_angles():
    """
    Проверка на корректность количества углов
    """
    square = Square('name', 1, 1, 2, 2)
    assert square.angles == 4


def test_add_square():
    """
    Проверка работы метода сложения площадей
    """
    square1 = Square('name1', 1, 1, 3, 3)
    square2 = Square('name2', 1, 1, 2, 2)
    assert square1.add_square(square2) == 5
