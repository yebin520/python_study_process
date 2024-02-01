# dog.py
class Dog:
    """docstring for Dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"The {self.name} is sitting now!")

    def roll_over(self):
        print(f"The {self.name} is rolling now!")


my_dog = Dog('Cj', 16)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()
