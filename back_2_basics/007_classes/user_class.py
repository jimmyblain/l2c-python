# 9-3, 5

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

# 9-8
class Privileges:
    '''Contains available privileges for an admin user'''
    def __init__(self, privileges = ['can add post', 'can delete posts', 'can ban user']):
        self.privileges = privileges
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title())
# 9-7
class Admin(User):
    '''Represent an administrator user object with special permissions'''
    def __init__(self, first_name, last_name, age, gender, is_active=True):
        super().__init__(first_name, last_name, age, gender, is_active)

        # Creating an Privileges instance within the Admin class as an attribute.
        self.privileges = Privileges()


baromega = User("Jimmy", "Blain", 32, "Male", False)
lishspeaks = User("Alicia", "Blain", 36, "Female")
baromega.describe_user()
lishspeaks.describe_user()
baromega.greet_user()
lishspeaks.greet_user()

lishspeaks.get_login_attempts()

lishspeaks.increment_login_attempts(1)
lishspeaks.increment_login_attempts(1)
lishspeaks.increment_login_attempts(1)       
lishspeaks.increment_login_attempts(1)
lishspeaks.get_login_attempts()

lishspeaks.reset_login_attempts()
lishspeaks.get_login_attempts()

sudo = Admin('John', 'Doe', 63, 'Non-Binary')
sudo.describe_user()

# Calling a method from the privilege class on a privilege object attribute within the Admin class
sudo.privileges.show_privileges()