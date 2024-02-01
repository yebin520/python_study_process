#car.py
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

my_new_car = Car ('audi','a4',2019)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_500)
my_new_car.print_odometer()

my_new_car.increment_miles(1000)
my_new_car.print_odometer()