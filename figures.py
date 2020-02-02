import math
from abc import abstractmethod


class Figure:
    name = None
    _area = None
    _angles = None
    _perimeter = None

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @property
    def area(self) -> float:
        return self._area

    @property
    def angles(self) -> int:
        return self._angles

    @property
    def perimeter(self) -> float:
        return self._perimeter

    def add_square(self, figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError(
                f'Can only receive Figure as argument, got {type(figure).__name__}'
            )
        else:
            return self.area + figure.area


class Triangle(Figure):
    def __init__(
        self, name: str, x0: float, y0: float, x1: float, y1: float, x2: float, y2: float,
    ):
        super().__init__(name)
        self._angles = 3
        side_a = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        side_b = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        side_c = math.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)
        self._perimeter = side_a + side_b + side_c
        half_per = self._perimeter / 2
        self._area = math.sqrt(
            half_per * (half_per - side_a) * (half_per - side_b) * (half_per - side_c)
        )


class Rectangle(Figure):
    def __init__(
        self, name: str, x0: float, y0: float, x1: float, y1: float,
    ):
        """
        Указываем только две противоположных вершины
        """
        super().__init__(name)
        self._angles = 4
        length = abs(x1 - x0)
        height = abs(y1 - y0)
        self._perimeter = (length + height) * 2
        self._area = length * height


class Square(Rectangle):
    def __init__(self, name: str, x0: float, y0: float, x1: float, y1: float):
        if abs(x1 - x0) != abs(y1 - y0):
            raise ValueError('Not a square')
        super().__init__(name, x0, y0, x1, y1)


class Circle(Figure):
    def __init__(self, name, radius: float):
        """
        Координаты центра не указываем, т.к. в текущем контексте не важны
        """
        super().__init__(name)
        self._area = math.pi * radius ** 2
        self._perimeter = math.pi * radius * 2
        self._angles = 0
