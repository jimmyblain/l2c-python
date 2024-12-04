#7-3

#Setting a flag to be used in the while loop
active = True

while active:
    toppings = input("Enter your desired pizza topping, or the word 'quit': ")
    if toppings != 'quit':
        print(f"You've added {toppings.upper()}")
    else:
        active = False

#7-4

tickets_needed = input("How many tickets do you need? ")
tickets_needed = int(tickets_needed)
tickets_given = 0

while tickets_given <= tickets_needed:
    age = input("\nHow old are you? (enter 'quit' to stop the program: )")
    
    #Break out of the loop 
    if age == 'quit':
        break
    
    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    #Increment by 1
    tickets_given += 1 
