from car import Car


class ElectricCar(Car):

    def open_hood(self):
        print(self)
        print("Open the hood, no engine found")
