# 9-1, 2, 4

# Class names should always be capitalized.
class Restaurant:
    '''Representation of a restaurant'''

    # Required method, runs every time a new object is initialized
    # Self is a required argument, everything else is dependent on your class
    def __init__(self, name, cuisine):
        '''Initialize attributes to describe a restaurant'''
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        '''Print name and cuisine of restaurant'''
        print(f"\nThe name of this restaurant is {self.name.title()}.")
        print(f"They serve {self.cuisine.title()} here.")

    def open_restaurant(self):
        '''Print that the restaurant in open'''
        print(f"Good news! {self.name.title()} is open today!")

    def set_number_served(self, served):
        '''Set the value for number of patrons served.'''
        self.number_served = served

    def increment_number_served(self, served):
        '''Increment the value of number of patrons served by the value passed'''
        self.number_served += served

    def get_number_served(self):
        '''Print number of patrons served for passed object'''
        print(f"\n{self.name.title()} has served {self.number_served} customers.")

# 9-6
# Creating a child class to the parent class Restaurant
# Class names are written in CamelCase
class IceCreamStand (Restaurant):
    '''Modeling an ice cream stand, which is a type of restraurant'''
    def __init__(self, name, cuisine):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to the child class
        '''
        #super() is a special method that calls a method from the parent class
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def get_flavors(self):
        '''Returns the list of flavors'''
        flavor_list = self.flavors[:]
        return flavor_list
    


burger_king = Restaurant('burger king', 'fast food')
ribbys = Restaurant("Ribby's", 'haitian')

burger_king.describe_restaurant()
burger_king.open_restaurant()
ribbys.describe_restaurant()
ribbys.open_restaurant()

burger_king.get_number_served()
burger_king.set_number_served(5)
burger_king.get_number_served()
burger_king.increment_number_served(10)
burger_king.get_number_served()

coldstone = IceCreamStand('Cold Stone', 'Dessert')
coldstone.describe_restaurant()
print(coldstone.get_flavors())