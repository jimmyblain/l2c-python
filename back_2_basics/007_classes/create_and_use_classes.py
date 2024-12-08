#9-1, 2

#Class names should always be capitalized.
class Restaurant:
    '''Representation of a restaurant'''

    #Required method, runs every time a new object is initialized
    #Self is a required argument, everything else is dependent on your class
    def __init__(self, name, cuisine):
        """Initialize attributes to describe a restaurant"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        '''Print name and cuisine of restaurant'''
        print(f"The name of this restaurant is {self.name.title()}.")
        print(f"They serve {self.cuisine.title()} food here.")

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
        print(f"\n{self.name.title()} has served {self.number_served} customers.")

    

    


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