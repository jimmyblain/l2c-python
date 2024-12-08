# 9-12
# Import user class specifically to avoid the need for dot notation.
from user import User

class Privileges:
    '''Contains available privileges for an admin user'''
    def __init__(self, privileges = ['can add post', 'can delete posts', 'can ban user']):
        self.privileges = privileges
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title())


class Admin(User):
    '''Represent an administrator user object with special permissions'''
    def __init__(self, first_name, last_name, age, gender, is_active=True):
        super().__init__(first_name, last_name, age, gender, is_active)

        # Creating an Privileges instance within the Admin class as an attribute.
        self.privileges = Privileges()