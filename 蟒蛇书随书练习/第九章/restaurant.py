#restaurant.py
class Restaurant:
    """docstring for Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served (self,number):
        self.number_served = number

    def increment_served_number (self,increment_number):
        self.number_served +=increment_number

    def describe_restaurant(self):
        print (f"The restaurant's name is {self.restaurant_name},and the cuisine type is {self.cuisine_type}")
    
    def open_restaurant (self):
        print (f"The restaurant is opening")

        
first_restaurant = Restaurant("久久","龙虾")
print (first_restaurant.restaurant_name)
print (first_restaurant.cuisine_type)
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()

first_restaurant.set_number_served(20)
print (first_restaurant.number_served)
first_restaurant.increment_served_number(10)
print(first_restaurant.number_served)