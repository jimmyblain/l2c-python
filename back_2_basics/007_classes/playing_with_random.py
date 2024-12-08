# 9-13
from random import randint

class Die:
    '''Represents a six-sided die'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        self.roll = randint(1, self.sides)
        print(f"You rolled a {self.roll}")

    
regular_die = Die()
attempts = 0

while attempts < 10:
    regular_die.roll_die()
    attempts+=1

ten_sided_die = Die(10)
attempts = 0

while attempts < 10:
    ten_sided_die.roll_die()
    attempts+=1    