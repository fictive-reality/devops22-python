class DieselEngine:

    def __init__(self):
        self.hp = 400
        self.has_hood = True


class ElectricEngine:
    def __init__(self):
        self.hp = 700
        self.has_hood = False


class Car:

    def __init__(self, engine):
        self.engine = engine

    def open_hood(self):
        if(self.engine.has_hood):
            print(
                f'Open the hood, showing nice engine of type {type(self.engine)}')

        else:
            print(f'Open the hood, no engine found')


def main():
    car = Car(DieselEngine())
    car.open_hood()

    electricCar = Car(ElectricEngine())
    electricCar.open_hood()


if __name__ == '__main__':
    main()
