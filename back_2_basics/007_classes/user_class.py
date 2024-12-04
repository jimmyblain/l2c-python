#9-3

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

    def describe_user(self):
        print(f"\nFull name: {self.full_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender.title()}")
        print(f"Account Status: {self.is_active}")

    def greet_user(self):
        print(f"\nHello {self.full_name.title()}!")
        if self.is_active:
            print("Your account is in good standing.")
        else:
            print("Your account is disabled.")


baromega = User("Jimmy", "Blain", 32, "Male", False)
lishspeaks = User("Lish", "Blain", 36, "Female")
baromega.describe_user()
lishspeaks.describe_user()
baromega.greet_user()
lishspeaks.greet_user()

        