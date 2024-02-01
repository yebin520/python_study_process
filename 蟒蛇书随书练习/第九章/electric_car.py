#electric_car.py
class Car:
    """docstring for Car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year =year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else:
            print ("You can't roll back an odometer")

    def increment_miles(self,miles):
        if miles >= 0:
            self.odometer_reading += miles
        else :
            print ("You can't roll back an odometer")
    
    def print_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
    def describe_battery (self):
        print (f"This car's battery size is {self.battery_size}")
    def get_range (self):
        if self.battery_size >=100 :
            range = 351
        elif self.battery_size < 100:
            range = 250
        print (f"This car can go about {range}miles on a full charge")
    def update_battery(self):
        if self.battery_size <100:
            self.battery_size = 100

class ElectricCar(Car):
    """docstring for ElectricCar"""

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()