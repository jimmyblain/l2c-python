#5-1,2

car = 'toyota'
if car == 'toyota':
    print(f"That's right, I drive a {car.title()}.\n")

print("Is my car a Nissan? I predeict false.")
print(car == 'Nissan')

#This will fail due to case sensitivity. 
#Use methods like lower() to clean data before comparison.
print("Is my car a Toyota? I predeict false.")
print(car == 'Toyota')

#5-7
cars = ['toyota','subaru','nissan','ford','bmw']
if 'Toyota'.lower() in cars: #Note the syntax used when checking if a value is in a List.
    print("We have that make.")

if ('toyota') or ('tesla') in cars:
    print("We have one of those makes.")

if ('toyota') and ('tesla') in cars:
    print("We have one of those makes.")
else:
    print("We're missing one or both of those models.")