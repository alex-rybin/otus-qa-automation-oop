class Figure:
    def __init__(self, area: float, perimeter: float, angles: int, name: str):
        self.name = name
        self.area = area
        self.angles = angles
        self.perimeter = perimeter

    def add_square(self, figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError(f'Can only receive Figure as argument, got {type(figure).__name__}')
        else:
            return self.area + figure.area


class Triangle(Figure):
    def __init__(self, area: float, perimeter: float):
        super().__init__(area, perimeter, 3, 'triangle')


class Rectangle(Figure):
    def __init__(self, area: float, perimeter: float):
        super().__init__(area, perimeter, 4, 'rectangle')


class Square(Rectangle):
    def __init__(self, area: float, perimeter: float):
        super().__init__(area, perimeter)
        self.name = 'square'


class Circle(Figure):
    def __init__(self, area: float, perimeter: float):
        super().__init__(area, perimeter, 0, 'circle')
