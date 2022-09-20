# 1. Create a class Square:
#    1. The Square takes 1 argument `side`
#    2. The Square should have a method `area`
    #   1. Area is calculated by side ** 2
    #   2. Area should be returned as a float
#    3. The Square should have a method `circumference`
    #   1. Circumference is calculated by side * 4
    #   2. Circumference should be returned as a float
# 2. Instantiate a object for
#    1. a square with side 2 and calculate the area & circumference
#    2. a square with side 3.5 and calculate the area & circumference

# ------------------------------------EXERCISE 1------------------------------------

class Square:
    def __init__(self, side):
        self.side = side
# ------------------------------------EXERCISE 1.2------------------------------------
    def area(self):
        return float(self.side * 2)
# ------------------------------------EXERCISE 1.3------------------------------------    
    def circumference(self):
        return float(self.side * 4)

# if __name__ == '__main__':
    # square = Square(7)  

# side = Square(4)
# side.area()
# side.circumference()

# ------------------------------------EXERCISE 2------------------------------------

if __name__ == '__main__':
    side1 = Square(2)
    print(side1.area())    
    print(side1.circumference())

    side1 = Square(3.5)
    print(side1.area()) 
    print(side1.circumference())