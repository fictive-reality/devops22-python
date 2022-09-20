
# Basic example

class A:
    pass


class B(A):
    pass


print(issubclass(B, A))
print(A.__subclasses__())
print(B.__bases__)

b = B()


# Complete example

class Shape:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name.capitalize()} {self.__dict__}"


class Rectangle(Shape):

    def __init__(self, b, l, ):
        super().__init__('rectangle')
        self.b = b
        self.l = l

    def area(self):
        return self.b * self.l


rect = Rectangle(2, 3)
print(rect.area())
print(rect)
