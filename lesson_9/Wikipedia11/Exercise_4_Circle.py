# 1. Create a class Circle
#    1. Provide the diagonal as a argument
#    2. Import pi from math.pi
#    3. Calculate the area in a method
#    4. Calculate the circumference in a method
#    5. Use your created methods to calculate the area and circumference directly in `__init__`
#    6. Add a color variable, the default color should be `grey` for all objects
#    7. Add a method that can set a variable color on the circle i.e `my_circle.set_color("red`)

# ------------------------------------EXERCISE 1------------------------------------

# How to area;
# radius = d/2
# diameter = 2 * r
# Area =  pi * r2
# circumference =  2 * pi * r

from math import pi

class Circle:
    def __init__(self, diagonal):
        self.diagonal = diagonal
        self.color = "grey"
        self.area = self.get_area
        self.circumference = self.get_circumference
        self.radius = self.get_radius
        
    def get_radius(self):
        radius = self.diagonal / 2
        return radius

    def get_area(self):
        area = pi * self.get_radius() ** 2
        return area
    
    def get_circumference(self):
        circumference = pi * self.diagonal
        return circumference
    
    def change_color(self, color):
        self.color = color

        
if  __name__ == "__main__":
    diameter = Circle(4)
    print(round(diameter.get_area(), 7))
    print(round(diameter.get_circumference(), 7))
    diameter.change_color("red")
    print(diameter.color)