#Die.py
from random import randint
class  Die:
    """docstring for  Die"""
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self):
        print (randint(1,self.sides))
die1 = Die (10)
die2 = Die (20)
for i in range (10):
    die1.roll_die()
for i in range (10):
    die2 .roll_die()