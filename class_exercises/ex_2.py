# ex_2.py
# By Aspen
# Create your own class and add various attributes and methods.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)

car = Vehicle("Toyota", "Prius", 2014)
car.print_info()
