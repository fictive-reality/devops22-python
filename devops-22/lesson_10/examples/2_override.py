from car import Car
from electric import ElectricCar

# regnr, manufacturer, model, year, color


def a_car():
    volvo = Car.create_car("ccc333", "Volvo", "XC60", "2018", "orange")
    volvo.open_hood()


def a_electric_car():
    tesla = ElectricCar.create_car(
        "bbb777", "tesla", "Model 3", "2020", "grey")
    tesla.open_hood()


def main():
    a_car()
    a_electric_car()


if __name__ == '__main__':
    main()
