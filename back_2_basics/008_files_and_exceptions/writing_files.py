# 10-4
from pathlib import Path

# Prompting the user for their name and writing it to a txt file
your_name = input('Please enter your name: ')

#If the file doesn't exist at this path, Python will create it
file_path = Path('back_2_basics/008_files_and_exceptions/guest.txt')
# This method always replaces the entire txt file with the new strings
file_path.write_text(your_name)

# 10-5
# Saving a list of names to a file
# There's probably a better way to do this using lists

guest_amount = int(input('How many guests are attending tonight? '))
guest_count = 1
guest_list = ''

while guest_count <= guest_amount:
    guest_name = input(f'Enter the name of guests: ')
    guest_name += '\n'
    # Store names in one large string
    guest_list += guest_name
    guest_count += 1

guest_book_path = Path('back_2_basics/008_files_and_exceptions/guest_book.txt')
guest_book_path.write_text(guest_list)