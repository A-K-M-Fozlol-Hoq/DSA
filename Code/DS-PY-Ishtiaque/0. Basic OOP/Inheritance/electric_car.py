from car import Car
from battery import Battery
class ElectricCar(Car):
    '''Repreents an electric car'''
    def __init__(self, make, model, year):
        super().__init__(make, model,year)
        # battery in kWh , charge level in %
        # self.battery_size=70
        # self.charge_level=0
        self.battery= Battery(70)
    def charge_battery_full(self):
        self.battery.charge_level=100
    def get_charge_level(self):
        return self.battery.charge_level
    def fill_fuel(self):
        print("Electric car don't have any fuel tank. Can't fill it")
    def get_fuel_level(self):
        print("Electric car don't have any fuel tank.")
