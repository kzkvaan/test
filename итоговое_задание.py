class Car:

    """ Базовый класс """

    def __init__(self, марка, годвыпуска):

        if not isinstance(марка, str):
            raise TypeError ("Марка должна быть строкой !")

        if not isinstance(годвыпуска, int):
            raise TypeError ("Год выпуска должен быть числом !")
        if годвыпуска <= 0:
            raise ValueError("Годы выпуска должен быть положительным числом !")

        self._марка = марка
        self._годвыпуска = годвыпуска

    def __str__(self):
        return f'Машина марки"{self._марка}", {self._годвыпуска} года выпуска '

    def __repr__(self):
        return f"{self.__class__.__марка__}({self._марка!r}, {self._годвыпуска!r}) "


class PassengerCar(Car):

    """Класс для легкового автомобиля"""

    def __init__(self, марка, годвыпуска, цвет):

        super().__init__(марка, годвыпуска)
        self._цвет= цвет


    def __str__(self) -> str:
        return f'Машина марки"{self._марка}", {self._годвыпуска} года выпуска, {self._цвет} цвета '

    def __repr__(self) -> str:
        return f"{self.__class__.__марка__}({self._марка!r}, {self._годвыпуска!r}, {self._цвет!r})"


class Lorrry(Car):
    """
    Класс для грузового автомобиля
    """
    def __init__(self, марка, годвыпуска,грузоподъемность):

        super().__init__(марка, годвыпуска)
        self._грузоподъемность= грузоподъемность

    def __str__(self) -> str:
            return f'Машина марки"{self._марка}", {self._годвыпуска} года выпуска, {self._грузоподъемность} тонн '

    def __repr__(self) -> str:
            return f"{self.__class__.__марка__}({self._марка!r}, {self._годвыпуска!r}, {self._грузоподъемность!r})"



