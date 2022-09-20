# In this exercise you will write two alternative solutions, one with inheritance and one with composition.

#### Composition

# 1. Create a class `Address` with street name, street number, postal code, country.
# 2. Create a class `Employee` that has an address class, employee number and salary

# Composition = Has-A-Relation
# I think it basicly means that in composition, we can "borrow" methods from
# another class, which been done below with "address"

# ------------------------------------EXERCISE 1(Composition)------------------------------------

class Address:

    def __init__(self, street_name, street_number, postal_code, country):
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.country = country
        
# ------------------------------------EXERCISE 2(Composition)------------------------------------

class Employee:
    def __init__(self, address, employee_number, salary):
        self.address = address
        self.employee_number = employee_number
        self.salary = salary

    def __str__(self):
        return f"Employee {self.employee_number} lives on {self.address.street_name}"

address = Address("Axelvold", "3230", "26878", "Sweden")
employee = Employee(address, "0864273", 25000)

print(employee)