# 1. Create a class that has at least one method
# 2. Create a subclass that uses your class (1) as base class
# 3. In the subclass (2) you should override the method from (1)
# 4. Print a instance of (1) and (2) both calling the same method name


# ------------------------------------EXERCISE 1------------------------------------

class Dog:
    def __init__(self, size):
        self.size = size
        self.breed = None

    def woof(self):
        print(self)
        print("Woof")     
        
        
    @classmethod
    def create_dog(cls, size, breed):
        clazz = cls(size)
        clazz.breed = breed
        return clazz
    
    def __str__(self):
        return f"{self.size} - {self.breed}"

class Pitbull(Dog):
    
    def woof(self):
        print(self)
        print("WOOF BITCH")


def a_dog():
    dobberman = Dog.create_dog("Big", "Dobberman")
    dobberman.woof()

def a_angrier_dog():
    pitbull = Pitbull.create_dog("Super big", "Pitbull")
    pitbull.woof()

def main():
    a_dog()
    a_angrier_dog()
    
if __name__ == "__main__":
    main()


