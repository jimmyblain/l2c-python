# 10-11, 12
from pathlib import Path
import json

# Reference this file with this variable
path = Path('back_2_basics/008_files_and_exceptions/favorite_number.json')

# Only run if the file exists at the specified path
if path.exists():
    # Store the data at this location in this variable
    contents = path.read_text()
    # Load the JSON data into this variable
    favorite_number = json.loads(contents)
    print(f"I know your favorite number. It's: {favorite_number}")
else:
    favorite_number = input('Enter your favorite number: ')
    # Format this number for JSON files and store in variable
    contents = json.dumps(favorite_number)
    # Write JSON-formated data to file
    path.write_text(contents)
    print("I'll never forget!!!")

