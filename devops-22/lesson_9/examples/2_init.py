
# Minimal Class with init method
class Car:
    def __init__(self):
        pass


# Instantiate Car

volvo = Car()


# Minimal meaningful __init__

class Car:
    def __init__(self, regnr):
        self.regnr = regnr


volvo = Car("abc123")
print(volvo.regnr)

# It will fail if a argument is missing
# saab = Car() # TypeError: __init__() missing 1 required positional argument: 'regnr'
