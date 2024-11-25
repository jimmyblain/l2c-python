#5-3,4,5

alien_color = 'red'
if alien_color == 'green':
    print("That's the right color!")

if alien_color == 'red':
    print("That's the right color!")

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!!")
elif alien_color == 'red':
    print("You just earned 20 points!!!")

#5-6

person_age = 5684
if person_age < 2:
    stage = 'Baby'
elif (person_age >=2) and (person_age < 4):
    stage = 'Toddler'
elif (person_age >=4) and (person_age < 13):
    stage = 'Preeteen'
elif (person_age >=13) and (person_age < 20):
    stage = 'Teenager'
elif (person_age >=20) and (person_age < 65):
    stage = 'Adult'
elif (person_age >=65):
    stage = 'Elder'

if stage != 'Elder':
    print(f"You are a {stage.lower()}.")
else:
    print(f"You are an {stage.lower()}.")
