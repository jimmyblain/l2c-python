#8-12

#Single * asterisk creates a list (tuple) of arbitrary size in function
#Able to accept as many arguments that are passed to it
def sandwich_order(*toppings):
    """Print the toppings of the sandwich order."""
    print("\nYour sandwich toppings are: ")
    for topping in toppings:
        print(f"- {topping.title()}")
    
sandwich_order('bread', 'ham', 'cheese')
sandwich_order('roll', 'meatballs', 'marinara sauce', 'mozzarella')
sandwich_order('bagel', 'cream cheese')

#8-13
#Doube ** asterisks creates a list of arbritrary size in the function
#Accepts any key-value pair arguments, after the required positional arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing user info provided."""

    #Set this key-value pair since these are always passed in any function call
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

my_profile = build_profile('Jimmy', 'Blain', location = 'Atlanta', age = 32, occupation = 'IT Director')
print(my_profile)

#8-14

def build_car(manufacturer, model_name, **car_info):
    """Build a dictionary of car information. Manufacturer and Model Name required."""

    car_info['maker'] = manufacturer
    car_info['model'] = model_name

    return car_info

my_car = build_car('Toyota', 'Camry 2022', miles = 48000, color = 'black', insured = True)
print(my_car)