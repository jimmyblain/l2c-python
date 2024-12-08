# 9-11, 9-12
''' Generic User class, imported by Admin class for more details.'''

class User:
    '''Represent a user of a common system/service'''

    def __init__(self, first_name, last_name, age, gender, is_active=True):
        '''Initializing the User object'''
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.is_active = is_active
        self.login_attempts = 0

    def describe_user(self):
        '''Lists out attributes of the User object'''
        print(f"\nFull name: {self.full_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender.title()}")
        print(f"Account Status: {self.is_active}")

    def greet_user(self):
        '''Greets the user and informs them of their account status'''
        print(f"\nHello {self.full_name.title()}!")
        if self.is_active:
            print("Your account is in good standing.")
        else:
            print("Your account is disabled.")

    def increment_login_attempts(self, login_attempt):
        '''Increment the login attempt by 1'''
        self.login_attempts += login_attempt

    def reset_login_attempts(self):
        '''Reset login attempts to 0'''
        self.login_attempts = 0
    
    def get_login_attempts(self):
        '''Print login attempts for given object'''
        print(f"\n{self.first_name.title()} has {self.login_attempts} login attempts.")

