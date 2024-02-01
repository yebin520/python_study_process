#restaurant.py
class Restaurant:
    """docstring for Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print (f"The restaurant's name is {self.restaurant_name},and the cuisine type is {self.cuisine_type}")
    def open_restaurant (self):
        print (f"The restaurant is opening")

        
first_restaurant = Restaurant("久久","龙虾")
second_reataurant = Restaurant("豪景","鲍鱼")
first_restaurant.describe_restaurant()
second_reataurant.describe_restaurant()