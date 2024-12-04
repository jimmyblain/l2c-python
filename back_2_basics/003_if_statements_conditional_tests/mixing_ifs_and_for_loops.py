#5-8, 9 , 10

usernames = ['jBlain', 'lgerald', 'admin', 'fgardner', 'bWord']


if usernames: #Checking if list has elements
    for username in usernames: #Go through this loop if list has elements
        if username.lower() == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in.")
else: #Print this message if list is empty
    print("We need to find some users!")

new_users = ['bbrown', 'whouston', 'JBlain', 'Bword', 'jzee']

#Making copy of list and forcing lower case
current_users = [users.lower() for users in usernames]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username {new_user.lower()} is unavailable.")
    else:
        print(f"The username {new_user.lower()} is free to use.")

#5-11
ordinals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal in ordinals:
    if ordinal > 3:
        print(f"{ordinal}th")
    elif ordinal == 1:
        print(f"{ordinal}st")
    elif ordinal == 2:
        print(f"{ordinal}nd")
    elif ordinal ==3:
        print(f"{ordinal}rd")