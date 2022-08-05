class Car:
    '''Representing a car'''
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        # capacity in gallons, initial fuel level is 0
        self.fuel_tank_capasity=25
        self.fuel_level=0
    def fill_fuel(self):
        print("Filling the tank to the fullest")
        self.fuel_level = self.fuel_tank_capasity
    def get_fuel_level(self):
        print("Returning the fuel level")
        return self.fuel_level
    def __str__(self):
        return(f"{self.make} {self.model} {self.year} fuel level ={self.fuel_level}")