#8-12.py
def sandwich(*food_names):
    for food_name in food_names:
        print(food_name)
    print(food_names)

sandwich('A','B','C')