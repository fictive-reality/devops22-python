from datetime import datetime


class Car:

    def __init__(self, regnr):
        self.regnr = regnr
        self._color = None
        self._year = None
        self.manufacturer = None
        self.model = None

    def open_hood(self):
        print(self)
        print("Open the hood, showing nice engine")

    # Python encapsulation
    @property
    def color(self):
        return self._color

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not self.valid_year(year):
            raise ValueError('Not valid year')
        self._year = year

    def valid_year(self, year):
        try:
            datetime.strptime(year, '%Y')
            return True
        except Exception:
            return False

    @classmethod
    def create_car(cls, regnr, manufacturer, model, year, color):
        clazz = cls(regnr)
        clazz.manufacturer = manufacturer
        clazz.model = model
        clazz.year = year
        clazz._color = color
        return clazz

    def __str__(self):
        return f'{self.manufacturer} - {self.model} [{self.year}] with color {self.color} and regnr {self.regnr}'
