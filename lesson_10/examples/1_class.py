from car import Car


def create_manually():
    # Constructor argument
    volvo = Car('abc123')

    # Only regnr is set
    print(volvo)

    volvo.manufacturer = 'volvo'
    volvo.model = 'XC90'

    # No setter for color
    # volvo.color = 'red'

    # Year has setter
    volvo.year = '2019'

    # Setter will validate year
    # volvo.year = 'abc'
    print(volvo)


def create_with_factory():
    saab = Car.create_car('aaa111', 'saab', '900', '1994', 'yellow')
    print(saab)


def main():
    create_manually()
    create_with_factory()


if __name__ == '__main__':
    main()
