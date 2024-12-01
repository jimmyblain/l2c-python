#7-1

rental_car = input("Enter your desired rental car: ")
print(f"\nYou have reserved a {rental_car.title()}.")

#7-2
#Breaking up long strings. Appending the second line to the first.
long_message = "We have tables available for small parties. For large parties, there may be a wait."
long_message += "\nHow large is your party? "

#User input is always read as a string. Use int() method to convert to an integer.
party_size = input(long_message)
party_size = int(party_size)

if party_size > 8:
    print(f"Your party of {party_size} will need to wait for an available table.")
else:
    print(f"Your party size of {party_size} can now be seated.")

#7-3

div_by_ten = input("Enter a number and I will tell you if its divisible by 10: ")
div_by_ten = int(div_by_ten)

if div_by_ten % 10 == 0:
    print(f"The number {div_by_ten} is divisible by 10.")
else:
    print(f"The number {div_by_ten} is NOT divisible by 10.")