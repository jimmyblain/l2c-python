# 9-14
from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']

attempts = 0
lottery_picks = []
while attempts < 4:
    lottery_picks.append(choice(lottery))
    attempts+=1

print(lottery_picks)

# 9-15 - How many tries will it take to win the lott
# Reseting/Setting base values
attempts = 0
tries_til_win = 0
lottery_picks = []
my_pick = [1, 2, 3, 4]

# Run until my pick matches the random selection
while lottery_picks != my_pick:
    while attempts < 4:
        lottery_picks.append(choice(lottery))
        attempts+=1
    
    # When they match, print the amount of tries it took.
    if lottery_picks == my_pick:
        print(f'\nThis took {tries_til_win} tries.')
        break
    # When they don't match, reset every and increment tries by 1
    else:
        lottery_picks = []
        attempts = 0
        tries_til_win+=1