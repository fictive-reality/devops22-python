#### Inheritance

# 1. Create a class named `Person`, it should have `address` stored, with street name, street number, postal code, country.?
# 2. Create a class `Employee` that uses `Person´ as base class. Add employee number and salary.

# ------------------------------------EXERCISE 1(Inheritance)------------------------------------

class Person:

    def __init__(self, street_name, street_number, postal_code, country):
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.country = country

# ------------------------------------EXERCISE 2(Inheritance)------------------------------------

class Employee(Person):

    def __init__(self, street_name, street_number, postal_code, country, employee_number, salary):
        super().__init__(street_name, street_number, postal_code, country)
        self.employee_number = employee_number
        self.salary = salary

    def __str__(self):
        return f"Employee {self.employee_number} lives on {self.street_name}"

employee = Employee("Inteckningvägen", "17D", "12931", "Sweden", "0864273", 25000)
print(employee)