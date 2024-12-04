#8-1

#Defining a function with no parameters
def display_message():
    """Display a simple message"""
    print("I'm learning about functions, which are self-contained blocks of code.")

display_message()

#8-2
#Definiting a function that acceptes a string parameter.
def favorite_book (title):
    """Accept a string, use it to display a message."""
    print(f"My favorite book is {title.title()}.")

favorite_book('the bible')
    
#8-3, 4

#Define default values for parameters, which the variables will be set to is no arguement is passed.
def make_shirt (size='large', text='I love Python'):
    """Print a message about shirt size and text on shirt."""
    print(f"\nThe size of the shirt is a(n) {size.upper()}.")
    print(f"The shirt will read '{text}'.")

#Passing positional arguements (order matters).
make_shirt('Xxl', 'I like turtles')

#Passing keyword arguements (order does not matter).
make_shirt(text='I love programming', size='small')

#Function will use default values when no parameters are passed.
make_shirt()
make_shirt(text = "It's really late right now")

#8-7

def describe_city(city_name, city_country='America'):
    print(f"\n{city_name.title()} is located in {city_country}.")

describe_city('Brooklyn')
describe_city('Atlanta')
describe_city('Barcelona', 'Spain')