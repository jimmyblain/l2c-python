# 9-10
'''A class used to represent a restaurant'''

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