# 10-13, 14
from pathlib import Path
import json

#This code has been modified to accept multiple user details isntead of only username

def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

# Modified to input three pieces of data
# Passed all input to a new dictionary, stored that in JSON file
def get_new_user(path):
    """Prompt for a new username."""
    username = input("What is your username? ")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    user = {'un' : username, 'f_name' : first_name, 'l_name' : last_name}
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def confirm_user(user):
    '''Confirm is the current user is correct'''
    answer = input(f"Are you user {user['un'].upper()} ? Enter Y or N: ").lower()
    if answer != 'n' and answer != 'y':
        print("Invalid input. Please try again.")
        confirm_user(user)
    elif answer == 'n':
        return False
    else:
        return True

def greet_user():
    """Greet the user by name."""
    path = Path('back_2_basics/008_files_and_exceptions/username.json')
    user = get_stored_user(path)
    if user:
        if confirm_user(user):
            print(f"Welcome back, {user['un'].upper()}!")
            print(f"We'll remember you when you come back, {user['un']}!")
        else:
            user = get_new_user(path)
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['un']}!")

greet_user()
